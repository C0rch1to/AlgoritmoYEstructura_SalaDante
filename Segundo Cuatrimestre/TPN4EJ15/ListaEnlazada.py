from Nodo import Nodo


class ListaEnlazada:
    """TDA Lista Simplemente Enlazada con operaciones fundamentales."""
    def __init__(self):
        self.inicio = None
        self.tamanio = 0

    def esta_vacia(self) -> bool:
        return self.inicio is None

    def insertar(self, dato):
        """Inserta un nuevo elemento al final de la lista."""
        nuevo_nodo = Nodo(dato)
        if self.inicio is None:
            self.inicio = nuevo_nodo
        else:
            actual = self.inicio
            while actual.sig is not None:
                actual = actual.sig
            actual.sig = nuevo_nodo
        self.tamanio += 1

    def eliminar(self, clave_nombre: str):
        """
        Elimina el nodo cuyo dato coincide con el nombre indicado.
        Retorna el objeto eliminado si existía, o None si no se encontró.
        """
        actual = self.inicio
        anterior = None

        while actual is not None and actual.info.nombre.lower() != clave_nombre.lower():
            anterior = actual
            actual = actual.sig

        if actual is None:
            return None

        if anterior is None:
            self.inicio = actual.sig
        else:
            anterior.sig = actual.sig

        self.tamanio -= 1
        return actual.info

    def buscar(self, clave_nombre: str):
        """Busca un elemento por nombre y retorna el objeto o None."""
        actual = self.inicio
        while actual is not None:
            if actual.info.nombre.lower() == clave_nombre.lower():
                return actual.info
            actual = actual.sig
        return None

    def barrido(self):
        """Generador para recorrer iterativamente los elementos de la lista."""
        actual = self.inicio
        while actual is not None:
            yield actual.info
            actual = actual.sig
