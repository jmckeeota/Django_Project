from robots.models import Robot, Module, ModuleItem
from rest_framework import serializers

class RobotModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['skill', 'description']

class Module_setSerializer(serializers.ModelSerializer):
    module = RobotModuleSerializer()

    class Meta:
        model = ModuleItem
        fields = ['module', 'quantity']

class RobotSerializer(serializers.ModelSerializer):
    modules = Module_setSerializer(source='moduleitem_set', many=True, read_only=True)

    class Meta:
        model = Robot
        fields = ['id', 'name', 'built', 'firmware', 'modules']

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'skill', 'description']