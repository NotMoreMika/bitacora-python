def generar_resumen(titulo,
                    *valores,
                    prefijo="Resultado",
                    mayusculas=False,
                    **metadatos):
    """
    Genera un resumen organizado con titulo, valores y metadatos.

    Parametros:
        titulo (str): Titulo del documento
        *valores: Cantidad variable de numeros
        prefijo (str, opcional): Prefijo del texto. Default "Resultado"
        mayusculas (bool, opcional): Si True, convierte a mayusuculas.
        **metadatos: Datos adicionales

    Retorno
        str: Cadena resumen con el resumen formateado
    """

    lineas = [f"{prefijo}: {titulo}"]

    if valores:
        lineas.append(f"Valores: {list(valores)}")
    else:
        lineas.append(f"No hay valores")

    if metadatos:
        lineas.append(f"Metadatos: {metadatos} ")

    resumen = "\n".join(lineas)

    if mayusculas:
        resumen = resumen.upper()

    return resumen

if __name__ == "__main__":
    print(generar_resumen("Ventas del mes"))
    print(generar_resumen("Calificaciones", 98, 67, 78, 94))
    print(generar_resumen("Altura", 165, 160, 173, 175, prefijo="Chequeo Medico"))
    print(generar_resumen("Altura", 165, 160, 173, 175, prefijo="Chequeo Medico", mayusculas=True))
    print(generar_resumen("Domino", 3, 5, 3, 4, prefijo="Puntos de", equipo=True, jugador_1="Mika"))
    print(generar_resumen("Calificaciones", *[98, 67, 78, 94]))
    print(generar_resumen("Calificaciones", 98, "tres", 78, 94))
