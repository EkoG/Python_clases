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
numero = str(9)
print(numero, type(numero)) #Casting
string_numero = int("14")
print(string_numero, type(string_numero))




# listas 

lista_1 = [1, 2, 3, 4, 5,]

