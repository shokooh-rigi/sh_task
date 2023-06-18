from django.db import models
from django.db.models import Sum


class CalculationManager(models.Manager):
    def sum_all(self):
        return self.aggregate(Sum('sum_number'))
