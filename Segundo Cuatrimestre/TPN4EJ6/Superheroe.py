class Superheroe:
    """Clase que representa a un superhéroe."""
    def __init__(self, nombre: str, anio_aparicion: int, casa_comic: str, biografia: str):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa_comic = casa_comic  # Marvel o DC
        self.biografia = biografia

    def __str__(self):
        return (f"Nombre: {self.nombre} | Año de aparición: {self.anio_aparicion} | "
                f"Casa: {self.casa_comic}\nBiografía: {self.biografia}")