def romano_a_decimal(romano): # La funcion que transforma el numero romano a decimal
    valores = {
        'I': 1,
        'V': 5,
        'X': 10, #El diccionario almacena el valor de cada letra
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    
    if romano == "": # Si el campo esta vacio la funcion devolvera 0
        return 0

    if len(romano) == 1 and valores.get(romano[0], -1) != -1:
        return valores[romano] # Si el numero romano tiene solo una letra, la funcion devolvera el valor de esa letra
    
    if valores.get(romano[0], -1) == -1:
        return -1 # Si el numero romano tiene una letra que no esta en el diccionario
    elif valores[romano[0]] < valores[romano[1]]: # Si el numero romano es mas largo la funcion sumara o restara como sea necesario
        return valores[romano[1]] - valores[romano[0]] + romano_a_decimal(romano[2:])
    else:
        return valores[romano[0]] + romano_a_decimal(romano[1:])


# Programa principal
numero = ""

while numero != "SALIR": # Para poder salir del programa
    numero = input("Ingrese un número romano (o 'salir'): ").upper()
    if numero != "SALIR": # Para que al salir del programa no intente convertir "SALIR" a decimal
        if romano_a_decimal(numero) == -1:
            print("Número romano inválido")
        else:
            print("Decimal:", romano_a_decimal(numero))  

print("Programa finalizado.")