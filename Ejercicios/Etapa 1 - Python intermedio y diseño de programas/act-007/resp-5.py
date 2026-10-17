def sumar_numeros(*args):
    """
    Calcula la suma de todos los numeros.

    Parametros:
        *args: Cantidad variable de numeros.

    Retorno:
        int: Total de la suma de los numeros. Si no recibe argumetos devuelve 0.
    """
    if len(args) == 0:
        return 0

    return sum(args)

def crear_ficha(nombre: str, **datos):
    """"
    Crea una ficha con el nombre y otros datos adicionales

    Parametros:
        nombre (str): Nombre de la persona
        **datos: Pares clave-valor con datos adicionales

    Retorno:
        dict: Diccionario con el nombre y los otros datos adicionales
    """

    ficha = {"nombre": nombre, "datos": datos}
    return ficha


if __name__ == "__main__":
    print(sumar_numeros(0))
    print(sumar_numeros(1))
    print(sumar_numeros(6, 8, 9))
    print(sumar_numeros(*[3, 4, 5]))

    print(crear_ficha("Mika"))
    print(crear_ficha("Higuruma", edad = 28))
    print(crear_ficha("Yuta Okkotsu", clan = "Gojo", hechicero = True))
    print(crear_ficha("Gojo", **{"hechicero": True, "pais": "Japon"}))
