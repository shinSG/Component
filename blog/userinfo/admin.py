from django.contrib import admin
from userinfo.models import Userinfo
# Register your models here.

class userinfoadmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_email', 'user_staff', 'user_active']


    def user_name(self, obj):
        return u'%s' % obj.user.name
    def user_email(self, obj):
        return u'%s' % obj.user.email

    def user_staff(self, obj):
        return u'%s' % obj.user.is_staff

    def user_active(self, obj):
        return u'%s' % obj.user.is_active


admin.site.register(Userinfo,userinfoadmin)