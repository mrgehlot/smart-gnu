from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# def user_profile_image(instance,filename):
#     return instance.username

USER_TYPE = (
    (0, 'user'),
    (1, 'Admin'),
    (2, 'Super Admin'),
)

SWITCH = (
    (0, False),
    (1, True),
)

class User(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user_type = models.IntegerField(choices=USER_TYPE, null=True)
    profile_image = models.CharField(max_length=1000, null=True,blank=True)

class University(models.Model):
    university_name = models.CharField(max_length=500, null=True,blank=True)

    def __str__(self):
        return self.university_name

class Department(models.Model):
    department_name = models.CharField(max_length=500, null=True,blank=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return self.department_name

class Devices(models.Model):
    device_name = models.CharField(max_length=500, null=True,blank=True)
    topic = models.CharField(max_length=500, null=True,blank=True)
    message = models.IntegerField(choices=SWITCH,default=0, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return self.device_name
