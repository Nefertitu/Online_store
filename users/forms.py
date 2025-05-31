from django.contrib.auth.forms import UserCreationForm

from catalog.forms import StyleFormMixin
from .models import User


class CustomUserCreationForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


