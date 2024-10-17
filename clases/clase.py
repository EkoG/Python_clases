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

# list comprehension
# 
lista = [numero**2 for numero in range(1, 11)]
diccionario_1 = {"a":"b", "c":"m", "Estudiante:":"Celia"} # No tienen un orden (indice) definido
diccionario = (f'{key}  {value}' for key, value in diccionario_1.items())
print(diccionario_1.items()) # lista de tuplas -> 
print(diccionario_1.values()) # lista de tuplas -> 
print(diccionario_1.keys()) # lista de tuplas 
nombre = 'Jorge'
print(f'hola cómo estas {nombre}')
print(diccionario)

quejas = "NO_ME_LLAMES" # -> "No Me Llames"
quejas = quejas.split("_")
print(quejas)
quejas = [queja.lower() for queja in quejas]
print(quejas)
quejas = [queja.capitalize() for queja in quejas]
print(quejas)
quejas = " ".join(quejas)
print(quejas)
# ------ Duplicado compacto
quejas = "NO_ME_LLAMES" # -> "No Me Llames"
quejas = quejas.split("_")
quejas = " ".join([queja.lower().capitalize() for queja in quejas])
print(quejas)

## Operaciones bool

# hint: 
# True == 1
# False == 0 == (a veces) None 

print(1 == True) # true
print(0 == False) # true
print(True !=  0) # true
print( 1 <= 0)
print( 1 >= 0)

# if elif else. ----- switch case
lista = ["a", "b"]
if lista: #len(lista) > 0: #comparacion
    print (lista)
elif 'a' in lista:
    print(f'esta lista contiene a {" ".join(lista)}')

else:
    print("lista vacia")

## -----------------------------------------------------

if not lista: # si NO hay elementos en mi lista == len(lista) <= 0
    print("lista vacia")
elif 'a' in lista:
    print(f'esta lista contiene {"*+ ".join(lista)}') # [a, b, c] -> a*+ b*+ c

# packaging/unpackaging
#.         x  y  z      0.  1
lista = [(0, 15, 30), # (0, 15)
        (-1, 30, None),
        (-3, 55, -200),
        (-5, 48, 80)]
# lista[0] = (0, 21)
# matrices
# esto es x del primer elemento
print(f"esto es la x del elemento inicial de mi tupla {str(lista[0][0])}")
print(f"esto es la y del elemento inicial de mi tupla {str(lista[0][1])}")
print(f"esto es la x del elemento segundo de mi tupla {str(lista[1][0])}")
print(f"esto es la y del elemento segundo de mi tupla {str(lista[1][1])}")

#   0   - >        4 - 1
for i in range(len(lista)):         #. [(), (), (), ()]
    print("x", "y")                     
#    print(f'x = {str(lista[i][0])}, y = {str(lista[0][0][1])}, z ={str(lista[i][0][1])}')


# range(4) ->      for i in 0,1,2,3:
# iteracion 1 -> i = 0 posicion 0 de la lista
# iteracion 2 -> i = 1 posicion 1 de la lista
# ... 

for x, y, z in lista: # Para cada elemento x, y  en lista imprime x= valor, y = valor
    print(f'x = {str(x)},  y = {str(y)}, z = {str(z)}')

# regex expressions ->  f'string {variable}'
# import re
# *


# Extraccion transformacion y cargo(load)

# Unpackaging arguments 

def numbers (*args): # *args -> (a, 33102990, c, d, )
    token = args[0]
    numero_telefono =  args[1]
    return sum([number for number in args])

#  ---
def add(numero_1: int, numero_2: int):
    return numero_1 + numero_2

nums = [2, 3]
#       0.  1
#
# [{},{},{},{},{[]:{},}]
# print(add(nums[0], nums[1]))
print(add(*nums)) # add((nums[0], nums[1])) tupla

x, y = nums # Toma el primer valor de lista y asignalo a x. Toma el segundo valor de nums y asignalo a Y
print(add(x, y))



nums_2 = (3, 3) # tupla
print(add(*nums_2))


numero_x, numero_y = nums_2 # desempaquetar

print(add(numero_x, numero_y))
# otra forma





nums_dict = {"x": 5, "y": 6}
# print(add(**nums_dict))

# Unpackaging key arguments

def named(**kwargs):
    print(kwargs)

# print(named(name="lorenzo", age="mateo"))
# try, error 


# decoradores
