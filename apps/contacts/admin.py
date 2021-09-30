from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    can_delete = True
    list_display = (
        "id",
        "user",
        "first_name",
        "last_name",
        "phone",
        "country",
        "city",
        "street",
        "building",
        "floor",
        "url",
        "image",
    )
    list_display_links = ("id",)
    search_fields = (
        "first_name",
        "last_name",
        "country",
        "city",
        "street",
        "phone",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "first_name",
                    "last_name",
                    "phone",
                    "country",
                    "city",
                    "street",
                    "building",
                    "floor",
                    "url",
                    "image",
                ),
            },
        ),
    )
    disabled_fields = ("user",)


admin.site.register(Contact, ContactAdmin)
