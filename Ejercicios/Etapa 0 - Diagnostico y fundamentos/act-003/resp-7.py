usuarios = [
    {"nombre": "Sukuna", "edad": 400, "activo": True},
    {"nombre": "Gojo", "edad": 25, "activo": False},
    {"nombre": "Higuruma", "edad": 28, "activo": True},
    {"nombre": "Luffy", "edad": 16, "activo": True}
]

for usuario in usuarios:
    if usuario["edad"] >= 18 and usuario["activo"] == True:
        print(usuario["nombre"])

def contar_activos(usuarios):
    usuarios_activos = 0
    for usuario in usuarios:
        if usuario["activo"] == True:
            usuarios_activos += 1
    print(usuarios_activos)

contar_activos(usuarios)
