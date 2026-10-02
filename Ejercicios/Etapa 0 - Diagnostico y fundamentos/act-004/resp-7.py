numeros = [14, 7, 25, 9, 31, 18]

def max_pos(lista_numeros):
    max = lista_numeros[0]
    posicion = 0

    for i, numero in enumerate(lista_numeros):

        if numero > max:
            max = numero
            posicion = i

    print(f"El mayor numero es {max} y su posicion es {posicion}")

max_pos(numeros)
