from django.contrib import admin
from .models import MyModel, TestModel

admin.site.register(MyModel)
admin.site.register(TestModel)

