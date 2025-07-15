from django import forms
from .models import Laboratory


class LaboratoryForm(forms.ModelForm):
    """Form para criar e editar laboratórios."""
    
    class Meta:
        model = Laboratory
        fields = ['nome', 'status']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do laboratório'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            })
        }
        
    def clean_nome(self):
        """Validação do nome do laboratório."""
        nome = self.cleaned_data.get('nome')
        if not nome or len(nome.strip()) < 3:
            raise forms.ValidationError('O nome deve ter pelo menos 3 caracteres.')
        return nome.strip()