def añadir_fruta(frutas: list | None = None) -> list:
    """
    Añade una fruta a una lista.

    Parametros:
        frutas (list, opcional): Lista de frutas. Si no se pasa, se crea una nueva.

    Retorno:
        list: Lista con la fruta añadida.
    """

    if frutas is None:
        frutas = []

    frutas.append("guayaba")
    return frutas


def añadir_fruta_mal(frutas: list = []) -> list:
    frutas.append("guayaba")
    return frutas

if __name__ == "__main__":

    resultado1 = añadir_fruta_mal()
    print(resultado1)

    resultado2 = añadir_fruta_mal()
    print(resultado2)

    """
    El valor por defecto [] se evalúa UNA SOLA VEZ cuando Python
    define la función. NO se crea una lista nueva en cada llamada.
    Todas las llamadas que no pasen argumento usarán LA MISMA lista.
    Por eso se acumulan los 'guayaba' entre llamadas.
    """
    nueva1 = añadir_fruta()
    print(nueva1)
    nueva2 = añadir_fruta()
    print(nueva2)

    # Aqui podemos comprobar que nueva1 no comparte estado con nueva2

    frutas1 = ["mango", "pera"]
    print(añadir_fruta(frutas1))
