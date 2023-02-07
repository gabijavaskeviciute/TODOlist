from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Uzduotis(models.Model):
    uzduoties_tekstas = models.CharField(verbose_name='Uzduoties_tekstas', max_length=200)
    vartotojas = models.ForeignKey(to=User, verbose_name="User", on_delete=models.SET_NULL, null=True, blank=True)
    data = models.DateField(verbose_name='Data', null=True)

    def __str__(self):
        return f"{self.uzduoties_tekstas} ({self.vartotojas})"


    class Meta:
        verbose_name = "Uzduotis"
        verbose_name_plural = "Uzduotys"
