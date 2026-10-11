def cuadrados(lista_numeros):
    if len(lista_numeros) == 0:
        return print("La lista esta vacia")

    pares = 0
    pares_cuadrados = []

    for numero in lista_numeros:
        if numero % 2 == 0:
            pares += 1
            pares_cuadrados.append(numero ** 2)

    if pares == 0:
        print("No hay ningun numero par en la lista")
    else:
        print(pares_cuadrados)

lista1 = [8, 15, 3, 20, 11]
lista2 = [-8, -2, -15, -4]
lista3 = [7, 7, 7, 7]
lista4 = [2]
lista5 = [15, 8, -3, 22, 7, 22, -10, 4, 18, 0, 22]
lista6 = [0, 0, 0, 0]
lista7 = []

cuadrados(lista1)
cuadrados(lista2)
cuadrados(lista3)
cuadrados(lista4)
cuadrados(lista5)
cuadrados(lista6)
cuadrados(lista7)

