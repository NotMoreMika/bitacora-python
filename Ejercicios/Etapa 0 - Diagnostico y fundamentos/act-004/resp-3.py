numeros = [7, 12, 4, 19, 3, 12, 8]
lista_vacia = []
objetivo = 19

def buscar_numero(lista_numero, objetivo):

    if objetivo in lista_numero:
        print("El objetivo existe en la lista")
    else:
        print("El objetivo no existe en la lista")

buscar_numero(numeros, objetivo)
buscar_numero(lista_vacia, objetivo)

buscar_numero(numeros, 13)
