# principal.py
from calculadora_gastos import (
    gasto_total,
    promedio_gasto,
    mayor_gasto,
    menor_gasto,
    generar_informe
)

if __name__ == "__main__":

    # Gastos normales
    gastos_mes = [150.50, 80.00, 230.75, 45.30, 120.00]

    print(f"Gastos del mes: {gastos_mes}")
    print(f"Total:   {gasto_total(gastos_mes):.2f}")
    print(f"Promedio: {promedio_gasto(gastos_mes):.2f}")
    print(f"Mayor:   {mayor_gasto(gastos_mes):.2f}")
    print(f"Menor:   {menor_gasto(gastos_mes):.2f}")

    # Informe completo
    informe = generar_informe(
        titulo="Gastos de octubre 2026",
        gastos=gastos_mes,
        autor="Mika",
        periodo="Mensual",
        moneda="USD"
    )
    print(informe)


    # Informe con solo total y mayor
    informe2 = generar_informe(
        titulo="Gastos personales",
        gastos=[50, 100, 75],
        mostrar_promedio=False,
        mostrar_menor=False
    )
    print(informe2)

    # Lista vacia
    print(generar_informe(titulo="Gastos sin datos", gastos=[]))


    # Entrada invalida
    gastos_invalidos = [100, "mil", 200]

    try:
        total = gasto_total(gastos_invalidos)
        print(f"Total: {total}")
    except TypeError as e:
        print(f"Error de tipo: {e}")

    # Calculo directo
    gastos = [10, 20, 30, 40, 50]
    print(f"Total:   {gasto_total(gastos)}")
    print(f"Promedio: {promedio_gasto(gastos)}")
