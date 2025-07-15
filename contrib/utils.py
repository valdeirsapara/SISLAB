from django.contrib.auth import get_user_model


def unique_username(user):
    """
    Gera um username único baseado no primeiro e último nome do usuário.
    
    Args:
        user: Instância do modelo User
        
    Returns:
        str: Username único gerado
    """
    base_username = f"{user.first_name}_{user.last_name}".lower().replace(" ", "_")
    username = base_username
    UserModel = get_user_model()
    counter = 1
    while UserModel.objects.filter(username=username).exists():
        counter += 1
        username = f"{base_username}_{counter}"
    return username
