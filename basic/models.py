from django.db import models

# Create your models here.


class Competition(models.Model):

    name = models.CharField(max_length=30, blank=False)
    subject = models.CharField(max_length=10, blank=False)
    startTime = models.DateField(auto_now=True)
    endTime = models.DateField(auto_now=True)
    detail = models.TextField(default='')
    procedure = models.TextField(default='')
    enrollUrl = models.URLField(default='')
    charge = models.IntegerField(default=0)
