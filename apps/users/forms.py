from django.forms import ModelForm, ImageField, Form, CharField, PasswordInput, TextInput

from apps.users.models import User


class UserRegisterForm(ModelForm):
    avatar = ImageField()
    password = CharField(max_length=128, widget=PasswordInput)

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ("avatar", "username", "first_name", "last_name", "email")
        widgets = {'password': PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
                   'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
                   'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
                   'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
                   'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})}


class UserLoginForm(Form):
    username = CharField(max_length=128,
                         widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))
    password = CharField(max_length=128,
                         widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
