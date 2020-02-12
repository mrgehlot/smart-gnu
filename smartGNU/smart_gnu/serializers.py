from rest_framework.serializers import ModelSerializer
from .views import *
from .models import *
class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'user_type', 'profile_image', 'email')


class UniversitySerializer(ModelSerializer):
    class Meta:
        model = University
        fields = ('id','university_name')


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ('id','department_name','university')


class DevicesSerializer(ModelSerializer):
    class Meta:
        model = Devices
        fields = ('id','device_name', 'topic', 'message', 'department')
