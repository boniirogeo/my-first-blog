"""
WSGI config for goban project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "goban.settings")

application = get_wsgi_application()

# Use whitenoise to serve static files on Heroku.com
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
