from django.contrib import admin
from .models import User, Squad, Firestation
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

class CustomUserAdmin(DefaultUserAdmin):
    # Add custom fields to the list display
    list_display = ('username', 'email', 'first_name', 'last_name', 'display_name', 'role', 'tracker_id', 'squad')
    
    # Add custom fields to the fieldsets
    fieldsets = DefaultUserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('display_name', 'avatar_url', 'role', 'tracker_id', 'squad')}),
    )
    
    # Add custom fields to the add_fieldsets
    add_fieldsets = DefaultUserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('display_name', 'avatar_url', 'role', 'tracker_id', 'squad')}),
    )

# Register the models
admin.site.register(User, CustomUserAdmin)
admin.site.register(Squad)
admin.site.register(Firestation)
