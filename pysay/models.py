
from django.db import models
from django.utils import timezone


class Cowsay(models.Model):
    default = 'cow'
    text = models.CharField(max_length=50)
    time = models.TimeField(default=timezone.now)
    change_cow = models.CharField(max_length=50, default=default)
