numeros = [12, -4, 7, 18, -9, 20, 3, -2, 15]

def analizar_lista(lista_numeros):

    suma = 0
    negativos = 0
    mayor_positivo = 0
    numeros_positivos = []

    for numero in lista_numeros:
        if numero > 0:
            suma += numero
        elif numero < 0:
            negativos += 1

        if numero > 10:
            numeros_positivos.append(numero)

        if numero > mayor_positivo:
            mayor_positivo = numero

    print(f"La suma de los positivos es: {suma}")
    print(f"En la lista hay {negativos} numeros negativos")
    if mayor_positivo == 0:
        print("En la lista no habia numeros positivos")
    else:
        print(f"El mayor positivo es {mayor_positivo}")
    print(f"Los numeros positivos mayor que 10 son: {numeros_positivos}")

analizar_lista(numeros)
