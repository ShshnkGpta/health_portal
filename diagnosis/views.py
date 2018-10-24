from django.shortcuts import render
from django.views.generic import CreateView

#
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Retina
from . import forms
#from . import retina-form


# Create your views here.

def diagnosis(request):
    return render(request,'diagnosis/disease.html')

"""class NewRetina(CreateView):
    model = Retina
    fields = ['retina_scan']
    template_name = 'diagnosis/disease.html'
"""

def retina_form_view(request):

    form = forms.RetinaForm()

    if request.method == "POST":
        retina_form = forms.RetinaForm(request.POST)
    
        if form.is_valid():
            #form.save(commit = True)
            print('Successfully submited')
        else:
            print("Error!")
        
    return render(request,'diagnonis/diabetes.html', {'form':retina_form})

def test(request):

    form = RetinaForm2()

    if request.method == 'POST':
        form = RetinaForm2(request.POST)

        if form.is_valid():
            form.save(commit = True)
            print('Successfully submited')
        else:
            print("Error!")
    return render(request,'diagnosis/diabetes.html',{'form':form})
