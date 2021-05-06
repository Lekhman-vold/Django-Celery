from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class TestModel(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
