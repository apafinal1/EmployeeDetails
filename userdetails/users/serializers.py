from rest_framework import serializers
from rest_framework_tricks.serializers import (
    HyperlinkedModelSerializer,
)
from .models import Employee


class ActivityPeriodsSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(required=False)
    end_time = serializers.DateTimeField(required=False)
    
    class Meta(object):
        model = Employee
        fields = (
            "start_time", 
            "end_time")
        nested_proxy_field = True


class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    real_name = serializers.CharField(required=False)
    tz = serializers.CharField(required=False)
    activity_periods = ActivityPeriodsSerializer(required=False, many =False)
    class Meta:
        model = Employee
        fields = (
            'id',
            'real_name',
            'tz',
            'activity_periods',
            )


