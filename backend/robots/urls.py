from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('robots/', views.robots_list),
    path('robots/<int:id>/', views.robot_detail),
]