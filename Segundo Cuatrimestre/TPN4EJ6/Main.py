from Superheroe import Superheroe
from ListaEnlazada import ListaEnlazada

# 2. FUNCIONES PARA CADA ACTIVIDAD SOLICITADA

def eliminar_superheroe(lista: ListaEnlazada, nombre: str = "Linterna Verde"):
    """Punto a: Elimina el nodo que contiene la información del superhéroe."""
    eliminado = lista.eliminar(nombre)
    if eliminado:
        print(f"[a] Se eliminó el nodo de: {eliminado.nombre}")
    else:
        print(f"[a] No se encontró a '{nombre}' en la lista.")


def mostrar_anio_aparicion(lista: ListaEnlazada, nombre: str = "Wolverine"):
    """Punto b: Muestra el año de aparición de un superhéroe."""
    heroe = lista.buscar(nombre)
    if heroe:
        print(f"[b] Año de aparición de {heroe.nombre}: {heroe.anio_aparicion}")
    else:
        print(f"[b] '{nombre}' no se encuentra en la lista.")


def modificar_casa_comic(lista: ListaEnlazada, nombre: str = "Dr. Strange", nueva_casa: str = "Marvel"):
    """Punto c: Modifica la casa de cómic de un superhéroe."""
    heroe = lista.buscar(nombre)
    if heroe:
        casa_anterior = heroe.casa_comic
        heroe.casa_comic = nueva_casa
        print(f"[c] Casa de {heroe.nombre} actualizada: '{casa_anterior}' -> '{heroe.casa_comic}'")
    else:
        print(f"[c] '{nombre}' no se encuentra en la lista.")


def mostrar_por_palabra_en_biografia(lista: ListaEnlazada, palabras=("traje", "armadura")):
    """Punto d: Muestra los nombres de héroes cuya biografía contenga ciertas palabras."""
    print(f"[d] Superhéroes cuya biografía contiene '{palabras[0]}' o '{palabras[1]}':")
    encontrados = False
    for heroe in lista.barrido():
        bio_lower = heroe.biografia.lower()
        if any(palabra.lower() in bio_lower for palabra in palabras):
            print(f"    - {heroe.nombre}")
            encontrados = True
    if not encontrados:
        print("    (Ninguno coincide)")


def mostrar_anteriores_a_anio(lista: ListaEnlazada, anio_limite: int = 1963):
    """Punto e: Muestra nombre y casa de superhéroes con aparición previa al año dado."""
    print(f"[e] Superhéroes con fecha de aparición anterior a {anio_limite}:")
    encontrados = False
    for heroe in lista.barrido():
        if heroe.anio_aparicion < anio_limite:
            print(f"    - {heroe.nombre} | Casa: {heroe.casa_comic} (Año: {heroe.anio_aparicion})")
            encontrados = True
    if not encontrados:
        print("    (Ninguno)")


def mostrar_casa_de_heroes(lista: ListaEnlazada, nombres=("Capitana Marvel", "Mujer Maravilla")):
    """Punto f: Muestra la casa a la que pertenecen los superhéroes especificados."""
    print(f"[f] Casa a la que pertenecen:")
    for nombre in nombres:
        heroe = lista.buscar(nombre)
        if heroe:
            print(f"    - {heroe.nombre}: {heroe.casa_comic}")
        else:
            print(f"    - {nombre}: No se encuentra en la lista")


def mostrar_informacion_completa(lista: ListaEnlazada, nombres=("Flash", "Star-Lord")):
    """Punto g: Muestra toda la información de los superhéroes indicados."""
    print(f"[g] Información completa:")
    for nombre in nombres:
        heroe = lista.buscar(nombre)
        if heroe:
            print(f"--------------------------------------------------\n{heroe}")
        else:
            print(f"--------------------------------------------------\n'{nombre}' no se encuentra en la lista.")


def listar_por_iniciales(lista: ListaEnlazada, iniciales=('B', 'M', 'S')):
    """Punto h: Lista los superhéroes cuyos nombres comienzan con las letras dadas."""
    print(f"[h] Superhéroes que comienzan con las letras {', '.join(iniciales)}:")
    encontrados = False
    for heroe in lista.barrido():
        if heroe.nombre and heroe.nombre[0].upper() in iniciales:
            print(f"    - {heroe.nombre}")
            encontrados = True
    if not encontrados:
        print("    (Ninguno)")


def contar_superheroes_por_casa(lista: ListaEnlazada):
    """Punto i: Determina cuántos superhéroes hay de cada casa de cómic."""
    print(f"[i] Cantidad de superhéroes por casa de cómic:")
    conteo = {}
    for heroe in lista.barrido():
        casa = heroe.casa_comic.upper()
        conteo[casa] = conteo.get(casa, 0) + 1

    for casa, total in conteo.items():
        print(f"    - {casa}: {total}")

if __name__ == "__main__":
    lista_superheroes = ListaEnlazada()

    # Carga de superhéroes (incluyendo casos para testear cada punto)
    heroes = [
        Superheroe("Linterna Verde", 1940, "DC", "Posee un anillo de poder y un traje verde esmeralda."),
        Superheroe("Wolverine", 1974, "Marvel", "Mutante con garras de adamantium y factor curativo."),
        Superheroe("Dr. Strange", 1963, "DC", "Maestro de las artes místicas."),  # Se carga erróneamente en DC para probar (c)
        Superheroe("Iron Man", 1963, "Marvel", "Viste una armadura de combate con tecnología de punta."),
        Superheroe("Batman", 1939, "DC", "Vigilante de Gotham que viste un traje táctico oscuro."),
        Superheroe("Superman", 1938, "DC", "El hombre de acero con traje azul y capa roja."),
        Superheroe("Spider-Man", 1962, "Marvel", "Joven con poderes arácnidos que tejió su propio traje."),
        Superheroe("Capitana Marvel", 1968, "Marvel", "Heredera de poderes cósmicos Kree."),
        Superheroe("Mujer Maravilla", 1941, "DC", "Princesa amazona portadora de una armadura mística."),
        Superheroe("Flash", 1940, "DC", "El corredor escarlata que domina la Fuerza de la Velocidad."),
        Superheroe("Star-Lord", 1976, "Marvel", "Líder de los Guardianes de la Galaxia."),
        Superheroe("Magneto", 1963, "Marvel", "Líder mutante con casco y traje protector.")
    ]

    for h in heroes:
        lista_superheroes.insertar(h)

    print(f"=== LISTA INICIAL ({lista_superheroes.tamanio} superhéroes cargados) ===\n")

    # Ejecución de las actividades:
    eliminar_superheroe(lista_superheroes, "Linterna Verde")
    print()
    mostrar_anio_aparicion(lista_superheroes, "Wolverine")
    print()
    modificar_casa_comic(lista_superheroes, "Dr. Strange", "Marvel")
    print()
    mostrar_por_palabra_en_biografia(lista_superheroes, ("traje", "armadura"))
    print()
    mostrar_anteriores_a_anio(lista_superheroes, 1963)
    print()
    mostrar_casa_de_heroes(lista_superheroes, ("Capitana Marvel", "Mujer Maravilla"))
    print()
    mostrar_informacion_completa(lista_superheroes, ("Flash", "Star-Lord"))
    print()
    listar_por_iniciales(lista_superheroes, ('B', 'M', 'S'))
    print()
    contar_superheroes_por_casa(lista_superheroes)
    
    