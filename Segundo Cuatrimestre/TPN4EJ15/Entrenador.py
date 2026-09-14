from ListaEnlazada import ListaEnlazada


class Entrenador:
    """Clase que representa a un entrenador Pokémon.

    Cada entrenador posee una lista enlazada de Pokémons (lista de lista).
    """
    def __init__(self, nombre: str, torneos_ganados: int,
                 batallas_perdidas: int, batallas_ganadas: int):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.pokemones = ListaEnlazada()  # Sub-lista de Pokémons

    def __str__(self):
        return (f"Entrenador: {self.nombre} | Torneos ganados: {self.torneos_ganados} | "
                f"Batallas ganadas: {self.batallas_ganadas} | "
                f"Batallas perdidas: {self.batallas_perdidas}")
