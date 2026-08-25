
from collections import deque

from List_ import List
from Superhero import (
    Superhero,
    by_name,
    by_real_name,
    by_year
)
from Superhero_Data import superheroes


# ============================================================
# FUNCIONES DEL EJERCICIO 1
# ============================================================

def buscar_recursivo(lista, buscado, posicion=0):
    """
    Busca recursivamente un elemento dentro de una lista.

    Args:
        lista (list): Lista donde buscar.
        buscado: Elemento que se desea encontrar.
        posicion (int): Posición actual de búsqueda.

    Returns:
        bool: True si encuentra el elemento, False si no.
    """

    # Caso base: se llegó al final de la lista
    if posicion >= len(lista):
        return False

    # Caso base: se encontró el elemento
    if lista[posicion] == buscado:
        return True

    # Llamada recursiva
    return buscar_recursivo(
        lista,
        buscado,
        posicion + 1
    )


def listar_recursivo(lista, posicion=0):
    """
    Lista recursivamente todos los elementos.

    Args:
        lista (list): Lista a recorrer.
        posicion (int): Posición actual.
    """

    # Caso base
    if posicion >= len(lista):
        return

    print(lista[posicion])

    # Llamada recursiva
    listar_recursivo(
        lista,
        posicion + 1
    )


# ============================================================
# EJERCICIO 1
# ============================================================

def ejercicio_1():
    """
    Resuelve el ejercicio 1.
    """

    print("=" * 70)
    print("EJERCICIO 1")
    print("=" * 70)

    # Lista simple de 15 superheroes
    heroes = [
        "Iron Man",
        "Hulk",
        "Thor",
        "Captain America",
        "Black Panther",
        "Spider-Man",
        "Wolverine",
        "Deadpool",
        "Doctor Strange",
        "Ant Man",
        "Hawkeye",
        "Black Widow",
        "Vision",
        "Scarlet Witch",
        "Captain Marvel"
    ]

    # --------------------------------------------------------
    # Buscar Captain America
    # --------------------------------------------------------

    print("\n¿Captain America está en la lista?")

    encontrado = buscar_recursivo(
        heroes,
        "Captain America"
    )

    if encontrado:
        print("Sí, Captain America está en la lista.")
    else:
        print("No, Captain America no está en la lista.")

    # --------------------------------------------------------
    # Listar superheroes
    # --------------------------------------------------------

    print("\nLista de superheroes:")

    listar_recursivo(heroes)


# ============================================================
# CARGA DE LOS PERSONAJES
# ============================================================

def cargar_personajes():
    """
    Carga los personajes de super_heroes_data.py
    dentro de una List.
    """

    lista = List()

    # Agregamos los criterios
    lista.add_criterion("name", by_name)
    lista.add_criterion("real_name", by_real_name)
    lista.add_criterion("year", by_year)

    # Convertimos cada diccionario en un objeto Superhero
    for hero in superheroes:

        personaje = Superhero(
            name=hero["name"],
            alias=hero["alias"],
            real_name=hero["real_name"],
            bio=hero["short_bio"],
            year=hero["first_appearance"],
            is_villain=hero["is_villain"]
        )

        lista.append(personaje)

    return lista


# ============================================================
# EJERCICIO 2 - PUNTO 1
# ============================================================

def ordenar_por_nombre(lista):
    """
    Lista los personajes ordenados por nombre.
    """

    print("\n" + "-" * 70)
    print("1. PERSONAJES ORDENADOS POR NOMBRE")
    print("-" * 70)

    lista.sort_by_criterion("name")

    lista.show()


# ============================================================
# EJERCICIO 2 - PUNTO 2
# ============================================================

def buscar_personajes(lista):
    """
    Determina la posición de The Thing y Rocket Raccoon.
    """

    print("\n" + "-" * 70)
    print("2. POSICIÓN DE THE THING Y ROCKET RACCOON")
    print("-" * 70)

    # The Thing
    posicion = lista.search(
        "The Thing",
        "name"
    )

    if posicion is not None:
        print(
            f"The Thing está en la posición "
            f"{posicion + 1}."
        )
    else:
        print("The Thing no está en la lista.")

    # Rocket Raccoon
    posicion = lista.search(
        "Rocket Raccoon",
        "name"
    )

    if posicion is not None:
        print(
            f"Rocket Raccoon está en la posición "
            f"{posicion + 1}."
        )
    else:
        print("Rocket Raccoon no está en la lista.")


# ============================================================
# EJERCICIO 2 - PUNTO 3
# ============================================================

def listar_villanos(lista):
    """
    Lista todos los personajes marcados como villanos.
    """

    print("\n" + "-" * 70)
    print("3. TODOS LOS VILLANOS")
    print("-" * 70)

    for hero in lista:

        if hero.is_villain:
            print(hero)


# ============================================================
# EJERCICIO 2 - PUNTO 4
# ============================================================

def cola_villanos(lista):
    """
    Coloca todos los villanos en una cola y determina
    cuáles aparecieron antes de 1980.
    """

    print("\n" + "-" * 70)
    print("4. VILLANOS QUE APARECIERON ANTES DE 1980")
    print("-" * 70)

    cola = deque()

    # Encolamos los villanos
    for hero in lista:

        if hero.is_villain:
            cola.append(hero)

    print(
        f"Villanos agregados a la cola: {len(cola)}"
    )

    print("\nVillanos anteriores a 1980:")

    # Desencolamos respetando FIFO
    while cola:

        villano = cola.popleft()

        if villano.year < 1980:
            print(villano)


# ============================================================
# EJERCICIO 2 - PUNTO 5
# ============================================================

