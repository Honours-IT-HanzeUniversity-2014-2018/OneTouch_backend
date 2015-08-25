import os, sys

sys.path.append('/home/onetouch/backend/app')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.core import wsgi
application = wsgi.get_wsgi_application()