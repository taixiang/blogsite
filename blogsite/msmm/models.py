from django.db import models

# Create your models here.

class Msmm(models.Model):
    count = models.IntegerField("数量", default=0)