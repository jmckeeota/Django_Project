from django.urls import include, path
from django.conf import settings
from rest_framework.routers import DefaultRouter
from . import views
from pprint import pprint

router = DefaultRouter()
router.register('robots', views.RobotViewSet)
router.register('modules', views.ModuleViewSet)
pprint(router.urls)


#URLConf
urlpatterns = router.urls

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns