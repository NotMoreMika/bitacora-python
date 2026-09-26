def imprimir_pares(numeros):
    for i in numeros:
        if numeros[i-1] % 2 == 0:
            print(numeros[i-1])

lista1 = [1, 2, 3, 4, 5, 6]
imprimir_pares(lista1)
