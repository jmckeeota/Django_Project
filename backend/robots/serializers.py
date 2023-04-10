from robots.models import Robot, Module, ModuleItem, Comment, Owner
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

class OwnerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    class Meta:
        model = Owner
        fields = ['user_id']

class RobotSerializer(serializers.ModelSerializer):
    modules = Module_setSerializer(source='moduleitem_set', many=True, read_only=True)
    owner = OwnerSerializer()
    class Meta:
        model = Robot
        fields = ['id', 'name', 'built', 'firmware', 'modules', 'owner']

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'skill', 'description']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'date', 'name', 'description']

    def create(self, validated_data):
        robot_id = self.context['robot_id']
        return Comment.objects.create(robot_id=robot_id, **validated_data)
