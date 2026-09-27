lista_compra = ["Arroz", "Frijol"]
#indicacion = None

def show_menu():
    print("=============== MENU ===============")
    print("1 - Mostrar todos los productos")
    print("2 - Agregar un producto")
    print("3 - Eliminar un producto")
    print("4 - Buscar un producto de la lista")

def pedir_orden():
    orden = int(input("Que desea hacer? "))
    return orden


def start():
    show_menu()
    orden = pedir_orden()
    if orden == 1:
        for producto in lista_compra:
            print(producto)
        start()
    elif orden == 2:
        nuevo_producto = input("Que producto desea añadir")
        lista_compra.append(nuevo_producto)
        start()
    elif orden == 3:
        producto_eliminar = input("Que producto desea quitar?")
        lista_compra.remove(producto_eliminar)
        start()
    elif orden == 4:
        producto_buscar = input("Que producto desea revisar si tiene")

        if producto_buscar in lista_compra:
            print("El producto esta en la lista")
        else:
            print("El producto no esta en la lista")
        start()



start()
