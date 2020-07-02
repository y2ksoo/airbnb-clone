from django.contrib import admin
from . import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom User Admin """

    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = (
        "language",
        "currency",
        "superhost",
    )


# class CustomUserAdmin(admin.ModelAdmin):
#     pass


# admin.site.register(models.User, CustomUserAdmin)
