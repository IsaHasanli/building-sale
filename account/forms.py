from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django import forms

User=get_user_model()
def validate_email(value):
    if User.objects.filter(email = value).exists():
        raise ValidationError(
            (f"{value} is taken."),
            params = {'value':value}
        )
User = get_user_model()
class RegisterForm(UserCreationForm):
    email = forms.EmailField(validators = [validate_email])
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        