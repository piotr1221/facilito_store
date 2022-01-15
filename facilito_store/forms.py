from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    #los widgets aplican estilos y atributos a los campos
    username = forms.CharField(
        required=True, min_length=3, max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'username',
            'placeholder': 'Username'
        }))
    email = forms.EmailField(required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'example@gmail.com'
        }))
    password = forms.CharField(required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }))

    password2 = forms.CharField(required=True,
        label='Confirmar Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }))

    # debe comenzar con "clean" para indicar a django que
    # realizara una validacion
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuentra en uso')

        return email

    # validar campos que dependan uno de otro
    def clean(self):
        # regresa los datos del formulario
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'El password no coincide')

    def save(self):
        # password es texto plano, pero create_user lo encripta
        return User.objects.create_user(
                self.cleaned_data.get('username'),
                self.cleaned_data.get('email'),
                self.cleaned_data.get('password'),
            )