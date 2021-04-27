"""
To use the application you should comment init SECRET_KEY, DEBUG, DATABASE.
For SECRET_KEY you can user the key commented beside.
For DEBUG you can user True.
For DATABASE you can comment MySQL or reconfig it or comment out SQLite3 Database
For Stripe and email you can will find constractions below
"""

from pathlib import Path
import environ

#  ! ENV
env = environ.Env()
environ.Env.read_env()
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = env('SECRET_KEY') # 'tm9vlx8c3#xb5@z17!8n(=-8g6bj9(-d!@6cn$r+_#%qd#3j_c'
DEBUG = int(env('DEBUG', default=0)) # True
# ENVIRONMENT = env('ENVIRONMENT', default='development')

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
COMPRESS_ENABLED = env('COMPRESS_ENABLED')
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
#         'NAME': env('DATABASE_NAME'),
#         'USER': env('DATABASE_USER'),
#         'PASSWORD': env('DATABASE_PASSWORD'),
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
EMAIL_HOST_USER = env('EMAIL_HOST_USER') # User any email
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD') # User any password

# /////////////////////////////////////////////////////////////////////////
# ! Stripe

STRIPE_TEST_PUBLISHABLE_KEY = env('STRIPE_TEST_PUBLISHABLE_KEY')
STRIPE_TEST_SECRET_KEY = env('STRIPE_TEST_SECRET_KEY')

# For any other user uncomment this and comment two lines above
# STRIPE_TEST_PUBLISHABLE_KEY = '0'
# STRIPE_TEST_SECRET_KEY = '0'

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

# /////////////////////////////////////////////////////////////
# ! django-debug-toolbar

# INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

# DEBUG_TOOLBAR_CONFIG = {
#     'DISABLE_PANELS': [
#         'debug_toolbar.panels.redirects.RedirectsPanel',
#     ],
#     'SHOW_TEMPLATE_CONTEXT': True,
# }
# DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False,}

# def show_toolbar(request):
#     return True

# DEBUG_TOOLBAR_CONFIG = {
#     "SHOW_TOOLBAR_CALLBACK" : lambda request: True,
# }
# //////////////////////////////////////////////////////////////