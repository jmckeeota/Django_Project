from robots.models import Robot, Module, ModuleItem
from rest_framework import serializers

class ModuleSerializer(serializers.Serializer):
    skill = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)

class Module_setSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    module = ModuleSerializer()

class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = ['id', 'name', 'built', 'firmware', 'modules']

    modules = Module_setSerializer(source='moduleitem_set', many=True)
