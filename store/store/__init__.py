import os

import django

from .celery import app as celery_app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
django.setup()


__all__ = ('celery_app',)