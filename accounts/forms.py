"""
    A user model can be both created and edited within the Django admin. So we’ll need to update
    the built-in forms too to point to CustomUser instead of User.
"""
# This imports will look for AUTH_USER_MODEl
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )