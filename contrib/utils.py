from django.contrib.auth import get_user_model


def unique_username(user):
    """Generate a unique username based on first and last name."""
    base_username = f"{user.first_name}_{user.last_name}".lower().replace(" ", "_")
    username = base_username
    UserModel = get_user_model()
    counter = 1
    while UserModel.objects.filter(username=username).exists():
        counter += 1
        username = f"{base_username}_{counter}"
    return username
