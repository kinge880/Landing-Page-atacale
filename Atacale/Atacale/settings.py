import os
from pathlib import Path
from decouple import config, Csv
import mimetypes
mimetypes.add_type("text/css", ".css", True)

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool, default=False)
ALLOWED_HOSTS = ['*','atacale.com.br','atacale.com.br/trabalhe','www.atacale.com.br','www.atacale.com.br/trabalhe','atacale-vagas.cjnqj5zqtael.sa-east-1.rds.amazonaws.com', 'atacale.sa-east-1.elasticbeanstalk.com']
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'corsheaders',
    'landpage',
    'error',
    'phone_field',
    'django_crontab',
    'django_cleanup.apps.CleanupConfig',
    #'mailer',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Atacale.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join((BASE_DIR), 'templates/')],
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

WSGI_APPLICATION = 'Atacale.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
    #}
#}

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DATABASENAME'),
        'USER': config('DATABASESUSER'),
        'PASSWORD': config('DATABASESPASS'),
        'HOST': config('DATABASEHOST'),
        'PORT': config('DATABASEPORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Rio_Branco'

USE_I18N = True

USE_TZ = True

ADMINS = [('Bruno', 'erroirdjango@gmail.com')]

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'staticfiles'),
)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

MAX_UPLOAD_PDF_SIZE = 10485760
MAX_UPLOAD_IMAGE_SIZE = 5242880

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_BACKEND = 'mailer.backend.DbBackend'
DEFAULT_FROM_EMAIL = config('EMAILLOGIN')
SERVER_EMAIL = config('EMAILLOGIN')
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAILLOGIN')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

#CRONJOBS = [
   # ('*/1 * * * *', '/var/app/venv/staging-LQM1lest/bin/python3.8 /var/app/current/manage.py send_mail >> ~/cron_mail.log 2>&1'),
    #('*/30 * * * *', '/var/app/venv/staging-LQM1lest/bin/python3.8 /var/app/current/manage.py retry_deferred >> ~/cron_mail_deferred.log 2>&1'),
    #('1 0 * * 1', '/var/app/venv/staging-LQM1lest/bin/python3.8 /var/app/current/manage.py purge_mail_log 7 >> ~/cron_mail_purge.log 2>&1'),
#]