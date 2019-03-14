from django import forms
from .models import Grant


class attachmentuploadform(forms.ModelForm):
    class Meta:
        model = Grant
        fields = ('attachment',)
