from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class CustumUserAdmin(UserAdmin):
    list_display = ("id","username","first_name","last_name","last_name","profile_pic","bio","facebook","linkedin","instagram","github","instagram")
admin.site.register(User,CustumUserAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_draft","category","created")
admin.site.register(Blog,BlogAdmin)