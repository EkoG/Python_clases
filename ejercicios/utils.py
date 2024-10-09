def agregar_elemento(lista: list, elemento: any):
    lista.append(elemento)
    return lista

                    # lista = strings
def eliminar_duplicados(lista: list) -> list:
    # set_a_lista = set(lista)  # eliminando duplicados, convirtiendo a un set
    return list(set(lista)) # devuelvo una lista