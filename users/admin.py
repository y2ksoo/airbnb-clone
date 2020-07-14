from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import mark_safe
from . import models
from rooms import models as room_models

# class CustomUserAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(models.User, CustomUserAdmin)
# "same as below"


class RoomInlineAdmin(admin.TabularInline):
    model = room_models.Room


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    inlines = (RoomInlineAdmin,)

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

    def get_thumbnail(self, obj):
        # print(obj.avatar.)
        # return
        return mark_safe(f'<img width="50px", src="{obj.avatar.url}" />')

    get_thumbnail.short_description = "Thumbnail"
