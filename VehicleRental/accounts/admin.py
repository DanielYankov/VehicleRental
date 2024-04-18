from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from VehicleRental.accounts.forms import UserEditForm, UserCreateForm
# Register your models here.

UserModel = get_user_model()
@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", "gender", "currency")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    form = UserEditForm
    add_form = UserCreateForm