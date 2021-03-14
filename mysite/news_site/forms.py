from django import forms
from .modules.Paeser import main as Pars
from .models import News

class ContactForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ["timestamp", ]