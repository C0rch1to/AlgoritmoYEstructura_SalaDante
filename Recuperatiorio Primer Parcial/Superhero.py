

class Superhero:
    """
    Representa un personaje del universo Marvel.
    """

    def __init__(
        self,
        name,
        alias,
        real_name,
        bio,
        year,
        is_villain
    ):
        """
        Inicializa un personaje.

        Args:
            name (str): Nombre del personaje.
            alias (str): Alias o identidad alternativa.
            real_name (str): Nombre real.
            bio (str): Biografía del personaje.
            year (int): Año de primera aparición.
            is_villain (bool): Indica si es villano.
        """

        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.bio = bio
        self.year = year
        self.is_villain = is_villain

    def __str__(self):
        """
        Devuelve una representación legible del personaje.
        """

        tipo = "Villano" if self.is_villain else "Superhéroe"

        return (
            f"{self.name} | "
            f"{self.real_name} | "
            f"{self.year} | "
            f"{tipo}"
        )


# ============================================================
# CRITERIOS DE ORDENAMIENTO
# ============================================================

def by_name(hero):
    """
    Criterio para ordenar por nombre.
    """

    return hero.name.lower()


def by_real_name(hero):
    """
    Criterio para ordenar por nombre real.
    """

    return (
        hero.real_name is None,
        (hero.real_name or "").lower()
    )


def by_year(hero):
    """
    Criterio para ordenar por año de aparición.
    """

    return hero.year

