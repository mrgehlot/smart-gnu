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
        fields = ('id','device_name', 'topic', 'message', 'gpio_pin','node_mcu')


class DeviceUpdateSerializer(serializers.Serializer):
    topic = serializers.CharField()
    payload = serializers.JSONField()
    message = serializers.CharField()
    class Meta:
        fields = ('topic','payload','message')



class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = ('id', 'email','user_type')

class NodeMCUCreateSerializer(serializers.Serializer):
    lab_number = serializers.CharField()
    node_mcu_ip = serializers.CharField()
    class Meta:
        fields = ('lab_number','node_mcu_ip')

class NodeMCUSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodeMCU
        fields = ('id', 'lab','node_mcu_ip')