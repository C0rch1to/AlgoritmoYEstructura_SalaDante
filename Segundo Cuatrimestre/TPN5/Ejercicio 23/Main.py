from typing import List, Dict 
from collections import Counter
from ArbolBinario import ArbolBinarioCriaturas

# ==============================================================================
# RESOLUCIÓN TRABAJO PRÁCTICO N° 5 - EJERCICIO 23
# Criaturas Mitológicas Griegas (Basado en Tabla.png)
# ==============================================================================

# Datos extraídos fielmente de Tabla.png
TABLA_CRIATURAS = [
    # Columna 1 y 2
    ("Ceto", None),
    ("Tifón", "Zeus"),
    ("Equidna", "Argos Panoptes"),
    ("Dino", None),
    ("Pefredo", None),
    ("Enio", None),
    ("Escila", None),
    ("Caribdis", None),
    ("Euríale", None),
    ("Esteno", None),
    ("Medusa", "Perseo"),
    ("Ladón", "Heracles"),
    ("Águila del Cáucaso", None),
    ("Quimera", "Belerofonte"),
    ("Hidra de Lerna", "Heracles"),
    ("León de Nemea", "Heracles"),
    ("Esfinge", "Edipo"),
    ("Dragón de la Cólquida", None),
    ("Cerbero", None),
    # Columna 3 y 4
    ("Cerda de Cromión", "Teseo"),
    ("Ortro", "Heracles"),
    ("Toro de Creta", "Teseo"),
    ("Jabalí de Calidón", "Atalanta"),
    ("Carcinos", None),
    ("Gerión", "Heracles"),
    ("Cloto", None),
    ("Láquesis", None),
    ("Átropos", None),
    ("Minotauro de Creta", "Teseo"),
    ("Harpías", None),
    ("Argos Panoptes", "Hermes"),
    ("Aves del Estínfalo", None),
    ("Talos", "Medea"),
    ("Sirenas", None),
    ("Pitón", "Apolo"),
    ("Cierva de Cerinea", None),
    ("Basilisco", None),
    ("Jabalí de Erimanto", None),
]

# Descripciones iniciales para enriquecer el árbol (Punto b)
DESCRIPCIONES_INICIALES = {
    "Talos": "Autómata gigante de bronce forjado por Hefesto para proteger la isla de Creta.",
    "Medusa": "Gorgona con serpientes por cabellos capaz de petrificar con su mirada.",
    "Cerbero": "Perro de múltiples cabezas que custodia la entrada al inframundo griego.",
    "Hidra de Lerna": "Monstruo serpentino policéfalo que regeneraba cabezas al ser cortadas.",
    "Minotauro de Creta": "Monstruo con cuerpo de hombre y cabeza de toro que habitaba en el laberinto.",
    "Quimera": "Criatura mitológica que escupía fuego con partes de león, cabra y serpiente.",
    "Ladón": "Dragón de cien cabezas que custodiaba las manzanas de oro del jardín de las Hespérides.",
    "León de Nemea": "Monstruo con piel impenetrable derrotado por Heracles en su primer trabajo.",
}


def cargar_arbol_desde_tabla(arbol: ArbolBinarioCriaturas) -> None:
    """Carga inicial del árbol binario con todos los registros de Tabla.png."""
    for nombre, derrotado_por in TABLA_CRIATURAS:
        desc = DESCRIPCIONES_INICIALES.get(nombre)
        arbol.insertar(nombre=nombre, derrotado_por=derrotado_por, capturada=None, descripcion=desc)


# ==============================================================================
# FUNCIONES PARA CADA ACTIVIDAD DE LA CONSIGNA
# ==============================================================================

