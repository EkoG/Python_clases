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

None
Nan



