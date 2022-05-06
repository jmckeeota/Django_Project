from backend.robots.models import Robot
from rest_framework import serializers

class ModuleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    skill = serializers.CharField(max_length=255)

class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = ['id', 'name', 'built', 'firmware']
    # id = serializers.IntegerField()
    # name = serializers.CharField(max_length=255)
    # model = serializers.CharField(max_length=255)
    # built = serializers.DateTimeField()
    # firmware = serializers.StringRelatedField()
    # module = ModuleSerializer()
