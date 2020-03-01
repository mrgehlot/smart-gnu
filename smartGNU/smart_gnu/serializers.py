from rest_framework import serializers
from .views import *
from .models import *
class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    class Meta:
        model = CollegeUser
        fields = ('id','username', 'user_type', 'profile_image', 'email')


class GoogleAuthCodeSerializer(serializers.Serializer):
    code = serializers.CharField()
    class Meta:
        fields = ('code')

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ('id','college_name')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id','department_name','college')

class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = ('id','lab_number','department')

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id','device_name', 'topic', 'message', 'lab')

class MqttSerializer(serializers.Serializer):
    topic = serializers.CharField()
    payload = serializers.BooleanField()
    class Meta:
        fields = ('topic','payload')

# class UserTypeSerializer(serializers.Serializer):
#
#     class Meta:
#         fields = ('id','user_type')

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = ('id', 'email','user_type')
