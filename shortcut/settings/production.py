from .base import *
import dj_database_url

DEBUG = True

SECRET_KEY = os.environ['SECRET_KEY']

MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DATABASES = {'default': dj_database_url.config()}
DATABASES['default']['CONN_MAX_AGE'] = 500

AWS_STORAGE_BUCKET_NAME = 'shortcutdigital'
AWS_ACCESS_KEY_ID = 'AKIAIUXYGURJFOHWP73Q'
AWS_SECRET_ACCESS_KEY = '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'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

try:
    from .local import *
except ImportError:
    pass
