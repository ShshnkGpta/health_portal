from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

# TEMPLATE URLS!
app_name = 'diagnosis'

urlpatterns = [
    url('diabetes/retinopathy',views.NewRetina.as_view(),name='retinopathy'),
]