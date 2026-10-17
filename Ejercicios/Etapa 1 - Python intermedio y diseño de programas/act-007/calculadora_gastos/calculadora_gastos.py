def gasto_total(gastos):
    """
    Calcula el total de una lista de gastos.

    Parametros:
        gastos (list): Lista de gastos numericos.

    Retorno:
        float: Suma de todos los gastos.

    Raises:
        TypeError: Si algun elemento no es numerico.
        ValueError: Si la lista esta vacia.
    """
    if not gastos:
        raise ValueError("La lista de gastos no puede estar vacia")

    for i, gasto in enumerate(gastos):
        if not isinstance(gasto, (int, float)) or isinstance(gasto, bool):
            raise TypeError(
                f"Todos los gastos deben ser numericos. "
                f"Elemento en posicion {i} es {type(gasto).__name__}: {gasto}"
            )

    return sum(gastos)


def promedio_gasto(gastos):
    """
    Calcula el promedio de una lista de gastos.

    Decisión sobre lista vacia:
        Se lanza ValueError porque no existe un promedio matematico
        valido para cero elementos. Es mejor fallar con un error
        claro que devolver 0 (que podria confundirse con un promedio real).

    Parametros:
        gastos (list): Lista de gastos numericos.

    Retorno:
        float: Promedio de los gastos.

    Raises:
        TypeError: Si algun elemento no es numerico.
        ValueError: Si la lista esta vacia.
    """
    if not gastos:
        raise ValueError(
            "No se puede calcular el promedio de una lista vacia"
        )

    for i, gasto in enumerate(gastos):
        if not isinstance(gasto, (int, float)) or isinstance(gasto, bool):
            raise TypeError(
                f"Todos los gastos deben ser numericos. "
                f"Elemento en posicion {i} es {type(gasto).__name__}: {gasto}"
            )

    return sum(gastos) / len(gastos)


def mayor_gasto(gastos):
    """
    Encuentra el gasto mas alto de la lista.

    Parametros:
        gastos (list): Lista de gastos numericos.

    Retorno:
        float: El gasto mas alto.

    Raises:
        ValueError: Si la lista esta vacia.
    """
    if not gastos:
        raise ValueError("La lista de gastos no puede estar vacia")
    return max(gastos)


def menor_gasto(gastos):
    """
    Encuentra el gasto mas bajo de la lista.

    Parametros:
        gastos (list): Lista de gastos numericos.

    Retorno:
        float: El gasto mas bajo.

    Raises:
        ValueError: Si la lista esta vacia.
    """
    if not gastos:
        raise ValueError("La lista de gastos no puede estar vacia")
    return min(gastos)


def generar_informe(
    titulo="Resumen de gastos",
    gastos=None,
    *,
    mostrar_total=True,
    mostrar_promedio=True,
    mostrar_mayor=True,
    mostrar_menor=True,
    **datos
):
    """
    Genera un informe de gastos con opciones configurables.

    Parametros:
        titulo (str, opcional): Titulo del informe. Default "Resumen de gastos".
        gastos (list, opcional): Lista de gastos. Si es None, se considera vacia.
        mostrar_total (bool, opcional): Mostrar el total. Default True.
        mostrar_promedio (bool, opcional): Mostrar el promedio. Default True.
        mostrar_mayor (bool, opcional): Mostrar el mayor gasto. Default True.
        mostrar_menor (bool, opcional): Mostrar el menor gasto. Default True.
        **datos: Metadatos adicionales (autor, fecha, etc.).

    Retorno:
        str: Informe formateado.
    """
    if gastos is None:
        gastos = []

    lineas = [f"=== {titulo} ===", ""]

    if not gastos:
        lineas.append("No hay gastos registrados.")
    else:
        if mostrar_total:
            lineas.append(f"Total de gastos:  {gasto_total(gastos):.2f}")
        if mostrar_promedio:
            lineas.append(f"Promedio:         {promedio_gasto(gastos):.2f}")
        if mostrar_mayor:
            lineas.append(f"Gasto mayor:      {mayor_gasto(gastos):.2f}")
        if mostrar_menor:
            lineas.append(f"Gasto menor:      {menor_gasto(gastos):.2f}")

        lineas.append(f"Cantidad:         {len(gastos)}")

    if datos:
        lineas.append("")
        lineas.append("Metadatos:")
        for clave, valor in datos.items():
            lineas.append(f"  {clave}: {valor}")

    return "\n".join(lineas)
