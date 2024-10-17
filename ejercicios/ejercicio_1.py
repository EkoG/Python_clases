# crear una funcion que reciba, una lista de elementos y multiplicar cada elemento y devolver su vañor

# hint: necesitas for
def multiplicar(*args):
    # inserte codigo aquí
    pass

nums = [1, 2, 3]
nums_2 = [2, 3, 5]
print(multiplicar(*nums))
print(multiplicar(*nums_2))

assert multiplicar(*nums) == 6
assert multiplicar(*nums_2) == 30
