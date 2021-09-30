from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class Admin(UserAdmin):
    model = User
    list_display = (
        "username",
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
    )
    list_display_links = ("email",)
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("email", "username")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "password",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                    "is_active",
                ),
            },
        ),
    )
    ordering = ("email",)


admin.site.register(User, Admin)
