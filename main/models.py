from django.db import models


class Url(models.Model):
    link = models.CharField(max_length=1000)
    uid = models.CharField(max_length=10)
