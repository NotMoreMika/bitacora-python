numeros = [3, 8, 12, 5, 7, 20]

def analizar_lista(lista_numeros):
    es_par = 0
    resultado = 0
    for numero in lista_numeros:
        resultado += numero
        if numero > 10:
            print(numero)
        if numero % 2 == 0:
            es_par += 1
    print(es_par)
    print(resultado)

analizar_lista(numeros)
