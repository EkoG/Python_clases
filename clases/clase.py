# variables
"""
Descripción de las variables más importantes en Python
"""
numero = 1.25
numero_2 = 4.99

numero_3 = numero_2//numero
numero_4 = numero_2/numero

print(numero_3, numero_4)

         # len -> 5
cadena = "Celia"
# No mutable
# print(cadena[5])
        # 0 1 2 3 4 -> n - 1
print(len(cadena))
cadena_nombre_2 = "Iñaki"  #PEP 8
print(cadena + cadena_nombre_2) #Concatenación
cadena = 'j' + cadena[1:len(cadena)] # SPLITING -> : (n - 1)
print(cadena)
        #0. 1. 2
        #-3 -2 -1
print(cadena[0], cadena[len(cadena) - 1], cadena[-1])
# cadenas son NO MUTABLES -> 



                # : 5 - 1 (añadido por python)
string = cadena[1:len(cadena)] #???
print(string)

# CAST
numero = str(9) # -> "9"
print(numero, type(numero)) #Casting
string_numero = int("14")
print(string_numero, type(string_numero))

# listas 

# Python -> Dinamicos 

lista_1 = [1, 2.9, 3, 4, 5, 6, "hola mundo", 8, {"a":1, "b":"c"}, [1,2,3]]
        #   0  1.  2.  3. 4
        # lista_1[-1] Ducker robbin -> len
        # listas (iteradora) -> MUTABLES != Inmutable

print(len(lista_1))

lista_1[0] = set()

#print(lista_1[ : : -1])
# IMPORTANTE
#lista_1.reverse()
l = lista_1
print(l)

# a p 

lista_1.append("0") # añade al final
print(lista_1)
lista_1.pop(-2) # remueva el objeto final 
print(lista_1)

# Diccionarios
# key : value
my_dict = {1:[1,2,3], 2:"string", 3:65, 4:{}} # vacio

diccionario = {}

print(1 in diccionario)
print(diccionario.get(1)) 

# {status:200, data:[1,nombres, llamadas, celurares]} -> json

coches = {"audi":["a1", "a2", "a3"], "Nissan":["staquitas", "tsurus"], "porche":["cayenne"]}
# O(n) time complexity -> [elem       ,i,       entos]
# O(1) inmediato 



# SET 
sett = set() # vacío
set_2 = {1,2,3,4, "hola", 9, "m", 1.3} # Elementos únicos
print(2 in set_2)

lista = [1,2,2,3,5,5,5,6,4,4,5]
        # 1 2 3 4
# casting (convertir una variable a otra)
print(set(lista))
print(sett, {1,})

# None -> 

# None
#  Nan

# Tuple -> Tupla (español)
        # lista inmutable
        # iterador 
        # indexado - 0 
        # primer elemento 0 ultimo elemento len(tupla) - 1
tupla = ()
tupla = tuple()
tupla = (1,) # Pregunta clase par crear tupla de un elemento
print(type(tupla))
tupla_2 = (1, None, "string", tuple(), {1,3,4,5})
print(tupla_2[-1])
print('')
# tupla_2[-1] = 90
# casting
tupla_3 = tuple(lista_1)
lista_4 = list(tupla_3)

# LOOP
# [1, 2, 3]
# Ejercicio 1: Suma de Elementos de una Lista, retorna el total
def sumar_elementos(lista: list) -> int:
    total = 0
    for numero in lista: #Esto se lee así: "Para cada numero en la lista"
        total += numero # total = numero + total
        print(total)
    return total


assert sumar_elementos([1, 3, 5, 9.9, 10.1]) == 29.0
tupla = ("numero", "nombres", "c", "y", "m") # oracion
#        0,        1,         2,    3,  4,  
oracion = ''
for string in tupla:
    oracion += string + ' '   #concatenar
    print(oracion)

lista = [1, 3, 4] # -> 3
# utilizando for para hacerlo de reversa
lista.reverse()
print(lista)
print(lista[::-1])
# for utilizando indices

# range
#                3
print(range(len(lista))) #desde 0 hasta n - 1

for i in range(10):
    print(i)

# Acceder ultimo elemento de una lista
print(lista[-1])
print(lista[0])
lista = [1, 3, 4, 6, 7]
for i in range(len(lista)):
    print("indice: " + str(i), "valor: " + str(lista[i]))

# reverse a través de swap
# definir a y b
# SWAP -> a,b = b,a
a = 1
b = 2
a, b = b, a
print(a, b)

# EJERCICIO COMPRENDER
lista = [1, 3, 4, 6, 7, "ga", "m"] 
# indice 0
lenght = len(lista)
for i in range(lenght // 2): # 5 // 2 -> 2 range(2)- > 0 1 # 146, 147
    lista[i], lista[lenght - 1 - i] = lista[lenght - 1 - i], lista[i] # 158 SWAP
print(lista)

