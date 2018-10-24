from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

# TEMPLATE URLS!
app_name = 'diagnosis'

urlpatterns = [
    url('diseases/',
        views.diagnosis,
        name='diagnosis'),

    url('diabetes/',
        views.retina_form_view,
        name='diabetes'),
]
