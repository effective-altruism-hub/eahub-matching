import os.path
from enum import Enum
from pathlib import Path

import dj_database_url
import environ
import sentry_sdk
from dotenv import load_dotenv
from sentry_sdk.integrations.django import DjangoIntegration


load_dotenv(".env.local")
load_dotenv(".env")
env = environ.Env()


class DjangoEnv(Enum):
    LOCAL = "local"
    STAGE = "stage"
    PROD = "prod"
    BUILD_DOCKER = "build_docker"


DJANGO_ENV_ENUM = DjangoEnv
DJANGO_ENV = DjangoEnv(env.str("DJANGO_ENV", DjangoEnv.LOCAL.value))


sentry_sdk.init(
    dsn=env.str("SENTRY_DSN", ""),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True,
)


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env.str(
    "SECRET_KEY", "django-insecure-(@=!o=kllqov0jt9hlu)qz%swsu)h8mx7=9bcf2zka1yn#aid#"
)

DEBUG = env.bool("DJANGO_DEBUG", True if DJANGO_ENV != DjangoEnv.PROD else False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "solo",
    "rest_framework",
    "rest_framework_simplejwt",
    "admin_reorder",
    "drf_yasg",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "import_export",
    "logentry_admin",
    "eahub",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "admin_reorder.middleware.ModelAdminReorder",
]

SITE_ID = 1

ROOT_URLCONF = "eahub.urls"

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

if DJANGO_ENV == DjangoEnv.BUILD_DOCKER:
    DATABASE_URL = "sqlite://:memory:"
else:
    DATABASE_URL = env.str("DATABASE_URL", "postgresql://postgres:@db:5432/db")

DATABASES = {"default": dj_database_url.parse(DATABASE_URL)}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static_collected")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
