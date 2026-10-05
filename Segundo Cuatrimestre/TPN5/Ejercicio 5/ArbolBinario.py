from typing import Optional, List, Generator

class Nodo:
    """
    Representa un nodo de un Árbol Binario de Búsqueda.
    Cumple con la consigna 'a': almacena el nombre del personaje y un campo
    booleano 'es_heroe' (True si es héroe, False si es villano).
    """
    def __init__(self, nombre: str, es_heroe: bool):
        self.nombre: str = nombre
        self.es_heroe: bool = es_heroe  # True: Héroe, False: Villano
        self.izq: Optional['Nodo'] = None
        self.der: Optional['Nodo'] = None

    def __str__(self) -> str:
        rol = "Superhéroe" if self.es_heroe else "Villano"
        return f"{self.nombre} [{rol}]"

    def __repr__(self) -> str:
        return f"Nodo({self.nombre!r}, es_heroe={self.es_heroe})"


class ArbolBinario:
    """
    TDA Árbol Binario de Búsqueda (ABB) ordenado alfabéticamente por 'nombre'.
    """
    def __init__(self):
        self.raiz: Optional[Nodo] = None

    def insertar(self, nombre: str, es_heroe: bool) -> None:
        """Inserta un nuevo personaje manteniendo el orden alfabético del árbol."""
        def __insertar(actual: Optional[Nodo], nombre: str, es_heroe: bool) -> Nodo:
            if actual is None:
                return Nodo(nombre, es_heroe)
            
            # Comparación insensible a mayúsculas para un orden natural consistente
            if nombre.lower() < actual.nombre.lower():
                actual.izq = __insertar(actual.izq, nombre, es_heroe)
            elif nombre.lower() > actual.nombre.lower():
                actual.der = __insertar(actual.der, nombre, es_heroe)
            else:
                # Si ya existe con el mismo nombre, se actualiza el rol
                actual.es_heroe = es_heroe
            return actual

        self.raiz = __insertar(self.raiz, nombre, es_heroe)

    def buscar(self, nombre: str) -> Optional[Nodo]:
        """Busca un personaje por coincidencia exacta (insensible a mayúsculas)."""
        actual = self.raiz
        clave = nombre.lower()
        while actual is not None:
            actual_clave = actual.nombre.lower()
            if clave == actual_clave:
                return actual
            elif clave < actual_clave:
                actual = actual.izq
            else:
                actual = actual.der
        return None

    def busqueda_proximidad(self, patron: str) -> List[Nodo]:
        """
        Búsqueda por proximidad: recorre el árbol y retorna todos los nodos
        cuyo nombre contenga el patrón de búsqueda (substring o prefijo).
        """
        coincidencias: List[Nodo] = []
        patron_lower = patron.lower()

        def __inorden(actual: Optional[Nodo]):
            if actual is not None:
                __inorden(actual.izq)
                if patron_lower in actual.nombre.lower():
                    coincidencias.append(actual)
                __inorden(actual.der)

        __inorden(self.raiz)
        return coincidencias

    def _obtener_minimo(self, nodo: Nodo) -> Nodo:
        """Devuelve el nodo con el valor menor en el subárbol dado."""
        actual = nodo
        while actual.izq is not None:
            actual = actual.izq
        return actual

    def eliminar(self, nombre: str) -> Optional[Nodo]:
        """
        Elimina el nodo con el nombre especificado manteniendo las propiedades de ABB.
        Retorna el nodo eliminado (o None si no existe).
        """
        eliminado: List[Optional[Nodo]] = [None]

        def __eliminar(actual: Optional[Nodo], clave: str) -> Optional[Nodo]:
            if actual is None:
                return None

            clave_actual = actual.nombre.lower()
            if clave < clave_actual:
                actual.izq = __eliminar(actual.izq, clave)
            elif clave > clave_actual:
                actual.der = __eliminar(actual.der, clave)
            else:
                eliminado[0] = Nodo(actual.nombre, actual.es_heroe)
                # Caso 1 y 2: Sin hijo izquierdo o sin hijo derecho
                if actual.izq is None:
                    return actual.der
                elif actual.der is None:
                    return actual.izq
                
                # Caso 3: Dos hijos. Se reemplaza por el sucesor inorden (mínimo del subárbol derecho)
                sucesor = self._obtener_minimo(actual.der)
                actual.nombre = sucesor.nombre
                actual.es_heroe = sucesor.es_heroe
                actual.der = __eliminar(actual.der, sucesor.nombre.lower())

            return actual

        self.raiz = __eliminar(self.raiz, nombre.lower())
        return eliminado[0]

    def modificar_nombre(self, nombre_actual: str, nuevo_nombre: str) -> bool:
        """
        Modifica el nombre de un personaje.
        Para preservar el orden y balance de búsqueda del ABB, se extrae el nodo
        y se reinserta con su nueva clave alfabética.
        """
        nodo_antiguo = self.buscar(nombre_actual)
        if nodo_antiguo is None:
            return False
        
        es_heroe = nodo_antiguo.es_heroe
        self.eliminar(nombre_actual)
        self.insertar(nuevo_nombre, es_heroe)
        return True

    def barrido_inorden(self) -> Generator[Nodo, None, None]:
        """Generador que realiza el recorrido inorden (ascendente A-Z)."""
        def __inorden(actual: Optional[Nodo]):
            if actual is not None:
                yield from __inorden(actual.izq)
                yield actual
                yield from __inorden(actual.der)

        yield from __inorden(self.raiz)

    def barrido_descendente(self) -> Generator[Nodo, None, None]:
        """Generador que realiza el recorrido inorden inverso (descendente Z-A)."""
        def __descendente(actual: Optional[Nodo]):
            if actual is not None:
                yield from __descendente(actual.der)
                yield actual
                yield from __descendente(actual.izq)

        yield from __descendente(self.raiz)

    def contar_nodos(self) -> int:
        """Retorna la cantidad total de nodos en el árbol."""
        def __contar(actual: Optional[Nodo]) -> int:
            if actual is None:
                return 0
            return 1 + __contar(actual.izq) + __contar(actual.der)

        return __contar(self.raiz)

    def contar_superheroes(self) -> int:
        """Cuenta únicamente los nodos donde es_heroe == True."""
        def __contar(actual: Optional[Nodo]) -> int:
            if actual is None:
                return 0
            cuenta = 1 if actual.es_heroe else 0
            return cuenta + __contar(actual.izq) + __contar(actual.der)

        return __contar(self.raiz)

    def contar_villanos(self) -> int:
        """Cuenta únicamente los nodos donde es_heroe == False."""
        def __contar(actual: Optional[Nodo]) -> int:
            if actual is None:
                return 0
            cuenta = 1 if not actual.es_heroe else 0
            return cuenta + __contar(actual.izq) + __contar(actual.der)

        return __contar(self.raiz)
