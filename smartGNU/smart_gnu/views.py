from rest_framework.viewsets import GenericViewSet,ViewSet,ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import User, University,Department,Devices
from .serializers import UserProfileSerializer,UniversitySerializer,DepartmentSerializer,DevicesSerializer
from rest_framework.authtoken.models import Token
from .mqtt_code import request_for_publish

class smart_gnu_apis(GenericViewSet):
    queryset = User.objects.all()
    authentication_classes = ()
    permission_classes = ()

    @action(methods=['GET'], detail=False)
    def google_signin(self, request):
        google_response = requests.get(url='https://www.googleapis.com/oauth2/v3/userinfo',
                     params={'access_token' : request.GET.get('code')})
        user_profile = google_response.json()
        user_profile.get('email')
        user_obj = User.objects.filter(email = user_profile.get('email')).first()
        if user_obj:
            if not user_obj.profile_image:
                user_obj.profile_image = user_profile.get('picture')
                user_obj.save()
        else:
            User.objects.create(email = user_profile.get('email'),username = user_profile.get('email'),
                                first_name = user_profile.get(''))
        user_data = UserProfileSerializer(user_obj).data
        token_obj, created  = Token.objects.get_or_create(user = user_obj)
        user_data['user_token'] = token_obj.key

        return Response(data={"user": user_data},status=status.HTTP_200_OK)


class mqtt_apis(ViewSet):
    authentication_classes = ()
    permission_classes = ()

    @action(methods=['POST'],detail=False)
    def home(self,request):
        topic = request.POST.get('topic')
        pay_load = request.POST.get('pay_load')
        request_for_publish(topic,pay_load)
        return Response(data={"message": "payload has been sent."}, status=status.HTTP_200_OK)



class universityviewset(ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    authentication_classes = ()
    permission_classes = ()

class departmentviewset(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    authentication_classes = ()
    permission_classes = ()

class devicesviewset(ModelViewSet):
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer
    authentication_classes = ()
    permission_classes = ()