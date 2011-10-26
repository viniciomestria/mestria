import os, sys
sys.path.append('/home/vinicio/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mestria.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
