# Each setting is documented at:
# https://docs.djangoproject.com/en/1.9/ref/settings/

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

from .wsgi import application
import os
from django.utils.translation import gettext_lazy as _
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
SECURE_BROWSER_XSS_FILTER = False
SECURE_CONTENT_TYPE_NOSNIFF = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_SECONDS = 0
SECURE_PROXY_SSL_HEADER = None
SECURE_REDIRECT_EXEMPT = []
SECURE_SSL_HOST = None
SECURE_SSL_REDIRECT = False
USE_X_FORWARDED_HOST = False
USE_X_FORWARDED_PORT = False
X_FRAME_OPTIONS = "SAMEORIGIN"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG_PROPAGATE_EXCEPTIONS = False
SILENCED_SYSTEM_CHECKS = []
MESSAGE_STORAGE = "django.contrib.messages.storage.fallback.FallbackStorage"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

AUTH_USER_MODEL = "Authentication.User"

LOGIN_REDIRECT_URL = "/accounts/profile/"
LOGIN_URL = "/accounts/login/"
PASSWORD_RESET_TIMEOUT_DAYS = 1
PASSWORD_HASHERS = ["django.contrib.auth.hashers.PBKDF2PasswordHasher"]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation."
        "UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation." "MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation." "CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation." "NumericPasswordValidator",
    },
]

ABSOLUTE_URL_OVERRIDES = {}
ADMINS = []
MANAGERS = ADMINS
ALLOWED_HOSTS = []
ALLOWED_INCLUDE_ROOTS = []
APPEND_SLASH = True
PREPEND_WWW = False
DISALLOWED_USER_AGENTS = []
INTERNAL_IPS = []

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        # 'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        # 'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        # 'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        # 'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        # 'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
    }
}

CORS_ORIGIN_ALLOW_ALL = True

CSRF_COOKIE_AGE = 31449600  # one year
CSRF_COOKIE_DOMAIN = None
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_NAME = "csrftoken"
CSRF_COOKIE_PATH = "/"
CSRF_COOKIE_SECURE = False
CSRF_FAILURE_VIEW = "django.views.csrf.csrf_failure"
CSRF_HEADER_NAME = "HTTP_X_CSRFTOKEN"
CSRF_TRUSTED_ORIGINS = []
SIGNING_BACKEND = "django.core.signing.TimestampSigner"

SESSION_CACHE_ALIAS = "default"
SESSION_COOKIE_AGE = 1209600  # two weeks
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_NAME = "sessionid"
SESSION_COOKIE_PATH = "/"
SESSION_COOKIE_SECURE = False
SESSION_ENGINE = "django.contrib.sessions.backends.db"
# SESSION_ENGINE = 'django.contrib.sessions.backends.file'
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
# SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_FILE_PATH = None
SESSION_SAVE_EVERY_REQUEST = False
SESSION_SERIALIZER = "django.contrib.sessions.serializers.JSONSerializer"

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DATABASE_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.environ.get("DATABASE_NAME", "heimdalerp"),
        "USER": os.environ.get("DATABASE_USER", "heimdalerp"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD", "heimdalerp"),
        # Uncomment to use TCP/IP
        "HOST": os.environ.get("DATABASE_HOST", "localhost"),
        # Uncomment to use TCP/IP
        "PORT": os.environ.get("DATABASE_PORT", "5432"),
        "ATOMIC_REQUESTS": False,
        "AUTOCOMMIT": True,
        "CONN_MAX_AGE": 0,
        "OPTIONS": {},
        "TIME_ZONE": None,
        "TEST": {
            "NAME": "test_heimdalerp",
            "CHARSET": None,
            "COLLATION": None,
            "DEPENDENCIES": [],
            "MIRROR": None,
            "SERIALIZE": True,
            "USER": "heimdalerp",
            "PASSWORD": None,
        },
    }
}

DATABASE_ROUTERS = []

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("knox.auth.TokenAuthentication",),
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DEFAULT_CHARSET = "utf-8"
DEFAULT_CONTENT_TYPE = "text/html"
DEFAULT_EXCEPTION_REPORTER_FILTER = "django.views.debug.SafeExceptionReporterFilter"

DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
FILE_CHARSET = "utf-8"
FILE_UPLOAD_HANDLERS = [
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
]
FILE_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50MB
FILE_UPLOAD_DIRECTORY_PERMISSIONS = None
FILE_UPLOAD_PERMISSIONS = None
FILE_UPLOAD_TEMP_DIR = None  # defaults to '/tmp' on UNIX-like OSs

DEFAULT_FROM_EMAIL = "webmaster@localhost"
SERVER_EMAIL = "root@localhost"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "localhost"
EMAIL_PORT = 25
EMAIL_HOST_PASSWORD = ""
EMAIL_HOST_USER = ""
EMAIL_SUBJECT_PREFIX = "[HeimdalERP] "
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_SSL_CERTFILE = None
EMAIL_SSL_KEYFILE = None
EMAIL_TIMEOUT = None

FIRST_DAY_OF_WEEK = 0  # Sunday

FIXTURE_DIRS = []
FORCE_SCRIPT_NAME = None
FORMAT_MODULE_PATH = None
IGNORABLE_404_URLS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third party apps
    "rest_framework",
    "knox",
    "corsheaders",
    "reversion",
    "jazzmin",
    # HeimdalERP Custom Apps
    "rest_framework_proxy",
    "invoice_ar",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]
USE_ETAGS = False

ROOT_URLCONF = "heimdalerp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = application

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = "es"
LANGUAGE_COOKIE_AGE = None
LANGUAGE_COOKIE_DOMAIN = None
LANGUAGE_COOKIE_NAME = "django_language"
LANGUAGE_COOKIE_PATH = "/"

LOCALE_PATHS = ["locale"]

LANGUAGES = [
    ("en", _("English")),
    ("es", _("Spanish")),
]

TIME_ZONE = "America/Argentina/Buenos_Aires"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = ""  # '/var/www/heimdalerp/static/'
STATIC_URL = "/static/"
STATICFILE_DIRS = []
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_ROOT = ""  # '/var/www/heimdalerp/media/'
MEDIA_URL = "/media/"  # It could also be: 'http://media.example.com/'

TEST_RUNNER = "django.test.runner.DiscoverRunner"
TEST_NON_SERIALIZED_APPS = []

#
# CUSTOM MODULES SETTINGS
#

# invoice_ar
REST_PROXY = {"HOST": "https://soa.afip.gob.ar"}
