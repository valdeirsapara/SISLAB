from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from contrib.models import Perfil

User = get_user_model()


class LoginForm(AuthenticationForm):
    """Form personalizado para login por email."""
    username = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Seu email'
        })
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Sua senha'
        })
    )


class UserRegistrationForm(forms.ModelForm):
    """Form para registro de usuários."""
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Sua senha'
        }),
        min_length=8
    )
    password_confirm = forms.CharField(
        label='Confirmar Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirme sua senha'
        })
    )
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Primeiro nome'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Último nome'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu email'
            })
        }
    
    def clean_email(self):
        """Valida se o email não está em uso."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email já está sendo usado.')
        return email
    
    def clean(self):
        """Valida se as senhas coincidem."""
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('As senhas não coincidem.')
        
        return cleaned_data


class PerfilForm(forms.ModelForm):
    """Form para dados do perfil do usuário."""
    
    class Meta:
        model = Perfil
        fields = ['matricula', 'data_nascimento', 'sexo']
        widgets = {
            'matricula': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sua matrícula'
            }),
            'data_nascimento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'sexo': forms.Select(attrs={
                'class': 'form-control'
            })
        }
    
    def clean_matricula(self):
        """Valida se a matrícula não está em uso."""
        matricula = self.cleaned_data.get('matricula')
        if matricula and Perfil.objects.filter(matricula=matricula).exists():
            raise forms.ValidationError('Esta matrícula já está sendo usada.')
        return matricula