from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from robots.models import Module, Robot, Owner
from .serializers import RobotSerializer

# Create your views here.
def say_hello(request):
    query_set = Owner.objects.annotate(
        robot_count=Count('robot')
    )

    return render(request, 'hello.html', {'name': 'Jason', 'results': list(query_set)})

@api_view()
def robots_list(request):
    queryset = Robot.objects.select_related('firmware').all()
    serializer = RobotSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def robot_detail(request, id):
    robot = get_object_or_404(Robot, pk=id)
    serializer = RobotSerializer(robot)
    return Response(serializer.data)