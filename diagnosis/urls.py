from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

# TEMPLATE URLS!
app_name = 'diagnosis'

urlpatterns = [
    url('',
        views.diagnosis,
        name='diagnosis'),

    url('diabetes/',
        views.retina_form_view,
        name='diabetes'),

    url('lala/',
        views.lala,
        name='lala'),

    url('test/',
        views.test,
        name='test')
]
