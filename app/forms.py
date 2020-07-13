from django import forms
from app.models import LogMessage
from app.models import AuthenticatorStorage

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",) # NOTE: the trailing comma is required

class AuthenticatorGenerationForm(forms.ModelForm):
    class Meta:
        model = AuthenticatorStorage
        fields = ("authenticator",) # NOTE: the trailing comma is required