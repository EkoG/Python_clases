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

# COMPRENDER