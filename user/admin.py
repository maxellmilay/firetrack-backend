from django.contrib import admin
from .models import User, Squad, Firestation
from django.contrib.auth.admin import UserAdmin

# Register the User model
admin.site.register(User, UserAdmin)
admin.site.register(Squad)
admin.site.register(Firestation)
