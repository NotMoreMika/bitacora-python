persona = {
    "name": "Higuruma",
    "edad": 28,
    "lenguaje": "Python"
}

persona["name"]
persona["edad"] = 30
persona["activo"] = True
persona.pop("lenguaje")

for i in persona.keys():
    print(i, persona.get(i))

if persona.get("edad"):
    print(persona.get("edad"))
else:
    print("No existe esa clave")
