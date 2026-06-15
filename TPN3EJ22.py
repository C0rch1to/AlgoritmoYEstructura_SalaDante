# Clase Personaje MCU

class PersonajeMCU:
    def __init__(self, nombre, superheroe, genero):
        self.nombre = nombre
        self.superheroe = superheroe
        self.genero = genero

    def __str__(self):
        return f"Personaje: {self.nombre} | Superhéroe: {self.superheroe} | Género: {self.genero}"

# TDA Cola

class Cola:
    def __init__(self):
        self.datos = []

    def arribo(self, dato):
        self.datos.append(dato)

    def atencion(self):
        if not self.cola_vacia():
            return self.datos.pop(0)

    def cola_vacia(self):
        return len(self.datos) == 0



# FUNCIONES

# Devuelve el nombre real a partir del alias
def buscar_personaje_por_superheroe(cola, alias):
    cola_aux = Cola()
    resultado = None

    while not cola.cola_vacia():
        personaje = cola.atencion()

        if personaje.superheroe.lower() == alias.lower():
            resultado = personaje.nombre

        cola_aux.arribo(personaje)

    while not cola_aux.cola_vacia():
        cola.arribo(cola_aux.atencion())

    return resultado


# Devuelve el alias a partir del nombre real
def buscar_superheroe_por_personaje(cola, nombre):
    cola_aux = Cola()
    resultado = None

    while not cola.cola_vacia():
        personaje = cola.atencion()

        if personaje.nombre.lower() == nombre.lower():
            resultado = personaje.superheroe

        cola_aux.arribo(personaje)

    while not cola_aux.cola_vacia():
        cola.arribo(cola_aux.atencion())

    return resultado


# INCISO B
def mostrar_superheroes_femeninos(cola):
    cola_aux = Cola()

    while not cola.cola_vacia():
        personaje = cola.atencion()

        if personaje.genero == "F":
            print(personaje.superheroe)

        cola_aux.arribo(personaje)

    while not cola_aux.cola_vacia():
        cola.arribo(cola_aux.atencion())


# INCISO C
def mostrar_personajes_masculinos(cola):
    cola_aux = Cola()

    while not cola.cola_vacia():
        personaje = cola.atencion()

        if personaje.genero == "M":
            print(personaje.nombre)

        cola_aux.arribo(personaje)

    while not cola_aux.cola_vacia():
        cola.arribo(cola_aux.atencion())


# INCISO E
def mostrar_nombres_con_s(cola):
    cola_aux = Cola()

    while not cola.cola_vacia():
        personaje = cola.atencion()

        if (personaje.nombre.upper().startswith("S")
                or personaje.superheroe.upper().startswith("S")):
            print(personaje)

        cola_aux.arribo(personaje)

    while not cola_aux.cola_vacia():
        cola.arribo(cola_aux.atencion())


# CARGA DE DATOS
cola_mcu = Cola()

cola_mcu.arribo(PersonajeMCU(
    "Tony Stark", "Iron Man", "M"
))

cola_mcu.arribo(PersonajeMCU(
    "Steve Rogers", "Capitán América", "M"
))

cola_mcu.arribo(PersonajeMCU(
    "Natasha Romanoff", "Black Widow", "F"
))

cola_mcu.arribo(PersonajeMCU(
    "Carol Danvers", "Capitana Marvel", "F"
))

cola_mcu.arribo(PersonajeMCU(
    "Scott Lang", "Ant-Man", "M"
))

cola_mcu.arribo(PersonajeMCU(
    "Wanda Maximoff", "Scarlet Witch", "F"
))


# INCISO A
print("Punto A)")
print(
    buscar_personaje_por_superheroe(
        cola_mcu,
        "Capitana Marvel"
    )
)

# INCISO B
print("\nPunto B)")
mostrar_superheroes_femeninos(cola_mcu)

# INCISO C

print("\nPunto C)")
mostrar_personajes_masculinos(cola_mcu)

# INCISO D

print("\nPunto D)")
print(
    buscar_superheroe_por_personaje(
        cola_mcu,
        "Scott Lang"
    )
)

# INCISO E

print("\nPunto E)")
mostrar_nombres_con_s(cola_mcu)

# ==========================================
# INCISO F
# ==========================================

print("\nPunto F)")

alias = buscar_superheroe_por_personaje(
    cola_mcu,
    "Carol Danvers"
)

if alias is not None:
    print("Carol Danvers se encuentra en la cola.")
    print("Superhéroe:", alias)
else:
    print("Carol Danvers no se encuentra en la cola.")