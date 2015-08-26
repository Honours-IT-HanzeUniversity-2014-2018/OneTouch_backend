import os

DEBUG = True

SETTINGS_PATH = os.path.dirname(os.path.realpath(__file__))
SITE_ROOT = os.path.abspath(os.path.join(SETTINGS_PATH, '../'))

ADMINS = (
    ('R. de Vries', 'r.devries@robbytu.net'),
    ('F. Noorlander', 'f.c.noorlander@st.hanze.nl'),
    ('K. Wierenga', 'k.y.wierenga@st.hanze.nl'),
    ('A. Tursic', 'a.tursic@st.hanze.nl'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'onetouch',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'middleware.xss.XsSharing'
)

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'res', 'shared'),
)

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'user',
)

ALLOWED_HOSTS = (
    'onetouch.local',
)

SITE_ID = 1
TIME_ZONE = 'Europe/Amsterdam'
LANGUAGE_CODE = 'nl-nl'
USE_TZ = True
SECRET_KEY = '5w3V5E93Y8p4m-2d4745^58fr848B85p^863hsfZ6Hb.82796d43xT97H78+d76u'
APPEND_SLASH = True
DEBUG_EMAIL_ADDRESS = ADMINS[0][1]
ROOT_URLCONF = 'urls'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')

# Import overriding local settings

try:
    from local_settings import *
except ImportError:
    pass