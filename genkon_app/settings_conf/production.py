from .base import *
import os

with open(os.path.join(BASE_DIR,'genkon_app/secret_key.txt')) as f:
  SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

with open(os.path.join(BASE_DIR,'genkon_app/db_password.txt')) as f:
  DB_PASSWORD = f.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'genkondb',
        'USER': 'jonasrothfuss',
        'PASSWORD': DB_PASSWORD,
        'HOST': 'genkon-db-instance.c1c9nmiz9egh.eu-central-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
"""

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'db_log': {
            'level': 'WARNING',
            'class': 'django_db_logger.db_log_handler.DatabaseLogHandler'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['db_log'],
            'level': 'WARNING',
            'propagate': True,
        }
    }
}

#TODO: HTTPS
#CSRF_COOKIE_SECURE = True
#SESSION_COOKIE_SECURE = True