from django.contrib import admin
from .models import User, Squad, Firestation
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

class CustomUserAdmin(DefaultUserAdmin):
    # Add custom fields to the list display
    list_display = ('username', 'email', 'first_name', 'last_name', 'display_name', 'role', 'tracker_id')
    
    # Add custom fields to the fieldsets
    fieldsets = DefaultUserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('display_name', 'avatar_url', 'role', 'tracker_id', 'squad')}),
    )
    
    # Add custom fields to the add_fieldsets
    add_fieldsets = DefaultUserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('display_name', 'avatar_url', 'role', 'tracker_id', 'squad')}),
    )
    
    filter_horizontal = ('squad', 'groups', 'user_permissions')

class SquadAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'firestation', 'leader', 'get_members_count')
    list_filter = ('status', 'firestation')
    search_fields = ('name', 'description')
    
    def get_members_count(self, obj):
        return obj.members.count()
    get_members_count.short_description = 'Members Count'
    
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'status', 'firestation', 'leader')
        }),
        ('Members', {
            'fields': ('get_members',),
            'classes': ('collapse',),
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj:  # Only for existing objects
            return readonly_fields + ('get_members',)
        return readonly_fields
    
    def get_members(self, obj):
        members = obj.members.all()
        return ", ".join([user.username for user in members])
    get_members.short_description = 'Members'

# Register the models
admin.site.register(User, CustomUserAdmin)
admin.site.register(Squad, SquadAdmin)
admin.site.register(Firestation)
