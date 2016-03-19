# -*- coding: utf-8 -*-
"""
Local settings for Family Laihonen project.

- Run in Debug mode
- Use console backend for emails
- Add django-extensions as app
"""

from .common import *  # noqa


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG


# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env("DJANGO_SECRET_KEY", default='7y!sv=5(4b(4^wpm!r+chb)%sq8&u&vt-3w7*h-=t9+yy4t(e_')


# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.console.EmailBackend')


# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}


# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('django_extensions', )


# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'


# Your local stuff: Below this line define 3rd party library settings
# ------------------------------------------------------------------------------
