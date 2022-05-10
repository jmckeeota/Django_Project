from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from robots.models import Module, Robot, Owner, ModuleItem
from .serializers import RobotSerializer, ModuleSerializer

class RobotViewSet(ModelViewSet):
    queryset = Robot.objects.prefetch_related('moduleitem_set__module').select_related('firmware').all()
    serializer_class = RobotSerializer

    def get_serializer_context(self):
        return{'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if ModuleItem.objects.filter(module_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Robot cannot be deleted because it has associated moduleitems'})

        return super().destroy(request, *args, **kwargs)

class ModuleViewSet(ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    def get_serializer_context(self):
        return{'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if ModuleItem.objects.filter(module_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Module cannot be deleted because it has associated moduleitems'})

        return super().destroy(request, *args, **kwargs)

# Create your views here.
def say_hello(request):
    query_set = Owner.objects.annotate(
        robot_count=Count('robot')
    )

    return render(request, 'hello.html', {'name': 'Jason', 'results': list(query_set)})