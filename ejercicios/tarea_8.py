from functools import wraps

# Definir el decorador
def remove_duplicates_decorator(func):
    @wraps(func)
    def wrapper(*args):
        # Procesar los argumentos para eliminar duplicados en listas o tuplas
        sin_duplicados = []
        for arg in args:
            pass
            # Aquí va el codigo para eliminar duplicados

        return func(*sin_duplicados)
    return wrapper

# Ejemplo de uso del decorador
@remove_duplicates_decorator
def process_data(data):
    return data

# Pruebas
print(process_data([1, 2, 2, 3, 4, 4, 5]))  # Debería imprimir [1, 2, 3, 4, 5]
print(process_data((1, 2, 2, 3, 4, 4, 5)))  # Debería imprimir (1, 2, 3, 4, 5)