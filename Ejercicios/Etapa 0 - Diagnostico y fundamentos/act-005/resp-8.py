def analizar_lista(lista_numeros):
    if len(lista_numeros) <= 1:
        return print("La lista no puede estar vacia o tener 1 elemento")

    cant_numero = len(lista_numeros)
    suma_total = 0

    pares = 0
    impares = 0

    mayor = lista_numeros[0]
    menor = lista_numeros[1]

    if mayor < menor:
        mayor = lista_numeros[1]
        menor = lista_numeros[0]

    for numero in lista_numeros:

        suma_total += numero

        if numero % 2 == 0 and numero != 0:
            pares += 1
        elif numero % 2 == 1 and numero !=0:
            impares += 1

        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero

    promedio = suma_total / cant_numero

    print("======Informe=====")
    print(f"La cantidad de numeros es {cant_numero}")
    print(f"La suma total es {suma_total}")
    print(f"El promedio es {promedio}")
    print(f"El mayor numero es {mayor}")
    print(f"El menor numero es {menor}")
    print(f"Hay {pares} numeros pares")
    print(f"Hay {impares} numeros impares")

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


