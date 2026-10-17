def crear_multiplicador(factor):
    """
    Crea una función que multiplica cualquier número por el factor dado.

    Parametros:
        factor (int, float): El número por el que se multiplicará.

    Retorno:
        function: Una función que recibe un número y devuelve el resultado.
    """
    def multiplicar(numero):
        return numero * factor

    return multiplicar

if __name__ == "__main__":
    multiplicar_por_2 = crear_multiplicador(2)
    multiplicar_por_10 = crear_multiplicador(10)

    print(f"multiplicar_por_2(5)  = {multiplicar_por_2(5)}")
    print(f"multiplicar_por_10(5) = {multiplicar_por_10(5)}")
    print(f"multiplicar_por_2(7)  = {multiplicar_por_2(7)}")
    print(f"multiplicar_por_10(7) = {multiplicar_por_10(7)}")

"""
Cada función conserva su propio factor, el que se le pasó cuando se creó.
Es como si cada función tuviera una "mochila" privada con el valor que necesita.
No se necesita una variable global porque cada función guarda su propia copia privada
de factor dentro de sí misma; cada multiplicar tiene la suya.
"""
