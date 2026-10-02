# Respuesta

Para el sgte programa:

```
numeros = [8, 15, 3, 20, 11]
mayor = 0

for numero in numeros:
    mayor = 0
    if numero > mayor:
        mayor = numero

print(mayor)
```
El resultado que produce es 11.
El resultado esperado es 20.
La variable  mayor se esta reiniciando a 0 en cada iteracion del bucle for.
La posición de una línea importa porque define el cuándo: cuándo se inicializa, cuándo se actualiza y cuándo se usa. Si lo que debe pasar una sola vez lo pones dentro del loop, se ejecuta muchas veces. Si lo que debe pasar muchas veces lo pones fuera, no se ejecuta nunca.

```
numeros = [8, 15, 3, 20, 11]
mayor = 0

for numero in numeros:
    if numero > mayor:
        mayor = numero

print(mayor)
```

El error se debe a la inicializacion de la variable dentro del loop, cuando esta solo deberia inicializarse una vez fuera del loop
