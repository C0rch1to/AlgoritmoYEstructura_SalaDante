
# Clase Notificacion


class Notificacion:
    def __init__(self, hora, app, mensaje):
        self.hora = hora
        self.app = app
        self.mensaje = mensaje

    def __str__(self):
        return f"[{self.hora}] {self.app}: {self.mensaje}"

# TDA Cola

class Cola:
    def __init__(self):
        self.datos = []

    def arribo(self, dato):
        self.datos.append(dato)

    def atencion(self):
        if not self.cola_vacia():
            return self.datos.pop(0)

    def cola_vacia(self):
        return len(self.datos) == 0

    def tamanio(self):
        return len(self.datos)

# TDA Pila

class Pila:
    def __init__(self):
        self.datos = []

    def apilar(self, dato):
        self.datos.append(dato)

    def desapilar(self):
        if not self.pila_vacia():
            return self.datos.pop()

    def pila_vacia(self):
        return len(self.datos) == 0

    def tamanio(self):
        return len(self.datos)


# ==========================================
# a) Eliminar notificaciones de Facebook
# ==========================================

def eliminar_facebook(cola):
    cola_aux = Cola()

    while not cola.cola_vacia():
        noti = cola.atencion()

        if noti.app != "Facebook":
            cola_aux.arribo(noti)

    while not cola_aux.cola_vacia():
        cola.arribo(cola_aux.atencion())


# ==========================================
# b) Mostrar tweets que contengan Python
#    sin perder datos
# ==========================================

def mostrar_twitter_python(cola):
    cola_aux = Cola()

    while not cola.cola_vacia():
        noti = cola.atencion()

        if (noti.app == "Twitter"
                and "python" in noti.mensaje.lower()):
            print(noti)

        cola_aux.arribo(noti)

    while not cola_aux.cola_vacia():
        cola.arribo(cola_aux.atencion())



# c) Guardar en una pila las notificaciones
#    entre 11:43 y 15:57 y contarlas
def notificaciones_en_rango(cola):
    cola_aux = Cola()
    pila = Pila()

    while not cola.cola_vacia():
        noti = cola.atencion()

        if "11:43" <= noti.hora <= "15:57":
            pila.apilar(noti)

        cola_aux.arribo(noti)

    while not cola_aux.cola_vacia():
        cola.arribo(cola_aux.atencion())

    return pila, pila.tamanio()



# Carga de datos de prueba

cola_notificaciones = Cola()

cola_notificaciones.arribo(
    Notificacion("10:15", "Facebook",
                 "Juan comentó tu publicación")
)

cola_notificaciones.arribo(
    Notificacion("12:30", "Twitter",
                 "Curso de Python gratuito")
)

cola_notificaciones.arribo(
    Notificacion("14:10", "Instagram",
                 "Nuevo seguidor")
)

cola_notificaciones.arribo(
    Notificacion("15:20", "Twitter",
                 "Python es tendencia")
)

cola_notificaciones.arribo(
    Notificacion("16:45", "Facebook",
                 "Nuevo mensaje recibido")
)

cola_notificaciones.arribo(
    Notificacion("13:50", "WhatsApp",
                 "Hola, ¿cómo estás?")
)

# PRUEBA

print("INCISO B:")
mostrar_twitter_python(cola_notificaciones)

print("\n INCISO C:")
pila_rango, cantidad = notificaciones_en_rango(
    cola_notificaciones
)

print("Cantidad de notificaciones:", cantidad)

print("\nContenido de la pila:")

while not pila_rango.pila_vacia():
    print(pila_rango.desapilar())

print("\n INCISO A:")
eliminar_facebook(cola_notificaciones)

print("Cola sin notificaciones de Facebook:")

while not cola_notificaciones.cola_vacia():
    print(cola_notificaciones.atencion())