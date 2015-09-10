# This file contains development specific settings
# Base settings should go to settings/base.py
# Production settings should go to settings/production.py
from fir.config.base import *

# DEBUG to True to have helpful error pages
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Sqlite3 database backend
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Do not send real emails, print them to the console instead:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# Dummy key for development
SECRET_KEY = 'DUMMY_KEY_FOR_DEVELOPMENT_DO_NOT_USE_IN_PRODUCTION'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated'),
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.SessionAuthentication'),
}

#REST_FRAMEWORK = {
#   '''Use hyperlinked styles by default'''
#   '''only used if serializer_class attribute is not set on a view'''
#   'DEFAULT_MODEL_SERIALIZER_CLASS':
#         'rest_framkework.serializers.HyperLinkedModelSerializer',
#   'DEFAULT_PERMISSION_CLASSES':
#          'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
# }

try:
    from fir.config.dev import *
except ImportError:
    pass
