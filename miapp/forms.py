from django import forms
from django.core import validators

class FormRegion(forms.Form):
    date = forms.CharField(
        label="Date",
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese Date',
                'class': 'date_form_regiones'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'El codigo es corto'),
            validators.MaxLengthValidator(10,'Superaste el límite de caracteres')
        ]
    )
    name = forms.CharField(
        label="Name",
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese name',
                'class': 'name_form_regiones'
            }
        ),
        validators=[
            validators.MinLengthValidator(2,'El nombre es corto'),
            validators.MaxLengthValidator(20,'Superaste el límite de caracteres')
        ]
    )
    cases = forms.CharField(
        label="Cases",
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese cases',
                'class': 'cases_form_regiones'
            }
        ),
        validators=[
            validators.MinLengthValidator(0,'Ingrese cases valida'),
            validators.MaxLengthValidator(20,'Ingrese cases valida')
        ]
    )

    deaths = forms.CharField(
        label="Deaths",
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese deaths',
                'class': 'deaths_form_regiones'
            }
        ),
        validators=[
            validators.MinLengthValidator(0,'Ingrese deaths validos'),
            validators.MaxLengthValidator(20,'Ingrese deaths validos')
        ]
    )

    opciones_lethality = [
        (1,'Alta'),
        (0,'Baja'),
    ]
    lethality = forms.TypedChoiceField(
        label="Lethality",
        choices=opciones_lethality
    )