"""
Serviços para lógica de negócio do sistema de laboratórios.
"""
from django.db import transaction
from django.contrib.auth import get_user_model
from contrib.models import Perfil
from contrib.utils import unique_username

User = get_user_model()


class UserRegistrationService:
    """Serviço para registro de usuários."""
    
    @staticmethod
    def create_user_with_profile(user_data, perfil_data):
        """
        Cria um usuário com perfil associado.
        
        Args:
            user_data (dict): Dados do usuário
            perfil_data (dict): Dados do perfil
            
        Returns:
            tuple: (user, perfil) criados
            
        Raises:
            Exception: Se houver erro na criação
        """
        with transaction.atomic():
            # Criar usuário
            user = User.objects.create_user(
                email=user_data['email'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                password=user_data['password']
            )
            user.username = unique_username(user)
            user.save()
            
            # Criar perfil
            perfil = Perfil.objects.create(
                user=user,
                matricula=perfil_data['matricula'],
                data_nascimento=perfil_data.get('data_nascimento'),
                sexo=perfil_data['sexo']
            )
            
            return user, perfil


class LaboratoryService:
    """Serviço para lógica de negócio dos laboratórios."""
    
    @staticmethod
    def get_available_laboratories():
        """Retorna laboratórios disponíveis."""
        from laboratory.models import Laboratory
        return Laboratory.objects.filter(
            ativo=True, 
            status=Laboratory.DISPONIVEL
        )
    
    @staticmethod
    def get_active_laboratories():
        """Retorna todos os laboratórios ativos."""
        from laboratory.models import Laboratory
        return Laboratory.objects.filter(ativo=True)