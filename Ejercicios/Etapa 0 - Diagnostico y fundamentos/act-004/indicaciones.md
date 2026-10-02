## Objetivo

Demostrar que puedes reconocer la estructura de un problema, identificar el estado que necesitas mantener, convertir el problema en un algoritmo y después implementarlo en Python.

La actividad consolida especialmente:

- patrones de resolución;
- estado acumulado;
- múltiples estados coordinados;
- inicialización y actualización del estado;
- depuración de errores de lógica;
- casos límite y pruebas.

## Preparación

Estudia y comprende antes de comenzar:

- 🧠 Clase — Patrones de resolución y depuración de fundamentos.
- Estado acumulado en bucles y condicionales.

Durante la resolución de los ejercicios, intenta trabajar de forma independiente. No consultes soluciones completas ni utilices IA para resolverlos.

Si olvidas una característica concreta de Python, intenta reconstruirla primero. Si necesitas consultar documentación para desbloquearte, registra qué consultaste.

## Entrega

Guarda la actividad en:

`Ejercicios/Etapa 0 - Diagnostico y fundamentos/act-004/`

Usa `.py` para los ejercicios cuyo objetivo principal sea programar. Usa `.md` cuando un ejercicio pida explicar el razonamiento, el algoritmo, la depuración o los casos límite.

No es necesario terminar toda la actividad en una sola sesión.

---

# Ejercicios

## Ejercicio 1 — Clasificación y conteo

Dada la lista:

```python
numeros = [12, -5, 0, 8, -3, 0, 15, -10]
```

Crea un programa que determine cuántos valores son:

- positivos;
- negativos;
- iguales a cero.

Muestra los tres resultados.

---

## Ejercicio 2 — Total y promedio

Dada la lista:

```python
numeros = [10, 15, 8, 22, 5, 18]
```

Calcula:

1. la suma total;
2. el promedio.

No utilices `sum()`.

El programa debe funcionar recorriendo la lista y manteniendo la información necesaria para obtener ambos resultados.

---

## Ejercicio 3 — Búsqueda

Crea un programa que reciba:

```python
numeros = [7, 12, 4, 19, 3, 12, 8]
objetivo = 19
```

Determina si el valor buscado aparece en la lista.

El resultado debe indicar claramente si fue encontrado o no.

Después cambia el valor de `objetivo` por uno que no aparezca y comprueba el comportamiento.

---

## Ejercicio 4 — Máximo y mínimo

Dada una lista de números, encuentra el valor máximo y el valor mínimo sin utilizar `max()` ni `min()`.

Prueba tu programa al menos con estas listas:

```python
[8, 15, 3, 20, 11]
[-8, -2, -15, -4]
[7, 7, 7, 7]
```

---

## Ejercicio 5 — Filtrado y transformación

Dada la lista:

```python
numeros = [3, 8, 11, 14, 5, 20, 7, 12]
```

Crea una nueva lista que contenga únicamente los números pares, pero almacenados elevados al cuadrado.

El resultado esperado para los datos anteriores es:

```
[64, 196, 400, 144]
```

---

## Ejercicio 6 — Segundo mayor

Dada una lista de números, encuentra el segundo valor más grande sin utilizar `sorted()` ni `max()`.

Prueba como mínimo con:

```python
[10, 12, 8, 25, 139, 32]
[30, 10, 20, 40, 15]
[-5, -2, -10, -1]
```

Antes de programar, explica en un `.md` qué información necesitas conservar mientras recorres la lista y qué debe ocurrir cuando aparece un nuevo máximo.

---

## Ejercicio 7 — Máximo y posición

Dada la lista:

```python
numeros = [14, 7, 25, 9, 31, 18]
```

Encuentra:

1. el valor máximo;
2. la posición en la que aparece por primera vez.

No utilices `max()` ni `index()`.

El resultado debe indicar tanto el valor como su posición.

---

## Ejercicio 8 — Problema combinado

Dada la lista:

```python
numeros = [12, -4, 7, 18, -9, 20, 3, -2, 15]
```

Obtén:

1. la suma de los números positivos;
2. cuántos números negativos existen;
3. el mayor número positivo;
4. una nueva lista con los números positivos mayores que 10.

Primero explica brevemente en un `.md` qué información necesitas mantener durante el recorrido. Después implementa el programa.

---

## Ejercicio 9 — Depuración: estado reiniciado

Analiza el siguiente programa:

```python
numeros = [8, 15, 3, 20, 11]
mayor = 0

for numero in numeros:
    mayor = 0
    if numero > mayor:
        mayor = numero

print(mayor)
```

Determina:

1. qué resultado produce;
2. qué resultado debería producir;
3. qué está ocurriendo con la variable `mayor`;
4. por qué la posición de una determinada línea cambia el comportamiento del programa.

Después corrige el programa y comprueba el resultado.

Conserva en un `.md` la explicación del error y de la corrección.

---

## Ejercicio 10 — Depuración: actualización de estados

El siguiente programa intenta encontrar el mayor y el segundo mayor:

```python
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

Analiza el programa y determina si mantiene correctamente la relación entre `mayor` y `segundo`.

Si encuentras un error:

1. explica qué información se pierde;
2. explica en qué momento ocurre;
3. corrige el programa;
4. comprueba la solución con más de una lista.

No te limites a cambiar la línea que produce el resultado incorrecto: explica la lógica que debe mantenerse entre los dos estados.

---

## Ejercicio 11 — Casos límite

Selecciona al menos **cuatro ejercicios anteriores** y prueba las situaciones que sean relevantes para cada uno.

Considera, cuando corresponda:

- lista vacía;
- un solo elemento;
- dos elementos;
- valores repetidos;
- valores negativos;
- todos los valores iguales;
- datos ordenados de menor a mayor;
- datos ordenados de mayor a menor;
- ausencia del valor buscado;
- aparición del máximo en distintas posiciones.

Para cada caso elegido, indica:

1. qué esperas que ocurra;
2. qué ocurre realmente;
3. si el programa necesita alguna modificación.

---

## Ejercicio 12 — Integración

Diseña y programa un pequeño analizador de una lista de números.

Dada:

```python
numeros = [15, 8, -3, 22, 7, 22, -10, 4, 18, 0]
```

El programa debe obtener:

- cantidad de positivos;
- cantidad de negativos;
- cantidad de ceros;
- suma de los positivos;
- promedio de todos los valores;
- mayor valor;
- menor valor;
- cantidad de veces que aparece el mayor;
- lista de los valores pares.

No utilices `sum()`, `max()` ni `min()`.

Antes de escribir el código, crea un `.md` donde describas qué estados necesitas mantener y cómo se actualizará cada uno durante el recorrido.

---

## Reglas de trabajo

- Puedes estudiar la teoría antes de comenzar.
- Durante la resolución, intenta trabajar sin volver a los apuntes.
- No utilices IA para generar las soluciones.
- Intenta reconstruir la lógica antes de buscar sintaxis.
- Si consultas documentación, registra qué consultaste y por qué.
- Si un ejercicio requiere varios intentos, conserva la solución final y, cuando exista un error relevante, documenta brevemente qué descubriste.
- No es necesario resolver toda la actividad de una sola vez.

## Evidencia que voy a revisar

La revisión se centrará en comprobar si puedes:

- reconocer patrones de resolución a partir de problemas concretos;
- identificar y conservar correctamente el estado;
- inicializar el estado en el lugar adecuado;
- actualizar uno o varios estados sin perder información;
- distinguir entre el valor actual, índices y posiciones cuando el problema lo requiere;
- combinar varios patrones en un mismo algoritmo;
- explicar errores de lógica y no solamente corregirlos;
- anticipar y probar casos límite;
- reconstruir la solución sin depender de una implementación previamente proporcionada.

La actividad se considera evidencia del proceso de aprendizaje, no solamente de si cada programa termina mostrando el resultado esperado.

## Evidencia y GitHub

Las soluciones prácticas deben permanecer en el repositorio indicado en **🔗 FUENTE_VERDAD**.

El tutor puede revisar tu trabajo, pero **no debe modificar, sobrescribir ni eliminar tus archivos**.

La actividad puede resolverse por partes y en varias sesiones.

## Criterio de finalización

La actividad podrá considerarse completada cuando hayas resuelto los ejercicios definidos, guardado la evidencia correspondiente en GitHub y declarado que has terminado.

La revisión del tutor se realizará posteriormente sobre la evidencia disponible.