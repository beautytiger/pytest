# -*- coding: utf-8 -*-

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'publisher.settings')

app = Celery('publisher')
app.config_from_object('django.conf:settings')

# Load task module from all registered Django app configs.
app.autodiscover_tasks()
