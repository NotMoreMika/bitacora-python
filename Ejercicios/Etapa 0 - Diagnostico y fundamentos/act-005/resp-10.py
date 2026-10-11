def encontrar_segundo(lista_numeros):

    if len(lista_numeros) <= 1:
        return print("La lista no puede estar vacia o tener un solo elemento")

    mayor = lista_numeros[0]
    segundo_mayor = lista_numeros[1]

    if mayor < segundo_mayor:
        mayor = lista_numeros[1]
        segundo_mayor = lista_numeros[0]

    for numero in lista_numeros:

        if numero > mayor:
            segundo_mayor = mayor
            mayor = numero
        if numero < mayor and numero > segundo_mayor:
            segundo_mayor = numero
        if mayor == segundo_mayor:
            segundo_mayor = numero


    if mayor == segundo_mayor:
        print("Los elementos de la lista son iguales")
    else:
        print(f"El segundo mayor es: {segundo_mayor}")

lista1 = [8, 15, 3, 20, 11]
lista2 = [-8, -2, -15, -4]
lista3 = [7, 7, 7, 7]
lista4 = [2]
lista5 = [15, 8, -3, 22, 7, 22, -10, 4, 18, 0, 22]
lista6 = [0, 0, 0, 0]
lista7 = []
lista8 = [7, 7, 7, 6]

encontrar_segundo(lista1)
encontrar_segundo(lista2)
encontrar_segundo(lista3)
encontrar_segundo(lista4)
encontrar_segundo(lista5)
encontrar_segundo(lista6)
encontrar_segundo(lista7)
encontrar_segundo(lista8)
