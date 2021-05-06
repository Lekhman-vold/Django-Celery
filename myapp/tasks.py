import string
import random
from celery import shared_task

from .models import MyModel, TestModel
from .test_utl import get_todo


@shared_task
def create_new_objects():
    random_name = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
    new_object = MyModel.objects.create(name=random_name)
    return new_object.name


@shared_task()
def get_last_info():
    t = get_todo()
    new_title = TestModel.objects.create(title=t)
    return new_title.title