def punto_a_listado_inorden(arbol: ArbolBinarioCriaturas) -> None:
    """
    Punto a: Listado inorden de las criaturas y quiénes las derrotaron.
    """
    print("\n" + "=" * 75)
    print("--- [a] Listado Inorden de Criaturas y sus Derrotadores ---")
    print("=" * 75)
    for nodo in arbol.barrido_inorden():
        derrotador = nodo.derrotado_por if nodo.derrotado_por else "No fue derrotada (-)"
        print(f"  • {nodo.nombre:<24} | Derrotado por: {derrotador}")


def punto_b_cargar_descripcion(arbol: ArbolBinarioCriaturas, nombre: str, descripcion: str) -> None:
    """
    Punto b: Se debe permitir cargar una breve descripción sobre cada criatura.
    """
    nodo = arbol.buscar(nombre)
    if nodo:
        nodo.descripcion = descripcion
        print(f"[b] Descripción asignada/actualizada con éxito para '{nombre}':\n    -> \"{descripcion}\"")
    else:
        print(f"[b] Criatura '{nombre}' no encontrada en el árbol.")


def punto_c_mostrar_informacion_talos(arbol: ArbolBinarioCriaturas) -> None:
    """
    Punto c: Mostrar toda la información de la criatura Talos.
    """
    print("\n--- [c] Información Completa de la Criatura Talos ---")
    nodo = arbol.buscar("Talos")
    if nodo:
        print(f"  Nombre:         {nodo.nombre}")
        print(f"  Derrotado por:  {nodo.derrotado_por if nodo.derrotado_por else 'Nadie'}")
        print(f"  Capturada por:  {nodo.capturada if nodo.capturada else 'No fue capturada'}")
        print(f"  Descripción:    {nodo.descripcion if nodo.descripcion else 'Sin descripción'}")
    else:
        print("  La criatura Talos no se encuentra en el árbol.")


def punto_d_top_3_derrotadores(arbol: ArbolBinarioCriaturas) -> None:
    """
    Punto d: Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas.
    """
    print("\n--- [d] Top 3 Héroes o Dioses que Derrotaron Mayor Cantidad de Criaturas ---")
    conteo_victorias: Dict[str, int] = Counter()

    for nodo in arbol.barrido_inorden():
        if nodo.derrotado_por and nodo.derrotado_por.strip() and nodo.derrotado_por != "-":
            # Si contiene detalles adicionales (como en el punto k), tomamos el nombre base del héroe
            heroe = nodo.derrotado_por.split("(")[0].strip()
            conteo_victorias[heroe] += 1

    top_3 = conteo_victorias.most_common(3)
    puesto = 1
    for heroe, victorias in top_3:
        print(f"  {puesto}°. {heroe:<18} -> {victorias} criatura(s) derrotada(s)")
        puesto += 1


def punto_e_criaturas_derrotadas_por_heracles(arbol: ArbolBinarioCriaturas) -> None:
    """
    Punto e: Listar las criaturas derrotadas por Heracles.
    """
    print("\n--- [e] Criaturas Derrotadas por Heracles ---")
    encontrados = False
    for nodo in arbol.barrido_inorden():
        if nodo.derrotado_por and "Heracles" in nodo.derrotado_por:
            print(f"  • {nodo.nombre}")
            encontrados = True
    if not encontrados:
        print("  (Ninguna criatura derrotada por Heracles)")


def punto_f_criaturas_no_derrotadas(arbol: ArbolBinarioCriaturas) -> None:
    """
    Punto f: Listar las criaturas que no han sido derrotadas.
    """
    print("\n--- [f] Criaturas que NO Han Sido Derrotadas ---")
    total = 0
    for nodo in arbol.barrido_inorden():
        if not nodo.derrotado_por or nodo.derrotado_por.strip() in ("", "-"):
            print(f"  • {nodo.nombre}")
            total += 1
    print(f"  Total no derrotadas: {total}")


