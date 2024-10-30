from functools import wraps

# Definir el decorador make_secure
def make_secure(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.get('level_access') == 'admin':
            return func(user, *args, **kwargs)
        else:
            raise PermissionError("User does not have admin access")
    return wrapper

# Ejemplo de uso del decorador
@make_secure
def get_admin_panel(user):
    return "Welcome to the admin panel"

# Ejemplo de usuarios
admin_user = {'user': 'name', 'level_access': 'admin'}
regular_user = {'user': 'name', 'level_access': 'user'}

# Pruebas
try:
    print(get_admin_panel(admin_user))  # Debería imprimir "Welcome to the admin panel"
except PermissionError as e:
    print(e)

try:
    print(get_admin_panel(regular_user))  # Debería lanzar una excepción PermissionError
except PermissionError as e:
    print(e)