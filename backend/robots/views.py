from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import DefaultPagination
from .filters import RobotFilter
from .models import Module, Robot, Owner, ModuleItem, Comment
from .serializers import CommentSerializer, RobotSerializer, ModuleSerializer

class RobotViewSet(ModelViewSet):
    queryset = Robot.objects.prefetch_related('moduleitem_set__module').select_related('firmware').all()
    serializer_class = RobotSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = RobotFilter
    pagination_class = DefaultPagination
    search_fields = ['name']
    ordering_fields = ['id', 'name', 'built']

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

class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(robot_id=self.kwargs['robot_pk'])
    def get_serializer_context(self):
        return {'robot_id': self.kwargs['robot_pk']}

# Create your views here.
def say_hello(request):
    query_set = Owner.objects.annotate(
        robot_count=Count('robot')
    )

    return render(request, 'hello.html', {'name': 'Jason', 'results': list(query_set)})
