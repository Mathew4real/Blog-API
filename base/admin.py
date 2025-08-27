from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class CustumUserAdmin(UserAdmin):
    list_display = ("username","first_name","last_name")
admin.site.register(User,CustumUserAdmin)
admin.site.register(Blog)