def punto_h_modificar_atrapadas_por_heracles(arbol: ArbolBinarioCriaturas) -> None:
    """
    Punto h: Modifique los nodos de las criaturas Cerbero, Toro de Creta,
    Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó.
    (Utiliza el campo 'capturada' requerido en la consigna 'g').
    """
    print("\n--- [h] Registrando Captura por Heracles (Cerbero, Toro de Creta, Cierva Cerinea, Jabalí de Erimanto) ---")
    objetivos = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Cierva Cerinea", "Jabalí de Erimanto"]
    actualizadas = set()

    for objetivo in objetivos:
        nodo = arbol.buscar(objetivo)
        if not nodo and objetivo == "Cierva Cerinea":
            nodo = arbol.buscar("Cierva de Cerinea")
        if nodo and nodo.nombre not in actualizadas:
            nodo.capturada = "Heracles"
            actualizadas.add(nodo.nombre)
            print(f"  -> {nodo.nombre}: campo 'capturada' actualizado a 'Heracles'")


def punto_i_busqueda_por_coincidencia(arbol: ArbolBinarioCriaturas, criterio: str) -> None:
    """
    Punto i: Se debe permitir búsquedas por coincidencia.
    """
    print(f"\n--- [i] Búsqueda por Coincidencia (Término: '{criterio}') ---")
    coincidencias = arbol.busqueda_coincidencia(criterio)
    if coincidencias:
        for nodo in coincidencias:
            derrotador = nodo.derrotado_por if nodo.derrotado_por else "-"
            capturador = f" | Capturada por: {nodo.capturada}" if nodo.capturada else ""
            print(f"  • {nodo.nombre} (Derrotado por: {derrotador}{capturador})")
    else:
        print(f"  No se encontraron coincidencias para '{criterio}'.")


def punto_j_eliminar_basilisco_y_sirenas(arbol: ArbolBinarioCriaturas) -> None:
    """
    Punto j: Eliminar al Basilisco y a las Sirenas.
    """
    print("\n--- [j] Eliminación de 'Basilisco' y 'Sirenas' del Árbol ---")
    for nombre in ["Basilisco", "Sirenas"]:
        eliminado = arbol.eliminar(nombre)
        if eliminado:
            print(f"  -> Criatura '{eliminado.nombre}' eliminada con éxito.")
        else:
            print(f"  -> No se encontró a '{nombre}' para eliminar.")


def punto_k_modificar_aves_del_estinfalo(arbol: ArbolBinarioCriaturas) -> None:
    """
    Punto k: Modificar el nodo que contiene a las Aves del Estínfalo,
    agregando que Heracles derrotó a varias.
    """
    print("\n--- [k] Modificando Aves del Estínfalo ---")
    nodo = arbol.buscar("Aves del Estínfalo")
    if nodo:
        nodo.derrotado_por = "Heracles (derrotó a varias)"
        descripcion_extra = "Heracles logró espantarlas con crótalos de bronce y abatió a varias con flechas."
        if nodo.descripcion:
            nodo.descripcion += " " + descripcion_extra
        else:
            nodo.descripcion = descripcion_extra
        print("  -> Nodo 'Aves del Estínfalo' modificado:")
        print(f"     Derrotado por: {nodo.derrotado_por}")
        print(f"     Descripción:   {nodo.descripcion}")
    else:
        print("  No se encontró el nodo 'Aves del Estínfalo'.")


def punto_l_modificar_nombre_ladon(arbol: ArbolBinarioCriaturas) -> None:
    """
    Punto l: Modifique el nombre de la criatura Ladón por Dragón Ladón.
    Para no corromper la propiedad del ABB, se extrae el nodo y se reubica.
    """
    print("\n--- [l] Modificando el nombre de 'Ladón' a 'Dragón Ladón' ---")
    exito = arbol.modificar_nombre("Ladón", "Dragón Ladón")
    if exito:
        print("  -> Nombre modificado exitosamente: 'Ladón' -> 'Dragón Ladón' (árbol reorganizado)")
    else:
        print("  -> No se encontró la criatura 'Ladón'.")