def superheroes_por_prefijo(lista):
    """
    Lista los superheroes cuyos nombres comienzan
    con Bl, G, My o W.
    """

    print("\n" + "-" * 70)
    print("5. SUPERHÉROES QUE COMIENZAN CON Bl, G, My Y W")
    print("-" * 70)

    prefijos = (
        "Bl",
        "G",
        "My",
        "W"
    )

    for hero in lista:

        if (
            not hero.is_villain
            and hero.name.startswith(prefijos)
        ):
            print(hero)


# ============================================================
# EJERCICIO 2 - PUNTO 6
# ============================================================

def ordenar_por_nombre_real(lista):
    """
    Lista los personajes ordenados por nombre real.
    """

    print("\n" + "-" * 70)
    print("6. PERSONAJES ORDENADOS POR NOMBRE REAL")
    print("-" * 70)

    lista.sort_by_criterion("real_name")

    for hero in lista:

        print(
            f"{hero.real_name} -> {hero.name}"
        )


# ============================================================
# EJERCICIO 2 - PUNTO 7
# ============================================================

def ordenar_superheroes_por_fecha(lista):
    """
    Lista los superheroes ordenados por año
    de primera aparición.
    """

    print("\n" + "-" * 70)
    print("7. SUPERHÉROES ORDENADOS POR FECHA DE APARICIÓN")
    print("-" * 70)

    lista.sort_by_criterion("year")

    for hero in lista:

        if not hero.is_villain:
            print(hero)


# ============================================================
# EJERCICIO 2 - PUNTO 8
# ============================================================

def modificar_ant_man(lista):
    """
    Modifica el nombre real de Ant Man a Scott Lang.
    """

    print("\n" + "-" * 70)
    print("8. MODIFICAR NOMBRE REAL DE ANT MAN")
    print("-" * 70)

    posicion = lista.search(
        "Ant Man",
        "name"
    )

    if posicion is not None:

        ant_man = lista[posicion]

        print(
            f"Nombre real anterior: "
            f"{ant_man.real_name}"
        )

        ant_man.real_name = "Scott Lang"

        print(
            f"Nombre real nuevo: "
            f"{ant_man.real_name}"
        )

    else:
        print("Ant Man no está en la lista.")


# ============================================================
# EJERCICIO 2 - PUNTO 9
# ============================================================

def buscar_en_biografias(lista):
    """
    Muestra personajes cuya biografía contiene
    'time-traveling' o 'suit'.
    """

    print("\n" + "-" * 70)
    print(
        '9. BIOGRAFÍAS CON "TIME-TRAVELING" O "SUIT"'
    )
    print("-" * 70)

    palabras = [
        "time-traveling",
        "suit"
    ]

    lista.filter_contain_on_bio(palabras)


# ============================================================
# EJERCICIO 2 - PUNTO 10
# ============================================================

def eliminar_personajes(lista):
    """
    Elimina Electro y Baron Zemo y muestra su información.
    """

    print("\n" + "-" * 70)
    print("10. ELIMINAR ELECTRO Y BARON ZEMO")
    print("-" * 70)

    # --------------------------------------------------------
    # ELECTRO
    # --------------------------------------------------------

    electro = lista.delete_value(
        "Electro",
        "name"
    )

    if electro is not None:

        print("\nElectro fue eliminado.")

        print("\nInformación:")
        print(f"Nombre: {electro.name}")
        print(f"Alias: {electro.alias}")
        print(f"Nombre real: {electro.real_name}")
        print(f"Año: {electro.year}")
        print(f"Villano: {electro.is_villain}")
        print(f"Biografía: {electro.bio}")

    else:
        print("\nElectro no estaba en la lista.")

    # --------------------------------------------------------
    # BARON ZEMO
    # --------------------------------------------------------

    baron_zemo = lista.delete_value(
        "Baron Zemo",
        "name"
    )

    if baron_zemo is not None:

        print("\nBaron Zemo fue eliminado.")

        print("\nInformación:")
        print(f"Nombre: {baron_zemo.name}")
        print(f"Alias: {baron_zemo.alias}")
        print(f"Nombre real: {baron_zemo.real_name}")
        print(f"Año: {baron_zemo.year}")
        print(f"Villano: {baron_zemo.is_villain}")
        print(f"Biografía: {baron_zemo.bio}")

    else:
        print("\nBaron Zemo no estaba en la lista.")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():

    
    # EJERCICIO 1
    

    ejercicio_1()

    
    # Cargar datos del ejercicio 2
    

    lista_heroes = cargar_personajes()

    print("\n\n" + "=" * 70)
    print("EJERCICIO 2")
    print("=" * 70)

    print(
        f"\nCantidad de personajes cargados: "
        f"{lista_heroes.size()}"
    )

    
    # Resolver consignas
    

    ordenar_por_nombre(lista_heroes)

    buscar_personajes(lista_heroes)

    listar_villanos(lista_heroes)

    cola_villanos(lista_heroes)

    superheroes_por_prefijo(lista_heroes)

    ordenar_por_nombre_real(lista_heroes)

    ordenar_superheroes_por_fecha(lista_heroes)

    modificar_ant_man(lista_heroes)

    buscar_en_biografias(lista_heroes)

    eliminar_personajes(lista_heroes)

    
    # Lista final

    print("\n" + "=" * 70)
    print("LISTA FINAL")
    print("=" * 70)

    lista_heroes.sort_by_criterion("name")

    lista_heroes.show()


# ============================================================
# EJECUCIÓN
# ============================================================

if __name__ == "__main__":
    main()

