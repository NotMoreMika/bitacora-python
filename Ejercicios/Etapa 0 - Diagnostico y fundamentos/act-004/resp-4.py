lista1 = [8, 15, 3, 20, 11]
lista2 = [-8, -2, -15, -4]
lista3 = [7, 7, 7, 7]
lista4 = [1]

def max_min(lista_numeros):

    if len(lista_numeros) <= 1:
        return print("La lista no es valida, introduce una lista con mas de 1 valor")

    maximo = lista_numeros[0]
    minimo = lista_numeros[0]

    for numero in lista_numeros[1:]:

        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero

    if maximo == minimo:
        print("En la lista todos los numeros son iguales")
    else:
        print("El valor maximo es: ", maximo)
        print("El valor minimo es: ", minimo)

max_min(lista1)
max_min(lista2)
max_min(lista3)
max_min(lista4)
