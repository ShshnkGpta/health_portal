from django import forms
from diagnosis.models import Retina

class RetinaForm(forms.Form):
    retina_scan = forms.FileField()
    exclude = []

class RetinaForm2(forms.ModelForm):
    class Meta:
        model = Retina
        exclude = []