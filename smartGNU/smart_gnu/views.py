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
                        InvitationSerializer, \
                        NodeMCUCreateSerializer, \
                        NodeMCUSerializer,\
                        DeviceUpdateSerializer,\
                        QrCodeSerializer
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

    def get_serializer_class(self):
        if self.action == "check_qr_code":
            return QrCodeSerializer
        return LabSerializer

    @action(methods=["POST"],detail=False)
    def check_qr_code(self,request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception= True)
        if self.queryset.filter(id = request.data.get('lab_id'),qr_code = request.data.get('qr_code')).exists():
            return Response({'flag': True}, status=200)
        return Response({'flag': False}, status=401)

class Deviceviewset(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('node_mcu__lab',)
    authentication_classes = ()
    permission_classes = ()

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return DeviceUpdateSerializer
        else:
            return DeviceSerializer

    def partial_update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        topic = serializer.data.get('topic')
        payload = serializer.data.get('payload')
        message = int(serializer.data.get('message'))
        if message == 1:
            payload['switch'] = "True"
        else:
            payload['switch'] = "False"
        published, error = request_for_publish(topic, payload)
        if not published:
            return Response(data={error}, status=status.HTTP_400_BAD_REQUEST)
        Device.objects.filter(id=kwargs.get('pk')).update(message=message)
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

class NodeMCUViewSet(ModelViewSet):
    queryset = NodeMCU.objects.all()
    serializer_class = NodeMCUSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('lab',)
    permission_classes = ()
    authentication_classes = ()

    def get_serializer_class(self):
        if self.action == 'create':
            return NodeMCUCreateSerializer
        return NodeMCUSerializer

    def create(self, request, *args, **kwargs):
        lab_obj = Lab.objects.get(lab_number=request.data.get('lab_number'))
        node_obj,created =NodeMCU.objects.get_or_create(lab = lab_obj,
                        node_mcu_ip = request.data.get('node_mcu_ip'))
        return Response({"message":"device added successfully"},
                        status=status.HTTP_201_CREATED)
