from django import forms
from django.contrib.auth.models import User
from blog.models import Entry


class UserCreation(forms.Form):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginUser(forms.Form):
    class Meta:
        model = User
        fields = ("username", "password")


class AddEntry(forms.Form):
    class Meta:
        model = Entry
        fields = ("title", "entries")


class EditEntry(forms.Form):
    class Meta:
        model = Entry
        fields = ("title", "entries")
