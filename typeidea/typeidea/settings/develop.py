from .base import * # NOQA
import os


DEBUG = True

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea_db_new',
        'USER': 'root',
        'PASSWORD': 'mysecret',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        # 'CONN_MAX_AGE': 5 * 60,
        # 'OPTIONS': {'charset': 'utf8mb4'}
    },
}

INSTALLED_APPS += [
    'pympler',
    'debug_toolbar',
    # 'debug_toolbar_line_profiler',
    'silk',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'silk.middleware.SilkyMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': 'https://cdn.bootcss.com/jquery.min.js',
}

# DEBUG_TOOLBAR_PANELS = [
    # 'pympler.panels.MemoryPanel',
    # 'debug_toolbar_line_profiler.panel.ProfilingPanel',
    # 'djdt_flamegraph.FlamegraphPanel',
# ]
