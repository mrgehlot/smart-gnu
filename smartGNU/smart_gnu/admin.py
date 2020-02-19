from django.contrib import admin
from django.conf import settings
from .models import CollegeUser,Device,Department, College,Lab
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','profile_image']

    def username(self,obj):
        return obj.user.username

class CollegeAdmin(admin.ModelAdmin):
    list_display = ['id','college_name']

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','department_name', 'college']

class LabAdmin(admin.ModelAdmin):
    list_display = ['id','lab_number', 'department']

class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id','device_name','topic','message','lab']
    # readonly_fields = ['topic']
admin.site.register(CollegeUser, UserAdmin)
admin.site.register(College,CollegeAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Lab,LabAdmin)
admin.site.register(Device,DeviceAdmin)
