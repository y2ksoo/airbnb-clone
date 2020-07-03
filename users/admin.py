from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# class CustomUserAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(models.User, CustomUserAdmin)
# "same as below"


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "superhost",
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
