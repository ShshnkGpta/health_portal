from django.db import models
from django.contrib import auth
from django.urls import reverse

# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

class Retina(models.Model):
    retina_scan = models.FileField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_absolute_url(self):
        return reverse("retina:detail", kwargs={"pk": self.pk})
    