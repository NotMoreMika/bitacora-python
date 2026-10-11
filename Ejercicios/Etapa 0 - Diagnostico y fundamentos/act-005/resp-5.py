def analizar_numeros(lista_numeros):

    if len(lista_numeros) == 0:
        return print("La lista esta vacia")
    if len(lista_numeros) == 1:
        return print("La lista no puede tener menos de 2 numeros")

    suma_positivos = 0
    negativos = 0
    maximo = lista_numeros[0]
    minimo = lista_numeros[1]

    if maximo < minimo:
        maximo = lista_numeros[1]
        minimo = lista_numeros[0]

    for numero in lista_numeros:

        if numero > 0:
            suma_positivos += numero
        if numero < 0:
            negativos += 1

        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero

    if maximo == minimo:
        print("Todos los numeros son iguales")
    else:
        print(f"En la lista el mayor numero es {maximo} y el menor numero es {minimo}, ademas hay {negativos} negativos y la suma de todos los numeros positivos da {suma_positivos}")

lista1 = [8, 15, 3, 20, 11]
lista2 = [-8, -2, -15, -4]
lista3 = [7, 7, 7, 7]
lista4 = [2]
lista5 = [15, 8, -3, 22, 7, 22, -10, 4, 18, 0, 22]
lista6 = [0, 0, 0, 0]
lista7 = []

analizar_numeros(lista1)
analizar_numeros(lista2)
analizar_numeros(lista3)
analizar_numeros(lista4)
analizar_numeros(lista5)
analizar_numeros(lista6)
analizar_numeros(lista7)
