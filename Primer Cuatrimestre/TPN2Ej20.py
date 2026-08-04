# Ejercicio 20 TP N2

# Diccionario con direcciones opuestas
opuestas = {
    "norte": "sur",
    "sur": "norte",
    "este": "oeste",
    "oeste": "este",
    "noreste": "suroeste",
    "noroeste": "sureste",
    "sureste": "noroeste",
    "suroeste": "noreste"
}

# Lista para guardar los movimientos
movimientos = []

# Cantidad de movimientos a registrar
cantidad = int(input("¿Cuántos movimientos realizará el robot?: "))

# Registro de movimientos
for i in range(cantidad):
    pasos = int(input(f"Ingrese la cantidad de pasos del movimiento {i+1}: "))
    direccion = input("Ingrese la dirección: ").lower()

    movimientos.append((pasos, direccion))

# Mostrar recorrido original
print("\nRecorrido realizado:")
for pasos, direccion in movimientos:
    print(f"{pasos} pasos hacia {direccion}")

# Generar camino de regreso
print("\nMovimientos para volver al punto de partida:")

for pasos, direccion in reversed(movimientos):
    print(f"{pasos} pasos hacia {opuestas[direccion]}")