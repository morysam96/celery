from __future__ import absolute_import, unicode_literals
import time
from celery import shared_task

@shared_task
def add(x, y,t):
    time.sleep(t)
    return x + y