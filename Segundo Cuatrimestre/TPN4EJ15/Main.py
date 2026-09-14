import sys
from Pokemon import Pokemon
from Entrenador import Entrenador
from ListaEnlazada import ListaEnlazada

sys.stdout.reconfigure(encoding='utf-8')

#  FUNCIONES PARA CADA ACTIVIDAD SOLICITADA


def cantidad_pokemones_entrenador(lista: ListaEnlazada, nombre_entrenador: str):
    """Punto a: obtener la cantidad de Pokémons de un determinado entrenador."""
    entrenador = lista.buscar(nombre_entrenador)
    if entrenador:
        print(f"[a] {entrenador.nombre} tiene {entrenador.pokemones.tamanio} Pokémon(s).")
    else:
        print(f"[a] No se encontró al entrenador '{nombre_entrenador}'.")


def entrenadores_mas_de_tres_torneos(lista: ListaEnlazada):
    """Punto b: listar los entrenadores que hayan ganado más de tres torneos."""
    print("[b] Entrenadores con más de 3 torneos ganados:")
    encontrados = False
    for entrenador in lista.barrido():
        if entrenador.torneos_ganados > 3:
            print(f"    - {entrenador.nombre} (Torneos: {entrenador.torneos_ganados})")
            encontrados = True
    if not encontrados:
        print("    (Ninguno)")


def pokemon_mayor_nivel_mejor_entrenador(lista: ListaEnlazada):
    """Punto c: Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados."""
    mejor_entrenador = None
    for entrenador in lista.barrido():
        if mejor_entrenador is None or entrenador.torneos_ganados > mejor_entrenador.torneos_ganados:
            mejor_entrenador = entrenador

    if mejor_entrenador is None:
        print("[c] La lista de entrenadores está vacía.")
        return

    pokemon_mayor = None
    for pokemon in mejor_entrenador.pokemones.barrido():
        if pokemon_mayor is None or pokemon.nivel > pokemon_mayor.nivel:
            pokemon_mayor = pokemon

    if pokemon_mayor:
        print(f"[c] Entrenador con más torneos: {mejor_entrenador.nombre} "
              f"({mejor_entrenador.torneos_ganados} torneos)")
        print(f"    Pokémon de mayor nivel: {pokemon_mayor}")
    else:
        print(f"[c] {mejor_entrenador.nombre} no tiene Pokémons registrados.")


def mostrar_datos_entrenador(lista: ListaEnlazada, nombre_entrenador: str):
    """Punto d: mostrar todos los datos de un entrenador y sus Pokémons."""
    entrenador = lista.buscar(nombre_entrenador)
    if entrenador:
        print(f"[d] {entrenador}")
        print(f"    Pokémons ({entrenador.pokemones.tamanio}):")
        for pokemon in entrenador.pokemones.barrido():
            print(f"      • {pokemon}")
    else:
        print(f"[d] No se encontró al entrenador '{nombre_entrenador}'.")


def entrenadores_porcentaje_batallas(lista: ListaEnlazada, porcentaje_min: float = 79.0):
    """Punto e: entrenadores cuyo porcentaje de batallas ganadas sea mayor al 79 %."""
    print(f"[e] Entrenadores con porcentaje de batallas ganadas > {porcentaje_min}%:")
    encontrados = False
    for entrenador in lista.barrido():
        total_batallas = entrenador.batallas_ganadas + entrenador.batallas_perdidas
        if total_batallas > 0:
            porcentaje = (entrenador.batallas_ganadas / total_batallas) * 100
            if porcentaje > porcentaje_min:
                print(f"    - {entrenador.nombre} ({porcentaje:.1f}%)")
                encontrados = True
    if not encontrados:
        print("    (Ninguno)")


def entrenadores_tipo_fuego_planta_o_agua_volador(lista: ListaEnlazada):
    """Punto f: entrenadores que tengan Pokémons de tipo fuego y planta,
    o de tipo agua y subtipo volador."""
    print("[f] Entrenadores con Pokémons tipo fuego+planta o agua/volador:")
    encontrados = False
    for entrenador in lista.barrido():
        tiene_fuego = False
        tiene_planta = False
        tiene_agua_volador = False

        for pokemon in entrenador.pokemones.barrido():
            tipo = pokemon.tipo.lower()
            subtipo = pokemon.subtipo.lower()

            if tipo == "fuego" or subtipo == "fuego":
                tiene_fuego = True
            if tipo == "planta" or subtipo == "planta":
                tiene_planta = True
            if tipo == "agua" and subtipo == "volador":
                tiene_agua_volador = True

        if (tiene_fuego and tiene_planta) or tiene_agua_volador:
            print(f"    - {entrenador.nombre}")
            encontrados = True
    if not encontrados:
        print("    (Ninguno)")


