from django import forms
from .models import ContactForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
        labels = {
            'customer_email': 'Correo Electrónico',
            'customer_name': 'Nombre',
            'message': 'Mensaje',
        }
        widgets = {
            'customer_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre Completo'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu mensaje aquí...', 'rows': 3}),
        }
        


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }