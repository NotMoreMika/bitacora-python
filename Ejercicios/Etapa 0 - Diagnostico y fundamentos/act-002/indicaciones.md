## Objetivo

Recuperar fluidez con variables, comparaciones, `range()`, listas, funciones y sintaxis básica sin depender de los apuntes durante la resolución.

## Preparación

Lee primero **Repaso inicial — Fundamentos de Python**. Después cierra los apuntes y resuelve la actividad por tu cuenta.

## Entrega

Guarda esta actividad en:

`Ejercicios/Etapa 0 - Diagnostico y fundamentos/act-002/`

Puedes conservar la misma idea de organización que utilizaste en `act-001`.

## Parte 1 — Predicción

Sin ejecutar el código, indica qué se imprimirá y explica por qué:

```python
numero = 3

for i in range(1, 5):
    print(numero + i)
```

## Parte 2 — Listas

Dada esta lista:

```python
usuarios = ["Mika", "Ana", "Carlos"]
```

1. Obtén el primer elemento.
2. Obtén el último elemento usando un índice negativo.
3. Agrega `"Luis"` al final.
4. Después de agregarlo, obtén `"Luis"` mediante su índice.

No copies los ejemplos de los apuntes; intenta escribirlos de memoria.

## Parte 3 — Función

Escribe una función:

```python
def es_par(numero):
    ...
```

Debe devolver `True` cuando el número sea par y `False` cuando sea impar.

Después demuestra su funcionamiento con al menos dos llamadas: una con un número par y otra con un número impar.

## Parte 4 — Función + lista + bucle

Escribe una función llamada `contar_pares(numeros)` que reciba una lista de números y devuelva cuántos de ellos son pares.

Ejemplo de comportamiento esperado:

```
contar_pares([1, 2, 4, 7, 9, 10]) -> 3
```

Intenta construirla utilizando los conceptos repasados, sin utilizar funciones avanzadas que hagan todo el trabajo automáticamente.

## Parte 5 — Razonamiento

Explica con tus palabras cómo resolverías este problema antes de escribir código:

> Recibes una lista de números. Debes obtener el número más pequeño sin utilizar `min()`.
> 

Describe los pasos del algoritmo.

## Parte 6 — Código completo

Crea un pequeño programa que:

1. Tenga una lista de números.
2. Recorra la lista.
3. Imprima solamente los números pares.

No es necesario crear una función para esta parte.

## Reglas

- Puedes consultar los apuntes **antes** de comenzar.
- No consultes la solución de la actividad mientras la resuelves.
- No utilices IA para generar las respuestas.
- Si olvidas una sintaxis, intenta reconstruirla primero.
- Si después necesitas consultar documentación para desbloquearte, anota qué tuviste que consultar.
- No busques que el código quede perfecto: queremos observar qué recuerdas y dónde aparecen los errores.

## Evidencia esperada

La revisión evaluará especialmente:

- comprensión de índices y listas;
- uso de `range()` y límites;
- comparación mediante `==`;
- uso del operador `%`;
- definición y llamada de funciones;
- `return`;
- bucles;
- indentación y `:`;
- capacidad para convertir un algoritmo sencillo en código Python.

La actividad no se califica solamente por cantidad de respuestas correctas. Los errores y las dificultades también son evidencia útil para adaptar el siguiente paso.