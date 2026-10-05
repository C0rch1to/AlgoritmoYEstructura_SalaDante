from typing import Tuple
from ArbolBinario import ArbolBinario, Nodo

# ==============================================================================
# RESOLUCIÓN TRABAJO PRÁCTICO N° 5 - EJERCICIO 5
# Superhéroes y Villanos del Universo Cinematográfico de Marvel (MCU)
# ==============================================================================


def cargar_datos_iniciales(arbol: ArbolBinario) -> None:
    """
    Carga el árbol inicial con superhéroes y villanos del MCU.
    Nota para el punto e: 'Doctor Strange' se inserta deliberadamente con un error
    tipográfico ('Doctor Strannge') para demostrar la corrección mediante búsqueda por proximidad.
    """
    personajes = [
        # (Nombre, es_heroe: True para héroe, False para villano)
        ("Iron Man", True),
        ("Capitán América", True),
        ("Captain Marvel", True),
        ("Thor", True),
        ("Hulk", True),
        ("Black Widow", True),
        ("Hawkeye", True),
        ("Spider-Man", True),
        ("Ant-Man", True),
        ("Black Panther", True),
        ("Doctor Strannge", True),  # Mal cargado a propósito según consigna 'e'
        ("Wanda Maximoff", True),
        ("Vision", True),
        ("Falcon", True),
        ("Winter Soldier", True),
        ("Colossus", True),
        ("Thanos", False),
        ("Loki", False),
        ("Ultron", False),
        ("Hela", False),
        ("Red Skull", False),
        ("Dormammu", False),
        ("Killmonger", False),
        ("Mysterio", False),
        ("Vulture", False),
        ("Ronan", False),
        ("Gorr", False),
        ("Kang", False),
    ]

    for nombre, es_heroe in personajes:
        arbol.insertar(nombre, es_heroe)


# ==============================================================================
# FUNCIONES PARA CADA ACTIVIDAD DE LA CONSIGNA
# ==============================================================================

def listar_villanos_alfabeticamente(arbol: ArbolBinario) -> None:
    """
    Punto b: Listar los villanos ordenados alfabéticamente.
    El recorrido inorden sobre un árbol de búsqueda binario visita los nodos en
    orden alfabético creciente. Filtramos aquellos con es_heroe == False.
    """
    print("\n--- [b] Listado de Villanos Ordenados Alfabéticamente ---")
    encontrados = False
    for nodo in arbol.barrido_inorden():
        if not nodo.es_heroe:
            print(f"  • {nodo.nombre}")
            encontrados = True
    if not encontrados:
        print("  (No hay villanos en el árbol)")


def mostrar_superheroes_con_c(arbol: ArbolBinario, prefijo: str = "C") -> None:
    """
    Punto c: Mostrar todos los superhéroes que empiezan con C.
    """
    print(f"\n--- [c] Superhéroes cuyo nombre empieza con '{prefijo}' ---")
    encontrados = False
    for nodo in arbol.barrido_inorden():
        if nodo.es_heroe and nodo.nombre.upper().startswith(prefijo.upper()):
            print(f"  • {nodo.nombre}")
            encontrados = True
    if not encontrados:
        print(f"  (No se encontraron superhéroes que inicien con '{prefijo}')")


def determinar_cantidad_superheroes(arbol: ArbolBinario) -> int:
    """
    Punto d: Determinar cuántos superhéroes hay en el árbol.
    """
    total_heroes = arbol.contar_superheroes()
    print(f"\n--- [d] Cantidad Total de Superhéroes en el Árbol ---")
    print(f"  Total de superhéroes: {total_heroes}")
    return total_heroes


def corregir_doctor_strange(arbol: ArbolBinario) -> None:
    """
    Punto e: Doctor Strange en realidad está mal cargado.
    Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre.
    """
    print("\n--- [e] Corrección de 'Doctor Strange' por Búsqueda por Proximidad ---")
    criterio = "stran"  # Búsqueda por proximidad para tolerar el error tipográfico
    coincidencias = arbol.busqueda_proximidad(criterio)

    print(f"Buscando por proximidad con patrón '{criterio}'...")
    if not coincidencias:
        print("  No se encontró ninguna coincidencia.")
        return

    for nodo_erroneo in coincidencias:
        nombre_viejo = nodo_erroneo.nombre
        nombre_correcto = "Doctor Strange"
        print(f"  Coincidencia encontrada: '{nombre_viejo}' (Héroe: {nodo_erroneo.es_heroe})")
        
        # Modificamos el nombre extrayendo y reinsertando para conservar el orden del ABB
        exito = arbol.modificar_nombre(nombre_viejo, nombre_correcto)
        if exito:
            print(f"  -> Nombre corregido exitosamente: '{nombre_viejo}' -> '{nombre_correcto}'")
        else:
            print(f"  -> Error al intentar corregir '{nombre_viejo}'")


