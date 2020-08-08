from django.db import models
from rest_framework_tricks.models.fields import NestedProxyField


# Create your models here.
class Employee(models.Model):
    """ creating Employee fields"""

    id = models.IntegerField(primary_key=True)
    real_name = models.CharField(max_length=268)
    tz = models.CharField(max_length=129)
    start_time = models.DateTimeField(auto_created=True)
    end_time = models.DateTimeField(auto_created=True)
    
    # creating a nested json  using proxy field
    activity_periods = NestedProxyField(
       'start_time',
       'end_time',
    )
    class Meta(object):
        ordering = ['id']

    def __str__(self):
        return self.real_name
