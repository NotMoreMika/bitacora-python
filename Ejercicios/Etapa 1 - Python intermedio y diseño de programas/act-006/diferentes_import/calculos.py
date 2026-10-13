def calcular_total(valores):
    return sum(valores)

def contar_positivos(valores):
    positivos = 0

    for valor in valores:
        if valor > 0:
            positivos += 1

    return positivos

def es_par(valor):
    return valor % 2 == 0
