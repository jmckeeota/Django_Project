from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from robots.models import Module, Robot, Owner

# Create your views here.
def say_hello(request):
    query_set = Owner.objects.annotate(
        robot_count=Count('robot')
    )

    return render(request, 'hello.html', {'name': 'Jason', 'results': list(query_set)})