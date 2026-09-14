class Nodo:
    """Nodo para la lista simplemente enlazada."""
    def __init__(self, info=None):
        self.info = info
        self.sig = None