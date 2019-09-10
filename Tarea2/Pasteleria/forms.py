from django import forms

class loginForm(forms.Form):
    nombre = forms.CharField(label='nombre', max_length=100)
    contraseña = forms.CharField(label='nombre', max_length=100)