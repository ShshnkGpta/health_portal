from django.db import models
from django.urls import reverse

# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()


class Retina(models.Model):
    retina_scan = models.FileField()

    def get_absolute_url(self):
        return reverse("retina_detail", kwargs={"pk": self.pk})
    