from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, Profile, LoginHistory

admin.site.register(MyUser, UserAdmin)
admin.site.register(Profile)
admin.site.register(LoginHistory)
