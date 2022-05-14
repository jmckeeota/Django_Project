from django.urls import include, path
from django.conf import settings
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('robots', views.RobotViewSet, basename='robots')
router.register('modules', views.ModuleViewSet)

robots_router = routers.NestedDefaultRouter(router, 'robots', lookup='robot')
robots_router.register('comments', views.CommentViewSet, basename='robot-comments')
#URLConf
urlpatterns = router.urls + robots_router.urls

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns