from .models import Whatsapp
from django import forms


class WhatForm(forms.ModelForm):
    class Meta:
        model = Whatsapp
        fields = ('__all__')