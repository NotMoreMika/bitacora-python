def clasificar_numero(numero):
    if numero > 0:
        print("positivo")
    elif numero < 0:
        print("negativo")
    else:
        print("cero")

def puede_acceder(edad, tiene_permiso):
    if edad >= 18 or tiene_permiso == True:
        print("Puede acceder")
    else:
        print("No puede acceder")

clasificar_numero(8)
clasificar_numero(-8)
clasificar_numero(3.2)
clasificar_numero(0)

puede_acceder(5, False)
puede_acceder(18, False)
puede_acceder(5, True)
puede_acceder(18, True)

