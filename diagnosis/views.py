from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)

from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from diagnosis.retina_form import NewRetinaForm

def diabetes(request):

    form = NewRetinaForm()

    if request.method == "POST":
        form = NewRetinaForm(request.POST)
    
        if form.is_valid():
            form.save(commit = True)
            print('Successfully submited')
        else:
            print("Error!")
        
    return render(request,'diagno')

class NewRetina(CreateView):
    model = Retina
    fields = ['retina_scan']