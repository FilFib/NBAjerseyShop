from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Address


admin.site.register(Address)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display[1:]
    ordering = ('email',)
    fieldsets = ()
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'first_name',
                    'last_name',
                    'password1',
                    'password2',
                ),
            },
        ),
    )


# @admin.register(User)
