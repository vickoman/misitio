"""
Django settings for misitio project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'izxbymnjv8^yi!m-e6gpg!%oqqa*-f8y%pr7v6yz+7o12c94^_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',   
    'misitio.apps.main', 
    'south',
    'social_auth',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'misitio.urls'

WSGI_APPLICATION = 'misitio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
           'read_default_file' :  os.path.join(BASE_DIR, 'my.cnf'),
        },
    }
}
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}




# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, 'misitio/media')
STATIC_ROOT = os.path.join(BASE_DIR, 'misitio/static') 
#STATICFILES_DIRS = (
#       os.path.join(BASE_DIR, 'misitio/static'),
#    )
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'misitio/templates')
    )  
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "misitio.apps.main.context_processors.topvotciones",
    "misitio.apps.main.context_processors.footertext"
    ) 
AUTHENTICATION_BACKENDS = (    
    'social_auth.backends.facebook.FacebookBackend',    
    'django.contrib.auth.backends.ModelBackend',
)

FACEBOOK_APP_ID='584126405013896'
FACEBOOK_API_SECRET='0c15d1460cbde1643bd4a03e80a28c81'

FACEBOOK_EXTENDED_PERMISSIONS = ['email']

LOGIN_URL          = '/login-form/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/login-error/'

USE_X_FORWARDED_HOST = True
