from robots.models import Robot, Module, ModuleItem
from rest_framework import serializers

class ModuleSerializer(serializers.Serializer):
    # module_id__id = serializers.IntegerField()
    # skill = serializers.CharField(max_length=255)
    module_id = serializers.PrimaryKeyRelatedField(
        queryset=ModuleItem.objects.all()
    )

class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = ['id', 'name', 'built', 'firmware', 'moduleitem_set']
    # id = serializers.IntegerField()
    # name = serializers.CharField(max_length=255)
    # model = serializers.CharField(max_length=255)
    # built = serializers.DateTimeField()
    # firmware = serializers.StringRelatedField()
    # module = ModuleSerializer()
    moduleitem_set = ModuleSerializer(many=True)
