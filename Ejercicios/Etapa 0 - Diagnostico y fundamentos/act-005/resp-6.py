def contar_palabras(lista_palabras):
    if len(lista_palabras) == 0:
        return print("La lista no puede estar vacia")

    contador = {}

    for palabra in lista_palabras:

        if palabra not in contador:
            contador[palabra] = 0

        contador[palabra] += 1

    print(contador)

lista1 = ["python", "js", "python", "css", "js", "python"]

contar_palabras(lista1)
