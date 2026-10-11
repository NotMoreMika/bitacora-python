def analizar_lista(lista_numeros):
    if len(lista_numeros) == 0:
        return print("La lista esta vacia")

    positivos = 0
    negativos = 0
    ceros = 0
    suma_total = 0

    for numero in lista_numeros:
        suma_total += numero
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            ceros += 1

    print(f"Hay {positivos} positivos, {negativos} negativos, {ceros} cero, la suma total es {suma_total}")

lista1 = [8, 15, 3, 20, 11]
lista2 = [-8, -2, -15, -4]
lista3 = [7, 7, 7, 7]
lista4 = [1]
lista5 = [15, 8, -3, 22, 7, 22, -10, 4, 18, 0, 22]
lista6 = [0, 0, 0, 0]

analizar_lista(lista1)
analizar_lista(lista2)
analizar_lista(lista3)
analizar_lista(lista4)
analizar_lista(lista5)
analizar_lista(lista6)
