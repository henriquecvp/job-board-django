from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Aditional Info',
            {
                'fields':(
                    'company',
                )
            }
        )
    )

admin.site.register(CustomUser, CustomAdmin)