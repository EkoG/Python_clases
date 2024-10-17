# crear una funcion que reciba, una lista de elementos y sumar cada elemento y devolver la suma total

# hint: necesitas for
def sumar(*args):
    # inserte codigo aquí
    pass

nums = [1, 2, 3]
nums_2 = [2, 3, 5]
print(sumar(*nums))
print(sumar(*nums_2))

assert sumar(*nums) == 6
assert sumar(*nums_2) == 10

# crear una funcion que reciba, una lista de elementos y restar cada elemento y devolver la resta total

# hint: necesitas for
def restar(*args):
    # inserte codigo aquí
    pass

nums_restar = [1, -2, 3]
nums_2_restar = [2, 3, -5]
print(restar(*nums_restar))
print(restar(*nums_2_restar))

assert restar(*nums_restar) == -4
assert restar(*nums_2_restar) == -5

# crear una clase llamada calculadora con los metodos sumar, restar, multiplicar y utilizar los metodos para 
# hacer operaciones arismeticas

class Calculadora:
    pass

calculo_1 = Calculadora()
print(calculo_1.suma(*nums))
assert calculo_1.suma(*nums) == 6
print(calculo_1.restar.restar(*nums_restar))
assert calculo_1.restar(*nums_restar) == -4
print(calculo_1.multiplicar(*nums))
assert calculo_1.multiplicar(*nums) == 6

# Bonus, Imprimir el objeto calculadora y obtener el siguiente mensaje

mensaje = "Hola soy una clase calculadora y estoy aquí para hacer operaciones arismeticas"

#hint utiliza dunder methods