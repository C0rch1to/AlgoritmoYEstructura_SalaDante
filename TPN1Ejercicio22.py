
# Trabajo a entregar 27/04

import random

contador = 0 # Va a contar los intentos de encontrar el sable de luz
sable_de_luz = random.randint(1, 10) # va a asignarle un numero entero aleatorio al sable de luz, el cual puede estar una o mas veces en la mochila (o no estar)
print(f"El sable de luz es numero {sable_de_luz}")

def llenar_mochila(lista): #llena la mochila con numeros aleatorios, para poder ver como la fuerza se comporta en diferentes casos
    for i in range(10):
        lista.append(random.randint(1, 10))
    print(lista)

def Usar_la_fuerza(lista): # Va a revisar la mochila elemento por elemento, hasta encontrar el sable de luz o revisar toda la mochila
    global contador
    if lista[contador] == sable_de_luz:
        return print(f"Has encontrado el sable de luz en el intento numero {contador + 1}")
    elif contador == len(lista) - 1:
        return print("El sable de luz no esta en la mochila")
    else:
        contador += 1
        print(f"Has encontrado {contador} objetos inútiles")
        Usar_la_fuerza(lista)
        
mochila = [] 
llenar_mochila(mochila)
Usar_la_fuerza(mochila)