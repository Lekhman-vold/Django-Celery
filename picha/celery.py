from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'picha.settings')
app = Celery('picha', broker='redis://127.0.0.1:6379')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    'creating_new_objects': {
        'task': 'myapp.tasks.create_new_objects',
        'schedule': 15.0,
    },
    'task_save_latest_flickr_image': {
        'task': 'myapp.tasks.get_last_info',
        'schedule': 10.0
    }
}
