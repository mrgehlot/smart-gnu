from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', smart_gnu_apis)
router.register("mqtt_api",mqtt_apis, basename='mqtt_api')
router.register("university", universityviewset, basename='university')
router.register("department", departmentviewset, basename='department')
router.register("devices", devicesviewset, basename='devices')

urlpatterns = [
    path('', include(router.urls)),
]
