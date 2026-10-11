def buscar_numero(lista_numeros, objetivo):

    if len(lista_numeros) == 0:
        return print("La lista esta vacia")

    existe = False
    valor = None

    for numero in lista_numeros:
        if numero > objetivo and numero % 2 == 0:
           existe = True
           valor = numero
           break

    if existe:
        print(f"El numero {valor} cumple los requisitos")
    else:
        print("Ningun numero cumple los requisitos")

lista1 = [8, 15, 3, 20, 11]
lista2 = [-8, -2, -15, -4]
lista3 = [7, 7, 7, 7]
lista4 = [2]
lista5 = [15, 8, -3, 22, 7, 22, -10, 4, 18, 0, 22]
lista6 = [0, 0, 0, 0]
lista7 = []

buscar_numero(lista1, 8)
buscar_numero(lista2, 8)
buscar_numero(lista3, 8)
buscar_numero(lista4, 8)
buscar_numero(lista5, 8)
buscar_numero(lista6, 8)
buscar_numero(lista7, 8)
