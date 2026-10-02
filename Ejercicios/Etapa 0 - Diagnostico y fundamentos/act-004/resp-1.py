numeros = [12, -5, 0, 8, -3, 0, 15, -10]
lista_vacia = []
lista_uno = [12]
lista_repetidos = [12, -5, 0, 8, -5, -3, 0, 12, 15, -10]
lista_iguales = [12, 12, 12]



def analizar_numeros(lista_numeros):
    positivos = 0
    negativos = 0
    ceros = 0

    for numero in lista_numeros:
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            ceros += 1
    print("Numeros positivos: ", positivos)
    print("Numeros negativos: ", negativos)
    print("Iguales a cero: ", ceros)

analizar_numeros(numeros)
analizar_numeros(lista_vacia)
analizar_numeros(lista_uno)
analizar_numeros(lista_repetidos)
analizar_numeros(lista_iguales)
