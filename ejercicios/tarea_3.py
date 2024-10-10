# EJERCICIO COMPRENDER
lista = [1, 3, 4, 6, 7, "ga", "m"] 
# indice 0
lenght = len(lista)
for i in range(lenght // 2): # 5 // 2 -> 2 range(2)- > 0 1 # 146, 147
    lista[i], lista[lenght - 1 - i] = lista[lenght - 1 - i], lista[i] # 158 SWAP
print(lista)