from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from sh_app.managers import CalculationManager


class Calculation(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    sum_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CalculationManager()

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
