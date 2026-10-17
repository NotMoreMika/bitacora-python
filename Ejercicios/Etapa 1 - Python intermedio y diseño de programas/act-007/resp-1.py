descuento = 0.10 # Global

def calcular_precio_final(precio):
    precio_final = precio * (1 - descuento)
    return precio_final

def calcular_precio(precio):
    descuento = 0.35 # Local
    precio_final = precio - descuento
    return precio_final

# Usa la variable global
print(calcular_precio_final(9)) # 8.9
# Usa la variable local
print(calcular_precio(9)) # 8.65

# El resultado es diferente en ambas funciones por el ambito de descuento
