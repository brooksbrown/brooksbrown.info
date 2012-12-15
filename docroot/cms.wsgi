activate_this = '/var/www/brooksbrown.info/venv/bin/activate_this.py'
print execfile(activate_this, dict(__file__=activate_this))


import os
import sys
sys.path.append('/var/www/brooksbrown.info')
sys.path.append('/var/www/brooksbrown.info/cms')
os.environ['DJANGO_SETTINGS_MODULE'] = 'cms.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
