from django import forms
from diagnosis.models import Retina

class RetinaForm(forms.ModelForm):
    class Meta:
        model = Retina
        exclude = []