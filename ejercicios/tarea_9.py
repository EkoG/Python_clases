def count_word_occurrences(word_list: list) -> dict:
    result = dict()
    for fruit in word_list:
        if fruit in result:
            #
            result[fruit] += 1
        else:
            result[fruit] = 1
    return result


# Ejemplo de uso
input_list = ["apple", "apple", "orange", "banana", "apple"]
output_dict = count_word_occurrences(input_list)
print(output_dict)  # Debería imprimir {"apple": 3, "banana": 2, "orange": 1}

# apple -> {'apple': 1}
# apple -> {'apple' : 2 } 1 + 1 
# orange -> {'orange': 1}
# apple - {'apple': 3 } 2 + 1
# acceder a la llave cosa
print(output_dict.get('cosa')) # util 
# print(output_dict['cosa'])
print(output_dict.get('apple'))
# print(output_dict.get('apple') + 1)
output_dict['apple'] = output_dict.get('apple') + 1
print(output_dict.get('apple'))

# utiliza el metodo get para reescribir la función de arriba

