from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(max_length=50,label='Nombre')
    last_name = forms.CharField(max_length=50, label='Apellido')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(RegistroUsuarioForm,self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Usuario'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar Contraseña'