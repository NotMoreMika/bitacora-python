numeros = [3, 8, 11, 14, 5, 20, 7, 12]

def cuadrados(lista_numeros):
    pares_cuadrado = []

    for numero in lista_numeros:
        if numero % 2 == 0:
            pares_cuadrado.append(numero ** 2)

    print(pares_cuadrado)

cuadrados(numeros)
