from django import forms
from .models import ContactForm

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