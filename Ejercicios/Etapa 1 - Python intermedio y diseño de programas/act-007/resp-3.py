def calcular_total(precio: float, cantidad: int=1, descuento: float=0):
    """
    Calcula el total de una compra aplicando descuento

    Parametros:
        precio (int, float): Precio unitario del producto. Debe ser mayor que 0.
        cantidad (int): Cantidad de productos. Debe ser mayor o igual que 1.
        descuento (int, float): Descuento como proporcion entre 0 y 1.

    Retorna:
        float: Total a pagar despues del descuento.
    """

    if precio <= 0:
        return "El precio indicado no es valido"

    if cantidad < 1:
        return "La cantidad no puede ser inferior a 1"

    if not 0 <= descuento <= 1:
        return "El descuento tiene que estar entre 0 y 1"


    total = precio * cantidad * (1 - descuento)

    return total

if __name__ == "__main__":
    # Prueba 1: Solo con precio
    print(calcular_total(10))

    # Prueba 2: Con argumentos posicionales
    print(calcular_total(25, 2, 0.15))

    # Prueba 3: Con argumentos nominales
    print(calcular_total(precio=12, cantidad=10, descuento=0.35))

    # Prueba 4: Omitir cantidad pero indique descuento
    print(calcular_total(9, descuento=0.15))

    # Prueba 5: Valores limites razonables
    print(calcular_total(100, 2, 0)) # Sin descuento
    print(calcular_total(100, 2, 1)) # Gratis



# Reglas
# Para entradas no validas lanzaremos al usuario un mensaje indicando el error
