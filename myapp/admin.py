from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Register

admin.site.register(Register, UserAdmin)