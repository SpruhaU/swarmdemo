from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    # Additional fields or customizations
    remember_me = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        help_text="Remember Me"
    )
    
    custom_input = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text="Custom Input"
    )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'email_verified', 'checkbox1', 'checkbox2', 'checkbox3', 'checkbox4']
