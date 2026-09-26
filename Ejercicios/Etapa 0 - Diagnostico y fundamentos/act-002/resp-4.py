def contar_pares(numeros):
    es_par = 0
    for i in numeros:
        if numeros[i-1] % 2 == 0:
            es_par += 1
    return es_par

list1 = [1, 2, 3, 4, 5, 6]

print(contar_pares(list1))
