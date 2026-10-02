numeros = [10, 15, 8, 22, 5, 18]
lista_vacia = []
lista_uno = [12]
lista_repetidos = [12, -5, 0, 8, -5, -3, 0, 12, 15, -10]
lista_iguales = [12, 12, 12]

def sum_prom(lista_numeros):
    suma = 0

    for numero in lista_numeros:
        suma += numero

    promedio = suma / len(lista_numeros)

    print("La suma total es: ", suma)
    print("El promedio es: ", promedio)

sum_prom(numeros)
sum_prom(lista_uno)
sum_prom(lista_repetidos)
sum_prom(lista_iguales)
sum_prom(lista_vacia)
