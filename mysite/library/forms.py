from .models import Uzduotis
from django import forms
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = 'date'

class UserUzduotisCreateForm(forms.ModelForm):
    class Meta:
        model = Uzduotis
        fields = ['uzduoties_tekstas', 'vartotojas', 'data']
        widgets = {'vartotojas': forms.HiddenInput(), 'data': DateInput()}