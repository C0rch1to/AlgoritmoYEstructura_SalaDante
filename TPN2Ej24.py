#Ejercicio 24 TP N2
from copy import copy
from typing import Any


class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Any:
        return self.__elements.pop()
    
    def show(self) -> None:
        stack_aux = Stack()
        stack_aux.__elements = copy(self.__elements)

        while stack_aux.size() > 0: 
            value = stack_aux.pop()
            print(value)
            
    def size(self) -> int:
        return len(self.__elements)
    
    def on_top(self) -> Any:
        if self.size() > 0:
            return self.__elements[-1]
        
# Carga de personajes
pila = Stack()

pila.push(("Iron Man", 10))
pila.push(("Captain America", 9))
pila.push(("Groot", 5))
pila.push(("Rocket Raccoon", 6))
pila.push(("Black Widow", 8))
pila.push(("Doctor Strange", 4))
pila.push(("Gamora", 6))
pila.push(("Captain Marvel", 3))

# Resolución
aux = Stack()
DCG = []
posicion = 1
pos_rocket = None
pos_groot = None

print("Personajes en más de 5 películas:\n")

while pila.size() > 0:

    personaje = pila.pop()
    nombre = personaje[0]
    peliculas = personaje[1]

    # Punto a)
    if nombre == "Rocket Raccoon":
        pos_rocket = posicion
    if nombre == "Groot":
        pos_groot = posicion

    # Punto b) y Punto c)
    if peliculas > 5 or nombre == "Black Widow":
        print(nombre, "-", peliculas, "películas")

    
    # Punto d)
    if nombre[0] in ["C", "D", "G"]:
        DCG.append(nombre)

    aux.push(personaje)
    posicion += 1

# Mostrar posiciones
print("\nRocket Raccoon está en la posición:", pos_rocket)
print("Groot está en la posición:", pos_groot)

print("\nPersonajes que comienzan con C, D o G: ")
for i in range (0, len(DCG)):
    print(DCG[i])

# Restaurar pila original
while aux.size() > 0:
    pila.push(aux.pop())