def listar_superheroes_descendente(arbol: ArbolBinario) -> None:
    """
    Punto f: Listar los superhéroes ordenados de manera descendente (Z a A).
    Se realiza un barrido inorden inverso (subárbol derecho, nodo, subárbol izquierdo).
    """
    print("\n--- [f] Listado de Superhéroes Ordenados de Forma Descendente (Z-A) ---")
    encontrados = False
    for nodo in arbol.barrido_descendente():
        if nodo.es_heroe:
            print(f"  • {nodo.nombre}")
            encontrados = True
    if not encontrados:
        print("  (No hay superhéroes en el árbol)")


def generar_bosque(arbol_origen: ArbolBinario) -> Tuple[ArbolBinario, ArbolBinario]:
    """
    Punto g: Generar un bosque a partir de este árbol:
      - Un árbol debe contener a los superhéroes.
      - Otro árbol a los villanos.
    Luego resuelve:
      I. Determinar cuántos nodos tiene cada árbol.
      II. Realizar un barrido ordenado alfabéticamente de cada árbol.
    """
    print("\n--- [g] Generación de Bosque (Árbol de Héroes y Árbol de Villanos) ---")
    arbol_heroes = ArbolBinario()
    arbol_villanos = ArbolBinario()

    # Recorremos el árbol original y distribuimos los nodos
    for nodo in arbol_origen.barrido_inorden():
        if nodo.es_heroe:
            arbol_heroes.insertar(nodo.nombre, True)
        else:
            arbol_villanos.insertar(nodo.nombre, False)

    # g.I: Cantidad de nodos de cada árbol
    total_h = arbol_heroes.contar_nodos()
    total_v = arbol_villanos.contar_nodos()
    print(f"[g.I] Cantidad de nodos en el Árbol de Superhéroes: {total_h}")
    print(f"[g.I] Cantidad de nodos en el Árbol de Villanos:    {total_v}")

    # g.II: Barrido ordenado alfabéticamente de cada árbol
    print("\n[g.II] Barrido alfabético del Árbol de Superhéroes:")
    for nodo in arbol_heroes.barrido_inorden():
        print(f"  • {nodo.nombre}")

    print("\n[g.II] Barrido alfabético del Árbol de Villanos:")
    for nodo in arbol_villanos.barrido_inorden():
        print(f"  • {nodo.nombre}")

    return arbol_heroes, arbol_villanos


# ==============================================================================
# PROGRAMA PRINCIPAL
# ==============================================================================

def main():
    print("=" * 70)
    print("  TP N° 5 - EJERCICIO 5: ÁRBOLES BINARIOS (SUPERHÉROES Y VILLANOS MCU)")
    print("=" * 70)

    arbol_mcu = ArbolBinario()
    cargar_datos_iniciales(arbol_mcu)
    print(f"Árbol cargado inicialmente con {arbol_mcu.contar_nodos()} personajes.")

    # Punto b: Listar villanos alfabéticamente
    listar_villanos_alfabeticamente(arbol_mcu)

    # Punto c: Mostrar superhéroes que empiezan con C
    mostrar_superheroes_con_c(arbol_mcu, prefijo="C")

    # Punto d: Determinar cuántos superhéroes hay en el árbol
    determinar_cantidad_superheroes(arbol_mcu)

    # Punto e: Búsqueda por proximidad y corrección de Doctor Strange
    corregir_doctor_strange(arbol_mcu)

    # Punto f: Listar superhéroes ordenados descendentemente
    listar_superheroes_descendente(arbol_mcu)

    # Punto g: Generar bosque y resolver incisos I y II
    generar_bosque(arbol_mcu)

    print("\n" + "=" * 70)
    print("  EJECUCIÓN DEL EJERCICIO 5 COMPLETADA CON ÉXITO")
    print("=" * 70)


if __name__ == "__main__":
    main()