def promedio_nivel_pokemones(lista: ListaEnlazada, nombre_entrenador: str):
    """Punto g: promedio de nivel de los Pokémons de un determinado entrenador."""
    entrenador = lista.buscar(nombre_entrenador)
    if entrenador is None:
        print(f"[g] No se encontró al entrenador '{nombre_entrenador}'.")
        return

    if entrenador.pokemones.tamanio == 0:
        print(f"[g] {entrenador.nombre} no tiene Pokémons registrados.")
        return

    suma_niveles = 0
    for pokemon in entrenador.pokemones.barrido():
        suma_niveles += pokemon.nivel

    promedio = suma_niveles / entrenador.pokemones.tamanio
    print(f"[g] Promedio de nivel de los Pokémons de {entrenador.nombre}: {promedio:.2f}")


def cuantos_entrenadores_tienen_pokemon(lista: ListaEnlazada, nombre_pokemon: str):
    """Punto h: determinar cuántos entrenadores tienen a un determinado Pokémon."""
    contador = 0
    for entrenador in lista.barrido():
        for pokemon in entrenador.pokemones.barrido():
            if pokemon.nombre.lower() == nombre_pokemon.lower():
                contador += 1
                break  # No contar dos veces si tiene duplicados

    print(f"[h] Cantidad de entrenadores que tienen a '{nombre_pokemon}': {contador}")


def entrenadores_con_pokemones_repetidos(lista: ListaEnlazada):
    """Punto i: mostrar los entrenadores que tienen Pokémons repetidos."""
    print("[i] Entrenadores con Pokémons repetidos:")
    encontrados = False
    for entrenador in lista.barrido():
        nombres_vistos = []
        tiene_repetido = False
        for pokemon in entrenador.pokemones.barrido():
            nombre_lower = pokemon.nombre.lower()
            if nombre_lower in nombres_vistos:
                tiene_repetido = True
                break
            nombres_vistos.append(nombre_lower)

        if tiene_repetido:
            print(f"    - {entrenador.nombre}")
            encontrados = True
    if not encontrados:
        print("    (Ninguno)")


def entrenadores_con_pokemon_especifico(lista: ListaEnlazada,
                                        pokemones_buscados=("Tyrantrum", "Terrakion", "Wingull")):
    """Punto j: entrenadores que tengan uno de los Pokémons: Tyrantrum, Terrakion o Wingull."""
    print(f"[j] Entrenadores que tienen a {', '.join(pokemones_buscados)}:")
    encontrados = False
    buscados_lower = [p.lower() for p in pokemones_buscados]

    for entrenador in lista.barrido():
        tiene_alguno = False
        pokemones_encontrados = []
        for pokemon in entrenador.pokemones.barrido():
            if pokemon.nombre.lower() in buscados_lower:
                tiene_alguno = True
                pokemones_encontrados.append(pokemon.nombre)

        if tiene_alguno:
            print(f"    - {entrenador.nombre} (tiene: {', '.join(pokemones_encontrados)})")
            encontrados = True
    if not encontrados:
        print("    (Ninguno)")


def entrenador_tiene_pokemon(lista: ListaEnlazada, nombre_entrenador: str, nombre_pokemon: str):
    """Punto k: determinar si un entrenador 'X' tiene al Pokémon 'Y'.
    Si lo tiene, muestra los datos de ambos."""
    entrenador = lista.buscar(nombre_entrenador)
    if entrenador is None:
        print(f"[k] No se encontró al entrenador '{nombre_entrenador}'.")
        return

    pokemon_encontrado = None
    for pokemon in entrenador.pokemones.barrido():
        if pokemon.nombre.lower() == nombre_pokemon.lower():
            pokemon_encontrado = pokemon
            break

    if pokemon_encontrado:
        print(f"[k] ¡Sí! {entrenador.nombre} tiene a {pokemon_encontrado.nombre}.")
        print(f"    Datos del entrenador: {entrenador}")
        print(f"    Datos del Pokémon:    {pokemon_encontrado}")
    else:
        print(f"[k] {entrenador.nombre} NO tiene al Pokémon '{nombre_pokemon}'.")


# ═══════════════════════════════════════════════════════════════════════════════
#  CARGA DE DATOS DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════

