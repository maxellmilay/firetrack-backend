from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register the User model
admin.site.register(User, UserAdmin)
