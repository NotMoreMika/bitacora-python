import calculos
import validaciones

gasto1 = [3000, 750, 2300, 1500]
gasto2 = []

def main(gastos):
    gasto_promedio = 0
    gasto_total = 0

    if validaciones.validar_lista(gastos):
        gasto_total = calculos.calcular_total(gastos)
        gasto_promedio = calculos.promedio(gastos)
    else:
        print("No hay gastos registrados todavía")
        return

    print(f"=====Informe=====\nEl gasto total es de {gasto_total} \nEl promedio de gastos es de {gasto_promedio}")

if __name__ == "__main__":
    main(gasto1)
    main(gasto2)
