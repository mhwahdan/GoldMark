from django.contrib import admin
from users.models import User, Client, Agent
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.forms import USERAdminCreationForm, USERAdminChangeForm
from users.models import Favorite

# Register your models here.


class UserAdmin(BaseUserAdmin):
    form = USERAdminChangeForm
    add_form = USERAdminCreationForm
    list_display = [
        'username',
        'email'
    ]
    list_filter = [
        'is_admin'
    ]
    fieldsets = (
        ('authentication', {
            'fields': [
                'username',
                'email'
            ]
        }
         ),
        ('Personal info', {
            'fields': [
                'firstname',
                'lastname',
                'phone',
                'image'
            ]
        }
         ),
        ('Permissions', {
            'fields': [
                'is_active',
                'is_staff',
                'is_admin'
            ]
        }
         ),
    )
    add_fieldsets = (
        (None, {
            'classes': [
                'wide'
            ],
            'fields': [
                'username',
                'firstname',
                'lastname',
                'email',
                'phone',
                'image'
                'password',
                'confirm_password'
            ]
        }
         ),
    )
    search_fields = [
        'email',
        'username',
        'phone'
    ]
    ordering = [
        'username'
    ]
    filter_horizontal = ()


class ClientDetailsInline(admin.TabularInline):
    model = Favorite


class ClientAdmin(admin.ModelAdmin):
    inlines = [ClientDetailsInline]


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Agent)

