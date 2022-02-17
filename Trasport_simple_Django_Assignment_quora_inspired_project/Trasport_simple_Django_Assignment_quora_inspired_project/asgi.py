"""
ASGI config for Trasport_simple_Django_Assignment_quora_inspired_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Trasport_simple_Django_Assignment_quora_inspired_project.settings')

application = get_asgi_application()
