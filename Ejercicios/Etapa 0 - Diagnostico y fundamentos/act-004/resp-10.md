# Respuesta

Para el sgte programa:

```py
numeros = [10, 25, 8, 40, 17]

mayor = numeros[0]
segundo = numeros[1]

for numero in numeros[2:]:
    if numero > mayor:
        mayor = numero
        segundo = numero
    elif numero > segundo:
        segundo = numero

print("Mayor:", mayor)
print("Segundo:", segundo)
```

La relacion entre el mayor y el segundo no se mantiene correctamente.

1. Se pierde el valor del segundo.
1. Cuando un numero es mayor que el mayor.
1. La correcion seria asi:

```py
numeros = [10, 25, 8, 40, 17]

mayor = numeros[0]
segundo = numeros[1]

if mayor < segundo:
    mayor = numeros[1]
    segundo = numeros[0]

for numero in numeros[2:]:
    if numero > mayor:
        segundo = mayor
        mayor = numero
    elif numero > segundo:
        segundo = numero

print("Mayor:", mayor)
print("Segundo:", segundo)
```
La solucion deberia funcionar en mas de una lista, exceptuando listas vacias o con un solo numero.

Ademas de la correcion dentro de la condicional que esta dentro del bucle. Hay que corregir la relacion entre el mayor y el segundo, ya que cuando se declaran sus valores iniciales se desconoce quien es el mayor, por eso hay que hacer un comprobacion con una condicional para que corrija sus valores.
