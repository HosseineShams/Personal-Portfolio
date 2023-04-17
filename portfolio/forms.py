from django import forms
from .models import Contact
from django.forms import ModelForm

class ContactForm(forms.ModelForm):
    name = forms.CharField(label="Name", max_length=200, required=False)
    email = forms.EmailField(label="Email", required=False)
    class Meta:
        model = Contact
        fields = ['subject', 'message']
