from pathlib import Path
from .secrets import *

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'tm9vlx8c3#xb5@z17!8n(=-8g6bj9(-d!@6cn$r+_#%qd#3j_c'
DEBUG = True

# /////////////////////////////////////////////////////////////////////////
# ! Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Apps
    'users.apps.UsersConfig',
    'service.apps.ServiceConfig',
    'contact.apps.ContactConfig',
    'employee.apps.EmployeeConfig',
    'request.apps.RequestConfig',
    'store.apps.StoreConfig',

    # 3td party apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'widget_tweaks',
    'crispy_forms',
    'djmoney',
    "compressor",
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'slahly.urls'
ALLOW_UNICODE_SLUGS = True
CRISPY_TEMPLATE_PACK = 'bootstrap4'
ALLOWED_HOSTS = ['*']
SITE_ID = 1
COMPRESS_ENABLED = True
WSGI_APPLICATION = 'slahly.wsgi.application'

# /////////////////////////////////////////////////////////////////////////
# ! Authentication

AUTH_USER_MODEL = 'users.User'
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_FORMS = {'signup': 'users.forms.UserCreationForm',
                 'login': 'allauth.account.forms.LoginForm',
                 'change_password': 'users.forms.ChangePasswordForm',}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# /////////////////////////////////////////////////////////////////////////
# ! Templates
TEMPLATE_DIR = Path.joinpath(BASE_DIR / 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# /////////////////////////////////////////////////////////////////////////
# ! Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', 
#         'NAME': DATABASE_NAME,
#         'USER': DATABASE_USER,
#         'PASSWORD': DATABASE_PASSWORD,
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# /////////////////////////////////////////////////////////////////////////
# ! Internationalization

LANGUAGE_CODE = 'ar-EG'

TIME_ZONE = 'Africa/Cairo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# /////////////////////////////////////////////////////////////////////////
# ! Static files

STATIC_URL = '/static/'

LANGUAGE_CODE = 'ar'

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    'compressor.finders.CompressorFinder',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# STATICFILES_DIRS = [Path.joinpath(BASE_DIR / 'staticfiles'),]
STATIC_ROOT = Path.joinpath(BASE_DIR / 'static',)

MEDIA_URL = '/media/'
MEDIA_ROOT = Path.joinpath(BASE_DIR, 'media/')

# /////////////////////////////////////////////////////////////////////////
# ! Email config

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = EMAIL_HOST_USER # User any email
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD # User any password

# /////////////////////////////////////////////////////////////////////////
# ! Stripe
# For any other user uncomment this and comment two lines above 
# but you can't pay at store
# STRIPE_TEST_PUBLISHABLE_KEY = '0'
# STRIPE_TEST_SECRET_KEY = '0'

STRIPE_TEST_PUBLISHABLE_KEY = STRIPE_TEST_PUBLISHABLE_KEY
STRIPE_TEST_SECRET_KEY = STRIPE_TEST_SECRET_KEY


# /////////////////////////////////////////////////////////////////////////
# ! Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
