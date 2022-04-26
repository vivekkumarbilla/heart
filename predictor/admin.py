from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import HeartData,DoctorHospital
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class HeartDataAdmin(admin.ModelAdmin):
    list_display=['title','age','probability']
    list_filter = ['probability','date','owner']
    def has_change_permission(self, request, obj=None):
        return False
    def title(self, obj):
        return format_html(f'<div>{obj.owner.first_name if obj.owner.first_name else obj.owner.username} {obj.owner.last_name if obj.owner.last_name else None}</div>')

admin.site.register(HeartData, HeartDataAdmin)

admin.site.register(DoctorHospital)
admin.site.unregister(Group)
admin.site.unregister(User)
class NewUserAdmin(UserAdmin):
    #def has_change_permission(self, request, obj=None):
        #return False  
    exclude = ['']

admin.site.register(User, NewUserAdmin)