"""
WSGI config for racers project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'racers.settings')

application = get_wsgi_application()


# Make sure you bind to the correct port dynamically (for Render).
from wsgiref.simple_server import make_server
port = int(os.environ.get('PORT', 10000))  # Render sets the PORT environment variable
httpd = make_server('', port, application)
httpd.serve_forever()