def cargar_datos():
    """Crea la lista de entrenadores con datos de prueba variados para
    poder verificar todas las actividades del ejercicio."""

    lista_entrenadores = ListaEnlazada()

    # --- Entrenador 1: Ash ---
    ash = Entrenador("Ash", torneos_ganados=5, batallas_perdidas=20, batallas_ganadas=80)
    ash.pokemones.insertar(Pokemon("Pikachu", 100, "eléctrico", "ninguno"))
    ash.pokemones.insertar(Pokemon("Charizard", 90, "fuego", "volador"))
    ash.pokemones.insertar(Pokemon("Bulbasaur", 70, "planta", "veneno"))
    ash.pokemones.insertar(Pokemon("Tyrantrum", 65, "roca", "dragón"))
    ash.pokemones.insertar(Pokemon("Pikachu", 55, "eléctrico", "ninguno"))  # Repetido para punto i
    lista_entrenadores.insertar(ash)

    # --- Entrenador 2: Misty ---
    misty = Entrenador("Misty", torneos_ganados=2, batallas_perdidas=15, batallas_ganadas=35)
    misty.pokemones.insertar(Pokemon("Starmie", 75, "agua", "psíquico"))
    misty.pokemones.insertar(Pokemon("Gyarados", 80, "agua", "volador"))  # agua/volador para punto f
    misty.pokemones.insertar(Pokemon("Wingull", 40, "agua", "volador"))   # Para punto j
    lista_entrenadores.insertar(misty)

    # --- Entrenador 3: Brock ---
    brock = Entrenador("Brock", torneos_ganados=1, batallas_perdidas=25, batallas_ganadas=30)
    brock.pokemones.insertar(Pokemon("Onix", 60, "roca", "tierra"))
    brock.pokemones.insertar(Pokemon("Geodude", 45, "roca", "tierra"))
    lista_entrenadores.insertar(brock)

    # --- Entrenador 4: Cynthia ---
    cynthia = Entrenador("Cynthia", torneos_ganados=8, batallas_perdidas=5, batallas_ganadas=95)
    cynthia.pokemones.insertar(Pokemon("Garchomp", 100, "dragón", "tierra"))
    cynthia.pokemones.insertar(Pokemon("Lucario", 88, "lucha", "acero"))
    cynthia.pokemones.insertar(Pokemon("Roserade", 82, "planta", "veneno"))
    cynthia.pokemones.insertar(Pokemon("Terrakion", 78, "roca", "lucha"))  # Para punto j
    lista_entrenadores.insertar(cynthia)

    # --- Entrenador 5: León ---
    leon = Entrenador("León", torneos_ganados=10, batallas_perdidas=3, batallas_ganadas=97)
    leon.pokemones.insertar(Pokemon("Charizard", 100, "fuego", "volador"))
    leon.pokemones.insertar(Pokemon("Dragapult", 92, "dragón", "fantasma"))
    leon.pokemones.insertar(Pokemon("Rillaboom", 88, "planta", "ninguno"))  # fuego+planta para punto f
    lista_entrenadores.insertar(leon)

    # --- Entrenador 6: Gary ---
    gary = Entrenador("Gary", torneos_ganados=4, batallas_perdidas=30, batallas_ganadas=70)
    gary.pokemones.insertar(Pokemon("Blastoise", 85, "agua", "ninguno"))
    gary.pokemones.insertar(Pokemon("Arcanine", 80, "fuego", "ninguno"))
    gary.pokemones.insertar(Pokemon("Electivire", 78, "eléctrico", "ninguno"))
    gary.pokemones.insertar(Pokemon("Blastoise", 60, "agua", "ninguno"))  # Repetido para punto i
    lista_entrenadores.insertar(gary)

    return lista_entrenadores


# ═══════════════════════════════════════════════════════════════════════════════
#  PROGRAMA PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":

    lista = cargar_datos()

    print(f"{'=' * 60}")
    print(f"  LISTA DE ENTRENADORES POKEMON ({lista.tamanio} cargados)")
    print(f"{'=' * 60}\n")

    # a. Cantidad de Pokémons de un entrenador
    cantidad_pokemones_entrenador(lista, "Ash")
    print()

    # b. Entrenadores con más de 3 torneos ganados
    entrenadores_mas_de_tres_torneos(lista)
    print()

    # c. Pokémon de mayor nivel del entrenador con más torneos
    pokemon_mayor_nivel_mejor_entrenador(lista)
    print()

    # d. Datos completos de un entrenador y sus Pokémons
    mostrar_datos_entrenador(lista, "Cynthia")
    print()

    # e. Entrenadores con porcentaje de batallas ganadas > 79%
    entrenadores_porcentaje_batallas(lista)
    print()

    # f. Entrenadores con Pokémons fuego+planta o agua/volador
    entrenadores_tipo_fuego_planta_o_agua_volador(lista)
    print()

    # g. Promedio de nivel de Pokémons de un entrenador
    promedio_nivel_pokemones(lista, "León")
    print()

    # h. Cuántos entrenadores tienen a un Pokémon determinado
    cuantos_entrenadores_tienen_pokemon(lista, "Charizard")
    print()

    # i. Entrenadores con Pokémons repetidos
    entrenadores_con_pokemones_repetidos(lista)
    print()

    # j. Entrenadores con Tyrantrum, Terrakion o Wingull
    entrenadores_con_pokemon_especifico(lista)
    print()

    # k. ¿El entrenador X tiene al Pokémon Y? (datos ingresados por el usuario)
    print("-" * 60)
    nombre_ent = input("Ingrese el nombre del entrenador: ")
    nombre_pok = input("Ingrese el nombre del Pokémon: ")
    entrenador_tiene_pokemon(lista, nombre_ent, nombre_pok)
