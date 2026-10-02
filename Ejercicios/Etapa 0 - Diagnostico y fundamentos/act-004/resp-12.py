numeros = [15, 8, -3, 22, 7, 22, -10, 4, 18, 0, 22]

def analizar_lista(lista_numeros):

    positivos = 0
    negativos = 0
    ceros = 0
    suma_positivos = 0
    suma_total = 0
    maximo = lista_numeros[0]
    minimo = lista_numeros[1]
    cant_maximo = {}
    pares = []

    if maximo < minimo:
        maximo = lista_numeros[1]
        minimo = lista_numeros[0]

    cant_maximo[maximo] = 0

    for numero in lista_numeros:
        suma_total += numero

        if numero > 0:
            positivos += 1
            suma_positivos += numero
        elif numero < 0:
            negativos += 1
        else:
            ceros += 1

        if numero > maximo:
            maximo = numero
            cant_maximo[maximo] = 0

        if numero == maximo:
            cant_maximo[maximo] += 1

        if numero < minimo:
            minimo = numero

        if numero != 0 and  numero % 2 == 0:
            pares.append(numero)

    promedio = suma_total / len(lista_numeros)

    print(f"Hay {positivos} positivos")
    print(f"Hay {negativos} negativos")
    print(f"Hay {ceros} ceros")
    print(f"La suma de los positivos es {suma_positivos}")
    print(f"El promedio total es {promedio}")
    print(f"El mayor valor es {maximo}")
    print(f"El menor valor es {minimo}")
    print(f"El mayor valor aparece {cant_maximo[maximo]} veces")
    print(f"Los pares son: {pares}")

analizar_lista(numeros)
