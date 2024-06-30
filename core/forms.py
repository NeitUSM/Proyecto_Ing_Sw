from django import forms

class FiltroGratuidadForm(forms.Form):
    gratuidad = forms.BooleanField(label='Gratuidad', required=False)
