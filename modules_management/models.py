from django.db import models, transaction
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.conf import settings

from core.models.core_models import (
    TimeStampedModel,
    UserTrackingModel,
    OrganizationModel,
)

import logging
from typing import List, Optional, Dict, Any

logger = logging.getLogger(__name__)


class ModuleCategory(TimeStampedModel):
    """
    Categorization for modules to provide better organization and filtering
    """

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text=_("CSS class or icon identifier for visual representation"),
    )
    color_code = models.CharField(
        max_length=7,
        blank=True,
        null=True,
        help_text=_("Hex color code for category visualization"),
    )

    class Meta:
        verbose_name = _("Module Category")
        verbose_name_plural = _("Module Categories")
        ordering = ["name"]

    def __str__(self):
        return self.name

    def clean(self):
        """
        Validate color code is a valid hex color
        """
        if self.color_code:
            import re

            if not re.match(r"^#(?:[0-9a-fA-F]{3}){1,2}$", self.color_code):
                raise ValidationError(
                    {"color_code": _("Enter a valid hex color code (e.g., #FF0000)")}
                )

    def get_module_count(self):
        """
        Return the number of modules in this category
        """
        return self.modules.count()


class ModuleModel(TimeStampedModel, UserTrackingModel, OrganizationModel):
    """
    Enhanced module model for comprehensive ERP system module management
    """

    class ModuleStatus(models.TextChoices):
        ACTIVE = "AC", _("Active")
        INACTIVE = "IN", _("Inactive")
        DEPRECATED = "DP", _("Deprecated")
        BETA = "BT", _("Beta")
        DEVELOPMENT = "DV", _("Development")

    class ModuleType(models.TextChoices):
        CORE = "CR", _("Core")
        EXTENSION = "EX", _("Extension")
        CUSTOM = "CM", _("Custom Module")
        THIRD_PARTY = "TP", _("Third-Party")

    # Validators
    version_validator = RegexValidator(
        regex=r"^\d+\.\d+(\.\d+)?$", message=_("Version must be in format X.Y or X.Y.Z")
    )

    # Basic Information
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Module Name"))
    description = models.TextField(
        blank=True, null=True, verbose_name=_("Module Description")
    )

    # Enhanced Versioning and Status
    version = models.CharField(
        max_length=20,
        validators=[version_validator],
        default="1.0.0",
        verbose_name=_("Module Version"),
    )
    status = models.CharField(
        max_length=2,
        choices=ModuleStatus.choices,
        default=ModuleStatus.ACTIVE,
        verbose_name=_("Module Status"),
    )
    module_type = models.CharField(
        max_length=2,
        choices=ModuleType.choices,
        default=ModuleType.EXTENSION,
        verbose_name=_("Module Type"),
    )

    # Categorization and Dependency Management
    category = models.ForeignKey(
        ModuleCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="modules",
        verbose_name=_("Module Category"),
    )
    dependencies = models.ManyToManyField(
        "self",
        symmetrical=False,
        blank=True,
        related_name="dependents",
        verbose_name=_("Module Dependencies"),
    )

    # Advanced Metadata
    short_code = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_("Short Code"),
        help_text=_("Unique short identifier for the module"),
    )
    documentation_url = models.URLField(
        blank=True, null=True, verbose_name=_("Documentation URL")
    )
    min_system_version = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[version_validator],
        verbose_name=_("Minimum System Version"),
    )

    # Performance and Tracking
    load_priority = models.IntegerField(
        default=0,
        verbose_name=_("Load Priority"),
        help_text=_("Lower numbers load first. Negative values allowed."),
    )
    total_installations = models.PositiveIntegerField(
        default=0, verbose_name=_("Total Installations")
    )

    # Licensing and Compliance
    license_type = models.CharField(
        max_length=100, blank=True, null=True, verbose_name=_("License Type")
    )
    is_open_source = models.BooleanField(
        default=False, verbose_name=_("Is Open Source")
    )

    class Meta:
        verbose_name = _("Module")
        verbose_name_plural = _("Modules")
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["name", "status"]),
            models.Index(fields=["short_code"]),
            models.Index(fields=["category"]),
        ]

    def __str__(self):
        return f"{self.name} (v{self.version})"

    def clean(self):
        """
        Validate module configurations
        """
        # Prevent circular dependencies
        if self.pk:
            if self in self.dependencies.all():
                raise ValidationError(_("A module cannot depend on itself"))

    def is_compatible(self, system_version: str) -> bool:
        """
        Check if module is compatible with given system version

        Args:
            system_version (str): System version to check compatibility against

        Returns:
            bool: Whether the module is compatible
        """
        if not self.min_system_version:
            return True

        try:
            from packaging import version

            return version.parse(system_version) >= version.parse(
                self.min_system_version
            )
        except ImportError:
            # Fallback to simple string comparison if packaging is not available
            return system_version >= self.min_system_version

    def increment_installations(self) -> None:
        """
        Increment total installations count
        """
        self.total_installations += 1
        self.save(update_fields=["total_installations"])

    @classmethod
    def get_active_modules(cls) -> models.QuerySet:
        """
        Retrieve all active modules

        Returns:
            QuerySet of active modules
        """
        return cls.objects.filter(status=cls.ModuleStatus.ACTIVE)

    @classmethod
    def get_modules_by_category(
        cls, category: Optional[ModuleCategory] = None
    ) -> models.QuerySet:
        """
        Retrieve modules filtered by category

        Args:
            category (Optional[ModuleCategory]): Category to filter by

        Returns:
            QuerySet of modules in the specified category
        """
        if category:
            return cls.objects.filter(category=category)
        return cls.objects.all()

    def check_dependencies(self) -> Dict[str, Any]:
        """
        Check module dependencies and their status

        Returns:
            Dict with dependency check results
        """
        dependency_status = {
            "all_dependencies_met": True,
            "missing_dependencies": [],
            "inactive_dependencies": [],
        }

        for dep in self.dependencies.all():
            if not ModuleModel.objects.filter(pk=dep.pk).exists():
                dependency_status["all_dependencies_met"] = False
                dependency_status["missing_dependencies"].append(dep.name)
            elif dep.status != self.ModuleStatus.ACTIVE:
                dependency_status["all_dependencies_met"] = False
                dependency_status["inactive_dependencies"].append(dep.name)

        return dependency_status

    @transaction.atomic
    def disable_module(self, reason: str = "") -> None:
        """
        Disable the module and log the action

        Args:
            reason (str, optional): Reason for disabling the module
        """
        try:
            self.status = self.ModuleStatus.INACTIVE
            self.save(update_fields=["status"])

            # Log the module disabling
            logger.info(f"Module {self.name} disabled. Reason: {reason}")
        except Exception as e:
            logger.error(f"Error disabling module {self.name}: {str(e)}")
            raise


class ModuleChangeLog(TimeStampedModel):
    """
    Track changes to modules for audit and tracking purposes
    """

    module = models.ForeignKey(
        ModuleModel, on_delete=models.CASCADE, related_name="change_logs"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    action = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _("Module Change Log")
        verbose_name_plural = _("Module Change Logs")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.module.name} - {self.action}"
