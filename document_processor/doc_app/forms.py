from django import forms
from .models import Document
from django import forms
from django.core.cache import cache

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('uploaded_file',)
