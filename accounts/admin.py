from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from . forms import CustomUserCreationForm,  CustomUserChangeForm

# Register your models here.
CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    """ Extend the built-in UserAdmin using this class. """
    
    # Used to construct a new CustomUser
    add_form = CustomUserCreationForm   
    form = CustomUserChangeForm
    model = CustomUser
    # List Display are based on the documentation
    list_display = [
        "email",
        "username",
        "date_joined",
        "is_superuser"
    ]

admin.site.register(CustomUser, CustomUserAdmin)