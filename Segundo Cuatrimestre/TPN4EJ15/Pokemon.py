class Pokemon:
    """Clase que representa a un Pokémon."""
    def __init__(self, nombre: str, nivel: int, tipo: str, subtipo: str):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return (f"Nombre: {self.nombre} | Nivel: {self.nivel} | "
                f"Tipo: {self.tipo} | Subtipo: {self.subtipo}")
