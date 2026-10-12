def analizar_numeros(lista_numeros):

    if len(lista_numeros) == 0:
        return "La lista esta vacia"

    suma_positivos = 0
    negativos = 0
    maximo = lista_numeros[0]
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

    return suma_positivos, negativos, maximo, minimo

lista1 = [8, 15, 3, 20, 11]
lista2 = [-8, -2, -15, -4]
lista3 = [7, 7, 7, 7]
lista4 = [2]
lista5 = [15, 8, -3, 22, 7, 22, -10, 4, 18, 0, 22]
lista6 = [0, 0, 0, 0]
lista7 = []

print(analizar_numeros(lista1))
print(analizar_numeros(lista2))
print(analizar_numeros(lista3))
print(analizar_numeros(lista4))
print(analizar_numeros(lista5))
print(analizar_numeros(lista6))
print(analizar_numeros(lista7))
