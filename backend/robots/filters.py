from django_filters.rest_framework import FilterSet
from .models import Robot, ModuleItem, Module

class RobotFilter(FilterSet):
    class Meta:
        model = Robot
        fields = {
            'moduleitem__module_id': ['exact']
        }