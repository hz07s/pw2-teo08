from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombres',
            'apellidos',
            'edad',
            'donador'
        ]

class rawPersonaForm(forms.Form):
    nombres = forms.CharField(
        widget= forms.Textarea(
            attrs={
                'placeholder' : 'Solo tu nombre, por favor',
                'id' : 'nombreID',
                'class' : 'special',
                'cols' : '10',
            }
        )
    )
    apellidos = forms.CharField()
    edad = forms.IntegerField(initial=20)
    donador = forms.BooleanField()