nivel = 1

# def lvl_up():
def lvl_up(nivel):
    nivel += 1
    print(nivel)

# lvl_up()
lvl_up(nivel)


# El error ocurre porque Python tratra como local el nombre al que se asigna dentro de una función
# Las lineas comentadas son las que causan el error
# La diferencia esta en el scope de la variable
