from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from user import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None,{'fields':('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields':('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Importat dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields' : ('email', 'name', 'password', 'password2')
        }),
    )

@admin.register(models.UserData)
class UserData(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['user', 'steps', 'calories', 'points']

#@admin.register(models.UserData)
class UserLeaderBoardAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id',  'points', 'get_name']
    def get_name(self, obj):
        return obj.user.name
    get_name.short_description = 'Name'
    get_name.admin_order_field = 'user'

admin.site.register(models.User, UserAdmin)
# admin.site.register(models.UserData, UserLeaderBoardAdmin)