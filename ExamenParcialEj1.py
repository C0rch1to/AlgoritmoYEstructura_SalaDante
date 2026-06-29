# Lista de 15 superhéroes
superheroes = [
    "Iron Man",
    "Thor",
    "Hulk",
    "Black Widow",
    "Hawkeye",
    "Capitan America",
    "Spider-Man",
    "Doctor Strange",
    "Black Panther",
    "Ant-Man",
    "Wasp",
    "Captain Marvel",
    "Scarlet Witch",
    "Vision",
    "Falcon"
]

# Función recursiva para buscar a Capitan America
def buscar_capitan(lista, indice=0):
    # Caso base: se llegó al final de la lista
    if indice == len(lista):
        return False

    # Si se encontró
    if lista[indice] == "Capitan America":
        return True

    # Llamada recursiva
    return buscar_capitan(lista, indice + 1)


# Función recursiva para listar los superhéroes
def listar_superheroes(lista, indice=0):
    # Caso base
    if indice == len(lista):
        return

    print(lista[indice])

    # Llamada recursiva
    listar_superheroes(lista, indice + 1)


# Programa Principal
print("Lista de superhéroes:")
listar_superheroes(superheroes)

print()

if buscar_capitan(superheroes):
    print("Capitan America está en la lista.")
else:
    print("Capitan America no está en la lista.")