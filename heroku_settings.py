"""Purplship Heroku specific django settings

This module extends the `purpleserver.settings` default settings and adds
additional config required to run purplship-server on Heroku.
"""
import logging
import dj_database_url
from purpleserver.settings import *


SECURITY, *EXTRA_MIDDLEWARE = MIDDLEWARE
MIDDLEWARE = [
    SECURITY,
    'whitenoise.middleware.WhiteNoiseMiddleware',
    *EXTRA_MIDDLEWARE
]


# Heroku: Update database configuration from $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

logging.warning("Purplship Heroku settings loaded...")
