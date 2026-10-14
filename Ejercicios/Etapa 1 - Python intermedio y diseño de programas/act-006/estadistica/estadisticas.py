def calcular_total(valores):
    if not valores:
        return 0
    return sum(valores)

def contar_positivos(valores):
    if not valores:
        return "No se acepta listas vacias"

    positivos = 0

    for valor in valores:
        if valor > 0:
            positivos += 1

    return positivos

def obtener_promedio(valores):
    if not valores:
        return 0
    resultado = calcular_total(valores)
    return resultado / len(valores)

# Las listas vacias se manejan como un caso atipico
# Para calcular_total y obtener_promedio que retorne 0
# Para contar positivos que indique que no se acepta listas vacias
# La razon es que en los positivos puede dar a entender que no hay numeros positivos siendo que en realidad no hay numeros
