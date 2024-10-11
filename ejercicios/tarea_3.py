# EJERCICIO COMPRENDER
lista = [1, 3, 4, 6, 7, "ga", "m"] 
# indice 0  1  2  3  4   5    6

lenght = len(lista) # -> 7 impar
# Para cada indice quiero que vayas 1 por 1, en el rango de 0 hasta 7//2 = 3 range(0, 3) -> 0, 1, 2
for i in range(lenght // 2): # 5 // 2 -> 2 range(2)- > 0 1 # 146, 147 -> pasos que da for: 0, 1, 2
    lista[i], lista[lenght - 1 - i] = lista[lenght - 1 - i], lista[i] # 158 SWAP
    # paso 1
    # lista[0], lista[6] = lista[6], lista[0]
    # SWAP de valores: 1,"m" = "m",1
    # lista = ["m", 3, 4, 6, 7, "ga", 1]
    # Paso 2
    # lista[1], lista[7 - 1 - 1] = lista[5], lista[1]
    # SWAP de valores: 3, "ga" = "ga", 3
    # lista = ["m", "ga", 4, 6, 7, 3, 1]
    # Paso 3
    # lista[2], lista[7 -1 -2] = lista[4], lista[2]
    # SWAP de valores: 4, 7 = 7, 4
    # lista = ["m", "ga", 7, 6, 4, 3, 1]
print(lista)