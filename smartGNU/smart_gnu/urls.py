from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register('college_user', CollegeUserViewSet, basename='college_user')
router.register("college", Collegeviewset, basename='college')
router.register("department", Departmentviewset, basename='department')
router.register("lab", Labviewset, basename='lab')
router.register("device", Deviceviewset, basename='device')
router.register("user_type", UserTypeView, basename='user_type')
router.register("invitation", InvitationViewSet, basename='invitation')
router.register("node_mcu", NodeMCUViewSet, basename='node_mcu')

urlpatterns = [
    path('', include(router.urls)),
]
