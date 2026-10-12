def analizar_lista(lista_numeros):

    if len(lista_numeros) == 0:
        return print("La lista esta vacia")

    mayor = lista_numeros[0]
    menor = lista_numeros[0]
    veces_mayor = {}
    pos_mayor = 0

    if mayor < menor:
        mayor = lista_numeros[1]
        menor = lista_numeros[0]
        pos_mayor = 1

    veces_mayor[mayor] = 0

    for i, numero in enumerate(lista_numeros):

        if numero > mayor:
            mayor = numero
            pos_mayor = i
            veces_mayor[mayor] = 0

        if numero == mayor:
            veces_mayor[mayor] += 1

        if numero < menor:
            menor = numero

    print(f"El mayor valor es {mayor} aparece en la posicion {pos_mayor} y se repite {veces_mayor[mayor]}")
    print(f"El menor numero es {menor}")


lista1 = [8, 15, 3, 20, 11]
lista2 = [-8, -2, -15, -4]
lista3 = [7, 7, 7, 7]
lista4 = [2]
lista5 = [15, 8, -3, 22, 7, 22, -10, 4, 18, 0, 22]
lista6 = [0, 0, 0, 0]
lista7 = []

analizar_lista(lista1)
analizar_lista(lista2)
analizar_lista(lista3)
analizar_lista(lista4)
analizar_lista(lista5)
analizar_lista(lista6)
analizar_lista(lista7)