def punto_m_listado_por_nivel(arbol: ArbolBinarioCriaturas) -> None:
    """
    Punto m: Realizar un listado por nivel del árbol (BFS).
    """
    print("\n" + "=" * 75)
    print("--- [m] Listado por Nivel del Árbol (Recorrido en Anchura - BFS) ---")
    print("=" * 75)
    nivel_actual = -1
    linea_nodos: List[str] = []

    for nivel, nodo in arbol.barrido_por_nivel():
        if nivel != nivel_actual:
            if linea_nodos:
                print(f"Nivel {nivel_actual:02d}: " + " | ".join(linea_nodos))
            nivel_actual = nivel
            linea_nodos = [nodo.nombre]
        else:
            linea_nodos.append(nodo.nombre)

    if linea_nodos:
        print(f"Nivel {nivel_actual:02d}: " + " | ".join(linea_nodos))


def punto_n_criaturas_capturadas_por_heracles(arbol: ArbolBinarioCriaturas) -> None:
    """
    Punto n: Muestre las criaturas capturadas por Heracles.
    """
    print("\n--- [n] Criaturas Capturadas por Heracles ---")
    encontradas = False
    for nodo in arbol.barrido_inorden():
        if nodo.capturada and "Heracles" in nodo.capturada:
            print(f"  • {nodo.nombre}")
            encontradas = True
    if not encontradas:
        print("  (Ninguna criatura capturada por Heracles)")


# ==============================================================================
# PROGRAMA PRINCIPAL
# ==============================================================================

def main():
    print("=" * 75)
    print("  TP N° 5 - EJERCICIO 23: CRIATURAS MITOLÓGICAS GRIEGAS")
    print("=" * 75)

    arbol_criaturas = ArbolBinarioCriaturas()
    cargar_arbol_desde_tabla(arbol_criaturas)
    print(f"Árbol cargado inicialmente con {arbol_criaturas.contar_nodos()} criaturas de Tabla.png.\n")

    # a. Listado inorden
    punto_a_listado_inorden(arbol_criaturas)

    # b. Permitir cargar descripción
    print("\n--- [b] Carga de Descripción Demostrativa ---")
    punto_b_cargar_descripcion(
        arbol_criaturas,
        "Pitón",
        "Gran serpiente que habitaba en el santuario de Delfos, muerta por las flechas de Apolo."
    )

    # c. Mostrar información de Talos
    punto_c_mostrar_informacion_talos(arbol_criaturas)

    # d. Determinar los 3 héroes o dioses que derrotaron mayor cantidad
    punto_d_top_3_derrotadores(arbol_criaturas)

    # e. Criaturas derrotadas por Heracles
    punto_e_criaturas_derrotadas_por_heracles(arbol_criaturas)

    # f. Criaturas que no han sido derrotadas
    punto_f_criaturas_no_derrotadas(arbol_criaturas)

    # g y h. Modificar capturas por Heracles
    punto_h_modificar_atrapadas_por_heracles(arbol_criaturas)

    # i. Búsquedas por coincidencia
    punto_i_busqueda_por_coincidencia(arbol_criaturas, "Creta")
    punto_i_busqueda_por_coincidencia(arbol_criaturas, "Jabalí")

    # j. Eliminar Basilisco y Sirenas
    punto_j_eliminar_basilisco_y_sirenas(arbol_criaturas)

    # k. Modificar Aves del Estínfalo
    punto_k_modificar_aves_del_estinfalo(arbol_criaturas)

    # l. Modificar Ladón por Dragón Ladón
    punto_l_modificar_nombre_ladon(arbol_criaturas)

    # m. Listado por nivel del árbol
    punto_m_listado_por_nivel(arbol_criaturas)

    # n. Mostrar criaturas capturadas por Heracles
    punto_n_criaturas_capturadas_por_heracles(arbol_criaturas)

    print("\n" + "=" * 75)
    print("  EJECUCIÓN DEL EJERCICIO 23 COMPLETADA CON ÉXITO")
    print("=" * 75)


if __name__ == "__main__":
    main()
