def encontrar_segundo(lista_numeros):
    mayor = lista_numeros[0]
    segundo_mayor = lista_numeros[1]

    if mayor < segundo_mayor:
        mayor = lista_numeros[1]
        segundo_mayor = lista_numeros[0]

    for numero in lista_numeros[2:]:

        if numero > mayor:
            segundo_mayor = mayor
            mayor = numero
        elif numero > segundo_mayor:
            segundo_mayor = numero

    print(f"El segundo mayor es: {segundo_mayor}")

numeros = [97, 35, 76, 23, 1, -3, -5, 0, 1110]

encontrar_segundo(numeros)
