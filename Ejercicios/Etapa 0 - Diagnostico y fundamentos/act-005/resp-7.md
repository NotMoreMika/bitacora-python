# Respuesta

Para el sgte programa:

```python
numeros = [12, 5, 28, 7, 19]

mayor = 0

for numero in numeros:
    mayor = 0

    if numero > mayor:
        mayor = numero

print(mayor)
```

El error del programa era que se estaba reiniciando el estado en cada llamada del loop

La version corregida seria asi:

```python
numeros = [12, 5, 28, 7, 19]

mayor = 0

for numero in numeros:

    if numero > mayor:
        mayor = numero

print(mayor)
```

El estado se estaba perdiendo porque se inicializaba 2 veces una fuera del loop y otra dentro del loop. La del loop asignaba a 0 el valor de la variable en cada vuelta perdiendose los valores anteriores.
