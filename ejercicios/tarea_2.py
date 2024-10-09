# Importar funciones
from utils import agregar_elemento, eliminar_duplicados

# Ejercicios con listas

# Ejercicio 1: Suma de Elementos de una Lista
def sumar_elementos(lista):
    suma = 0
    for numero in lista: #Esto se lee así: "Para cada numero en la lista"
        # Añadir tu codigo aquí
        pass
    return suma

# Prueba la función sumar_elementos
numeros = [1, 2, 3, 4, 5]
print("Suma de elementos:", sumar_elementos(numeros))  # Salida: 15
assert sumar_elementos(numeros) == 15

# Ejercicio 2: Añadir un nuevo elemento en la lista
# Prueba la función encontrar_maximo
numeros = [1, 2, 3, 4, 5]
# numeros.append(6)
numeros = agregar_elemento(numeros, 6)
assert numeros == [1, 2, 3, 4, 5, 6]
numeros = agregar_elemento(numeros, 9)
assert numeros == [1, 2, 3, 4, 5, 6, 9]

strings = ["a", "c", "b", "c", "b", "a"]
strings = agregar_elemento(strings, "d") # se añade "d" a strings
# ejericio Extra

strings_sin_duplicados = eliminar_duplicados(strings)
print(strings_sin_duplicados)



# Ejercicio 3: Eliminar el primer y ultimo elemento de una lista
def eliminar_elementos(lista):
    # Añadir tu codigo
    pass
# Prueba la función eliminar_elementos
numeros = [1, 2, 3, 4, 5]
eliminar_elementos(numeros)
assert numeros == [2, 3, 4]
