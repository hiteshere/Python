from __future__ import unicode_literals

from django.db import models

# Create your models here.
class appList(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField()

class app(models.Model):
    # for unique value for every app we create for app list for manny to one relation
    app_list = models.ForeignKey(appList)
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    complete = models.BooleanField(default= True)