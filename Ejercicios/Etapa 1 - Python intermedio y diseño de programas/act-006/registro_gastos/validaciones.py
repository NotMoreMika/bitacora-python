def validar_lista(lista):
    if len(lista) > 0:
        return True
    else:
        return False

# Solo vamos a descartar listas vacias
# Listas con 1 numero o todos iguales no afectan la logica
# No vamos a complicar la validacion asegurando que todos los valores sean numericos
