"""
WSGI config for d1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import time
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd1.settings')

#rh: bringt nix, TZ kann man nicht  aendern  rrrrrrrrrrrrrr
#v1 os.environ.setdefault('TZ', 'Europe/Berlin')

#v2 os.environ["TZ"] = "Europe/Berlin"
#v2 time.tzset()




application = get_wsgi_application()

#v3 os.environ.setdefault('TZ', 'Europe/Berlin')

