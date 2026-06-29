from super_heroes_data import superheroes
from collections import deque

# 1. Listado ordenado por nombre
print("1) Personajes ordenados por nombre")
ordenados_nombre = sorted(superheroes, key=lambda x: x["name"])
for personaje in ordenados_nombre:
    print(personaje["name"])

# 2. Posición de "The Thing" y "Rocket Raccoon"
print("\n2) Posiciones")
for i, personaje in enumerate(ordenados_nombre):
    if personaje["name"] == "The Thing":
        print("The Thing está en la posición:", i)
    elif personaje["name"] == "Rocket Raccoon":
        print("Rocket Raccoon está en la posición:", i)

# 3. Listar todos los villanos
print("\n3) Villanos")
for personaje in superheroes:
    if personaje["is_villain"]:
        print(personaje["name"])

# 4. Cola de villanos aparecidos antes de 1980
print("\n4) Villanos aparecidos antes de 1980")
cola_villanos = deque()

for personaje in superheroes:
    if personaje["is_villain"]:
        cola_villanos.append(personaje)

while cola_villanos:
    villano = cola_villanos.popleft()
    if villano["first_appearance"] < 1980:
        print(villano["name"], "-", villano["first_appearance"])

# 5. Superhéroes que comienzan con Bl, G, My y W
print("\n5) Superhéroes que comienzan con Bl, G, My y W")

prefijos = ("Bl", "G", "My", "W")

for personaje in superheroes:
    if (not personaje["is_villain"] and
        personaje["name"].startswith(prefijos)):
        print(personaje["name"])

# 6. Ordenados por nombre real
print("\n6) Ordenados por nombre real")

ordenados_real = sorted(
    superheroes,
    key=lambda x: x["real_name"] if x["real_name"] else ""
)

for personaje in ordenados_real:
    print(personaje["real_name"], "-", personaje["name"])

# 7. Superhéroes ordenados por fecha de aparición
print("\n7) Superhéroes ordenados por fecha de aparición")

heroes = [p for p in superheroes if not p["is_villain"]]
heroes = sorted(heroes, key=lambda x: x["first_appearance"])

for personaje in heroes:
    print(personaje["first_appearance"], "-", personaje["name"])

# 8. Cambiar nombre real de Ant Man
print("\n8) Modificación de Ant Man: ")

for personaje in superheroes:
    if personaje["name"] == "Ant Man":
        personaje["real_name"] = "Scott Lang"
        print(personaje["name"], "ahora es ", personaje["real_name"])

# 9. Biografía contiene "time-traveling" o "suit"
print("\n9) Personajes con 'time-traveling' o 'suit'")

for personaje in superheroes:
    bio = personaje["short_bio"].lower()
    if "time-traveling" in bio or "suit" in bio:
        print(personaje["name"])

# 10. Eliminar Electro y Baron Zemo
print("\n10) Eliminar Electro y Baron Zemo: ")

eliminar = ["Electro", "Baron Zemo"]

for nombre in eliminar:
    for personaje in superheroes[:]:
        if personaje["name"] == nombre:
            print("Eliminado:")
            print(personaje["name"], "-", personaje["real_name"])
            superheroes.remove(personaje)