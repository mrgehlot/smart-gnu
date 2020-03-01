from rest_framework.viewsets import GenericViewSet,ViewSet,ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
import requests
from .models import *
from .serializers import UserProfileSerializer,\
                        CollegeSerializer,\
                        DepartmentSerializer,\
                        DeviceSerializer, \
                        LabSerializer,\
                        GoogleAuthCodeSerializer,\
                        MqttSerializer,\
                        InvitationSerializer
from rest_framework.authtoken.models import Token
from .mqtt_code import request_for_publish

class CollegeUserViewSet(ModelViewSet):
    queryset = CollegeUser.objects.all()
    serializer_class = GoogleAuthCodeSerializer
    authentication_classes = ()
    permission_classes = ()


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        google_response = requests.get(url='https://www.googleapis.com/oauth2/v3/userinfo',
                                       params={'access_token': request.data.get('code')})
        user_profile = google_response.json()
        user_obj = self.queryset.filter(user__email=user_profile.get('email')).first()
        if user_obj:
            if not user_obj.profile_image:
                user_obj.profile_image = user_profile.get('picture')
                user_obj.save()
        else:
            user = User.objects.create(email=user_profile.get('email'),
                                       username=user_profile.get('name'),
                                       first_name=user_profile.get('given_name'),
                                       last_name=user_profile.get('family_name'))
            user_obj = CollegeUser.objects.create(profile_image=user_profile.get('picture'),
                                                  user=user)

        user_data = UserProfileSerializer(user_obj).data
        token_obj, created = Token.objects.get_or_create(user=user_obj.user)
        user_data['user_token'] = token_obj.key
        return Response(data={"user": user_data}, status=status.HTTP_200_OK)




class Collegeviewset(ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    authentication_classes = ()
    permission_classes = ()

class Departmentviewset(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('college',)
    authentication_classes = ()
    permission_classes = ()

class Labviewset(ModelViewSet):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('department',)
    authentication_classes = ()
    permission_classes = ()

class Deviceviewset(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('lab',)
    authentication_classes = ()
    permission_classes = ()

    def get_serializer_class(self):
        if self.action == 'publish_message':
            return MqttSerializer
        else:
            return DeviceSerializer

    @action(methods=['POST'], detail=False)
    def publish_message(self, request):
        serializer = MqttSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        topic= serializer.data.get('topic')
        payload = serializer.data.get('payload')

        request_for_publish(topic, payload)
        return Response(data={"message": "payload has been sent."}, status=status.HTTP_200_OK)


class UserTypeView(ViewSet):
    permission_classes = ()
    authentication_classes = ()

    def list(self,request,format=None):
        return Response(data=dict((id,user_type) for id,user_type in USER_TYPE),status=status.HTTP_200_OK)


class InvitationViewSet(ModelViewSet):
    permission_classes = ()
    authentication_classes = ()
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
