from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True, label="Full Name")

    class Meta:
        model = User
        fields = ['full_name', 'username', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    pass

class CustomPasswordResetForm(PasswordResetForm):
    pass
