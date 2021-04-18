from pathlib import Path
# from django.contrib.messages import constants as messages
# import os
import environ

#  ! ENV
env = environ.Env()
environ.Env.read_env()
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = env('SECRET_KEY')
DEBUG = int(env('DEBUG', default=0))
# ENVIRONMENT = env('ENVIRONMENT', default='development')

# /////////////////////////////////////////////////////////////////////////
# ! Application definition

INSTALLED_APPS = [
    # Django Admin Interface
    # 'admin_interface',
    # 'colorfield',
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
    'pages.apps.PagesConfig',
    'service.apps.ServiceConfig',
    'orders.apps.OrdersConfig',

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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', 
#         'NAME': 'slahly',
#         'USER': 'admin',
#         'PASSWORD': 'root',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

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
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

# /////////////////////////////////////////////////////////////////////////
# ! Stripe

STRIPE_TEST_PUBLISHABLE_KEY = env('STRIPE_TEST_PUBLISHABLE_KEY')
STRIPE_TEST_SECRET_KEY = env('STRIPE_TEST_SECRET_KEY')

# /////////////////////////////////////////////////////////////////////////
# ! Password validation

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# /////////////////////////////////////////////////////////////////////////
# ! Security
# if ENVIRONMENT == 'production':
#     SECURE_BROWSER_XSS_FILTER = True
#     X_FRAME_OPTIONS = 'DENY'
#     SECURE_SSL_REDIRECT = True
#     SECURE_HSTS_SECONDS = 3600
#     SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#     SECURE_HSTS_PRELOAD = True
#     SECURE_CONTENT_TYPE_NOSNIFF = True
#     SESSION_COOKIE_SECURE = True
#     CSRF_COOKIE_SECURE = True
#     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


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