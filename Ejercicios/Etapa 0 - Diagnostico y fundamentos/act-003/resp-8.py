numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def encontrar_segundo(lista_numeros):

    for numero in lista_numeros:
        mas_grande = None
        segundo_mayor = None
        mas_grande = numero

        if mas_grande > numero:
            if segundo_mayor > numero:
                continue
            elif segundo_mayor < numero:
                segundo_mayor = numero

    print(segundo_mayor)

encontrar_segundo(numeros)

# No supe resolverlo xDDD
