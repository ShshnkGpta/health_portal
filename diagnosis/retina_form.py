from django import forms
from diagnosis.models import Retina

class NewRetinaForm(forms.ModelForm):
    class Meta:
        model = Retina
        