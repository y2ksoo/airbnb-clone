from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "used_by",
    )

    """ item admin definition """

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ photo admin definitino """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="100px", src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        ("Spaces", {"fields": ("beds", "bedrooms", "bath", "guest")}),
        ("Times", {"fields": ("checkin", "checkout", "instant_book")}),
        (
            "More About the Space",
            {"classes": ("collapse",), "fields": ("amenity", "facility", "house_rule")},
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guest",
        "bedrooms",
        "host",
        "room_type",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    ordering = ("name", "price", "bedrooms")

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenity",
        "facility",
        "house_rule",
        "city",
        "country",
    )

    search_fields = ("city", "host__username")

    filter_horizontal = (
        "amenity",
        "facility",
        "house_rule",
    )

    raw_id_fields = ("host",)

    def count_amenities(self, obj):
        return obj.amenity.count()

    count_amenities.short_description = "# of Amenities"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "# of Photos"

