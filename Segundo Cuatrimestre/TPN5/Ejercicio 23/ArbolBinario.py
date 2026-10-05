from typing import Optional, List, Generator
from collections import deque

class NodoCriatura:
    """
    Nodo de un Árbol Binario de Búsqueda para las Criaturas Mitológicas.
    Cumple con los incisos:
      - 'nombre': Clave de ordenamiento alfabético en el ABB.
      - 'derrotado_por': Héroe o dios que derrotó a la criatura.
      - 'capturada': Héroe o dios que la capturó (consigna 'g').
      - 'descripcion': Breve descripción de la criatura (consigna 'b').
    """
    def __init__(
        self,
        nombre: str,
        derrotado_por: Optional[str] = None,
        capturada: Optional[str] = None,
        descripcion: Optional[str] = None
    ):
        self.nombre: str = nombre
        self.derrotado_por: Optional[str] = derrotado_por
        self.capturada: Optional[str] = capturada
        self.descripcion: Optional[str] = descripcion
        self.izq: Optional['NodoCriatura'] = None
        self.der: Optional['NodoCriatura'] = None

    def __str__(self) -> str:
        derrotador = self.derrotado_por if self.derrotado_por else "Nadie (-)"
        capturador = f" | Capturada por: {self.capturada}" if self.capturada else ""
        desc = f" | Descripción: {self.descripcion}" if self.descripcion else ""
        return f"{self.nombre} (Derrotado por: {derrotador}{capturador}{desc})"


class ArbolBinarioCriaturas:
    """
    TDA Árbol Binario de Búsqueda (ABB) para gestionar criaturas mitológicas.
    """
    def __init__(self):
        self.raiz: Optional[NodoCriatura] = None

    def insertar(
        self,
        nombre: str,
        derrotado_por: Optional[str] = None,
        capturada: Optional[str] = None,
        descripcion: Optional[str] = None
    ) -> None:
        """Inserta una criatura manteniendo el orden alfabético del árbol."""
        def __insertar(actual: Optional[NodoCriatura]) -> NodoCriatura:
            if actual is None:
                return NodoCriatura(nombre, derrotado_por, capturada, descripcion)

            if nombre.lower() < actual.nombre.lower():
                actual.izq = __insertar(actual.izq)
            elif nombre.lower() > actual.nombre.lower():
                actual.der = __insertar(actual.der)
            else:
                # Si ya existe, actualiza sus campos
                if derrotado_por is not None:
                    actual.derrotado_por = derrotado_por
                if capturada is not None:
                    actual.capturada = capturada
                if descripcion is not None:
                    actual.descripcion = descripcion
            return actual

        self.raiz = __insertar(self.raiz)

    def buscar(self, nombre: str) -> Optional[NodoCriatura]:
        """Búsqueda exacta por nombre (insensible a mayúsculas/minúsculas)."""
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

    def busqueda_coincidencia(self, criterio: str) -> List[NodoCriatura]:
        """
        Punto i: Permite búsquedas por coincidencia (subcadena insensible a mayúsculas).
        """
        coincidencias: List[NodoCriatura] = []
        criterio_lower = criterio.lower()

        def __inorden(actual: Optional[NodoCriatura]):
            if actual is not None:
                __inorden(actual.izq)
                if criterio_lower in actual.nombre.lower():
                    coincidencias.append(actual)
                __inorden(actual.der)

        __inorden(self.raiz)
        return coincidencias

    def _obtener_minimo(self, nodo: NodoCriatura) -> NodoCriatura:
        """Devuelve el nodo con la clave menor en el subárbol dado."""
        actual = nodo
        while actual.izq is not None:
            actual = actual.izq
        return actual

    def eliminar(self, nombre: str) -> Optional[NodoCriatura]:
        """
        Elimina el nodo con el nombre dado manteniendo las propiedades del ABB.
        Retorna una copia del nodo eliminado o None si no se encontró.
        """
        eliminado: List[Optional[NodoCriatura]] = [None]

        def __eliminar(actual: Optional[NodoCriatura], clave: str) -> Optional[NodoCriatura]:
            if actual is None:
                return None

            clave_actual = actual.nombre.lower()
            if clave < clave_actual:
                actual.izq = __eliminar(actual.izq, clave)
            elif clave > clave_actual:
                actual.der = __eliminar(actual.der, clave)
            else:
                eliminado[0] = NodoCriatura(
                    actual.nombre,
                    actual.derrotado_por,
                    actual.capturada,
                    actual.descripcion
                )
                # Casos 1 y 2: Un solo hijo o ninguno
                if actual.izq is None:
                    return actual.der
                elif actual.der is None:
                    return actual.izq

                # Caso 3: Dos hijos. Reemplazo por sucesor inorden
                sucesor = self._obtener_minimo(actual.der)
                actual.nombre = sucesor.nombre
                actual.derrotado_por = sucesor.derrotado_por
                actual.capturada = sucesor.capturada
                actual.descripcion = sucesor.descripcion
                actual.der = __eliminar(actual.der, sucesor.nombre.lower())

            return actual

        self.raiz = __eliminar(self.raiz, nombre.lower())
        return eliminado[0]

    def modificar_nombre(self, nombre_actual: str, nuevo_nombre: str) -> bool:
        """
        Modifica el nombre de una criatura asegurando la integridad del ABB
        (extrae y reinserta según la nueva posición alfabética).
        """
        nodo_antiguo = self.buscar(nombre_actual)
        if nodo_antiguo is None:
            return False

        # Guardamos los atributos actuales
        derrotado_por = nodo_antiguo.derrotado_por
        capturada = nodo_antiguo.capturada
        descripcion = nodo_antiguo.descripcion

        # Eliminamos e insertamos con el nuevo nombre
        self.eliminar(nombre_actual)
        self.insertar(nuevo_nombre, derrotado_por, capturada, descripcion)
        return True

    def barrido_inorden(self) -> Generator[NodoCriatura, None, None]:
        """Punto a: Recorrido inorden del árbol (orden alfabético)."""
        def __inorden(actual: Optional[NodoCriatura]):
            if actual is not None:
                yield from __inorden(actual.izq)
                yield actual
                yield from __inorden(actual.der)

        yield from __inorden(self.raiz)

    def barrido_por_nivel(self) -> Generator[tuple[int, NodoCriatura], None, None]:
        """
        Punto m: Realiza un recorrido por nivel del árbol usando una cola (BFS).
        Produce tuplas (nivel, nodo).
        """
        if self.raiz is None:
            return

        cola: deque[tuple[int, NodoCriatura]] = deque([(0, self.raiz)])
        while cola:
            nivel, actual = cola.popleft()
            yield (nivel, actual)
            if actual.izq is not None:
                cola.append((nivel + 1, actual.izq))
            if actual.der is not None:
                cola.append((nivel + 1, actual.der))

    def contar_nodos(self) -> int:
        """Retorna la cantidad total de nodos en el árbol."""
        def __contar(actual: Optional[NodoCriatura]) -> int:
            if actual is None:
                return 0
            return 1 + __contar(actual.izq) + __contar(actual.der)

        return __contar(self.raiz)
