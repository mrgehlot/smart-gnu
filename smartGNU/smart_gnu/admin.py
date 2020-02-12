from django.contrib import admin
from django.conf import settings
from .models import User,Devices,Department, University
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','profile_image']

    def username(self,obj):
        return obj.user.username

class UniversityAdmin(admin.ModelAdmin):
    list_display = ['id','university_name']

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','department_name']

class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id','device_name','topic','message','department']

admin.site.register(User, UserAdmin)
admin.site.register(Devices,DeviceAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(University,UniversityAdmin)