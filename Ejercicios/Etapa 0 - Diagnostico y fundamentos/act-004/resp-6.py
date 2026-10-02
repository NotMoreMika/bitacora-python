lista1 = [10, 12, 8, 25, 139, 32]
lista2 = [30, 10, 20, 40, 15]
lista3 = [-5, -2, -10, -1]


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

encontrar_segundo(lista1)
encontrar_segundo(lista2)
encontrar_segundo(lista3)
