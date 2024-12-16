from django.db import models
from django.utils.translation import gettext_lazy as _

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserTrackingModel(models.Model):
    created_by = models.ForeignKey(
        'auth.User', related_name='%(class)s_created', on_delete=models.SET_NULL, null=True, blank=True
    )
    updated_by = models.ForeignKey(
        'auth.User', related_name='%(class)s_updated', on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        abstract = True


class OrganizationModel(models.Model):
    organization = models.ForeignKey(
        'Organization', related_name='%(class)s_organization', on_delete=models.CASCADE
    )

    class Meta:
        abstract = True


class BasePersonModel(TimeStampedModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AddressModel(models.Model):
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    class Meta:
        abstract = True


class FinanceModel(TimeStampedModel):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=10, default='USD')

    class Meta:
        abstract = True


class InventoryModel(TimeStampedModel):
    item_name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True


class HRModel(BasePersonModel):
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    hire_date = models.DateField()

    class Meta:
        abstract = True


class CRMModel(BasePersonModel, AddressModel):
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class AuditTrailModel(TimeStampedModel):
    action = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True
