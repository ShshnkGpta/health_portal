from django.shortcuts import render
from django.views.generic import CreateView

#
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Retina
#from . import retina-form


# Create your views here.
def diabetes(request):

    form = NewRetinaForm()

    if request.method == "POST":
        form = NewRetinaForm(request.POST)
    
        if form.is_valid():
            form.save(commit = True)
            print('Successfully submited')
        else:
            print("Error!")
        
    return render(request,'diagnonis/diabetes.html')

class Diagnosis(CreateView):
    template_name = 'diagnosis/disease.html'

class NewRetina(CreateView):
    model = Retina
    fields = ['retina_scan']