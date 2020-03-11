from django.contrib import admin
from django.conf import settings
from .models import CollegeUser,Device,Department, College,Lab
from .mqtt_code import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','profile_image']

    def username(self,obj):
        return obj.user.username

class CollegeAdmin(admin.ModelAdmin):
    list_display = ['id','college_name']

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','department_name', 'college','node_id']

class LabAdmin(admin.ModelAdmin):
    list_display = ['id','lab_number', 'department']

class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id','device_name','topic','message','gpio_pin','node_mcu']
    readonly_fields = ['topic']
class NodeMCUAdmin(admin.ModelAdmin):
    list_display = ['id','lab','node_mcu_ip','node_mcu_name']

admin.site.register(CollegeUser, UserAdmin)
admin.site.register(College,CollegeAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Lab,LabAdmin)
admin.site.register(Device,DeviceAdmin)
admin.site.register(NodeMCU,NodeMCUAdmin)
