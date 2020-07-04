from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        #fields = UserCreationForm.Meta.fields + ('custom_field',)


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        #fields = UserChangeForm.Meta.fields + ('custom_field',)


# class CustomUserSignupForm(CustomUserCreationForm):

#     class Meta(CustomUserCreationForm.Meta):
#         fields = ['username', 'email', 'password1', 'password2']
