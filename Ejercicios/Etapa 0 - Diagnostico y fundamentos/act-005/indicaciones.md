## 🎯 Propósito

Esta es la **evaluación de cierre de la Etapa 0**.

No pretende comprobar si recuerdas de memoria cada método de Python. Pretende comprobar si puedes **leer un problema, decidir cómo resolverlo, escribir una solución y detectar errores cuando aparezcan**.

> **Regla principal:** durante los ejercicios no se te indicará qué patrón, estructura o estrategia debes utilizar. Esa decisión forma parte de la evaluación.
> 

## 📌 Reglas

- Trabaja en Python.
- Puedes consultar la documentación oficial de Python cuando necesites confirmar **sintaxis o funcionamiento de una característica concreta**.
- No consultes soluciones completas ni busques cómo resolver específicamente el ejercicio.
- Puedes usar VS Code y su autocompletado.
- Si un ejercicio no exige una técnica concreta, elige tú la solución.
- Si haces una suposición sobre un caso límite, indícala en tu explicación.
- Guarda las respuestas en GitHub dentro de:
    
    `Ejercicios/Etapa 0 - Diagnostico y fundamentos/act-005/`
    

## 🧪 BLOQUE 1 — Fundamentos

### Ejercicio 1 — Clasificación

Crea un programa que reciba una lista de valores numéricos y muestre:

- cuántos son positivos;
- cuántos son negativos;
- cuántos son cero;
- la suma total de los valores.

Prueba el programa con varios casos, incluido uno que contenga únicamente ceros.

**Entrega:** código y una explicación breve de cómo decidiste resolverlo.

### Ejercicio 2 — Transformación

Dada una lista de números, crea otra lista que contenga únicamente los números que sean pares, pero elevados al cuadrado.

Ejemplo:

`[1, 2, 3, 4, 5, 6] → [4, 16, 36]`

Incluye una prueba con una lista vacía.

## 🧠 BLOQUE 2 — Razonamiento algorítmico

### Ejercicio 3 — Análisis de una lista

Dada una lista de números, determina:

- el valor mayor;
- el valor menor;
- la posición del mayor;
- cuántas veces aparece el mayor.

No utilices `max()`, `min()` ni `count()`.

Explica qué valores necesitas mantener mientras recorres la lista.

**Caso límite obligatorio:** decide qué debe ocurrir si la lista está vacía y documenta tu decisión.

### Ejercicio 4 — Búsqueda con condición

Dada una lista de números y un objetivo, determina si existe algún número que cumpla simultáneamente estas dos condiciones:

1. es mayor que el objetivo;
2. es par.

El programa debe indicar si existe y, si existe, mostrar uno de los valores que cumple la condición.

Prueba también una lista donde ningún valor cumpla ambas condiciones.

## 🔧 BLOQUE 3 — Funciones y estructuras

### Ejercicio 5 — Función de análisis

Crea una función que reciba una lista de números y devuelva información suficiente para conocer:

- suma de positivos;
- cantidad de negativos;
- mayor valor;
- menor valor.

Decide tú qué estructura devolverá la función.

Prueba la función con:

- números positivos y negativos;
- todos los números positivos;
- todos los números negativos;
- una lista vacía.

Explica qué decisión tomaste para la lista vacía.

### Ejercicio 6 — Diccionario

Crea un programa que reciba una lista de palabras y construya un diccionario donde cada palabra sea una clave y su valor indique cuántas veces aparece.

Ejemplo:

`["python", "js", "python", "css", "js", "python"]`

debe producir un resultado equivalente a:

`{"python": 3, "js": 2, "css": 1}`

No es necesario conservar un orden específico.

## 🐛 BLOQUE 4 — Depuración

### Ejercicio 7 — Encuentra el error

El siguiente código pretende encontrar el mayor número de una lista:

```python
numeros = [12, 5, 28, 7, 19]

mayor = 0

for numero in numeros:
    mayor = 0

    if numero > mayor:
        mayor = numero

print(mayor)
```

1. Explica por qué el programa no funciona correctamente.
2. Corrígelo.
3. Explica **qué estado se estaba perdiendo y en qué momento se reiniciaba**.

No basta con entregar el código corregido.

## 🧩 BLOQUE 5 — Integración

### Ejercicio 8 — Problema completo

Escribe un programa que analice una lista de números y produzca un pequeño informe.

El informe debe indicar:

- cantidad de números;
- suma total;
- promedio;
- mayor;
- menor;
- cantidad de números pares;
- cantidad de números impares.

Debes decidir cómo organizar el programa.

**Condición:** intenta resolver el análisis recorriendo la lista una sola vez.

Si decides no hacerlo de una sola pasada, explica por qué.

Incluye una prueba con una lista normal y otra con una lista vacía.

## 📝 BLOQUE 6 — Explicación

### Ejercicio 9 — Explica tu estrategia

Elige **uno** de los ejercicios 3, 5 u 8 y explica con tus propias palabras:

1. qué información necesitabas mantener;
2. qué valores se inicializan antes del recorrido;
3. qué cambia dentro del recorrido;
4. qué ocurre cuando aparece un valor que cambia el resultado;
5. qué casos límite consideraste.

No busco una explicación académica. Quiero comprobar que puedes explicar el razonamiento que hay detrás de tu código.

## 🧠 BLOQUE 7 — Reto final

### Ejercicio 10 — Sin indicación de patrón

Dada una lista de números, crea un programa que determine cuál es el **segundo valor más grande distinto del mayor**.

Ejemplo:

`[10, 25, 8, 25, 17, 3] → 17`

El mayor es 25 y el segundo mayor distinto es 17.

Considera y documenta qué debe ocurrir en estos casos:

- lista vacía;
- un solo elemento;
- todos los elementos iguales;
- solo existe un valor distinto.

**Importante:** aquí no se te proporciona el algoritmo. Debes decidir cómo mantener la información necesaria.

## ✅ Criterio general de la evaluación

La evaluación no exige que todo sea perfecto a la primera. Se valorará especialmente:

- comprensión de variables y tipos;
- uso correcto de condicionales y bucles;
- manejo de listas y diccionarios;
- creación y uso de funciones;
- capacidad para mantener estados durante un recorrido;
- elección autónoma de una estrategia;
- detección y corrección de errores lógicos;
- consideración de casos límite;
- capacidad de explicar el razonamiento.

### 🚦 Para cerrar la Etapa 0

ACT-005 será revisada como una evaluación global.

**Superar un ejercicio aislado no determina el resultado final.** Se observará el conjunto de evidencias y, especialmente, si puedes resolver problemas fundamentales sin que se te indique previamente qué patrón aplicar.

Si la evaluación confirma los objetivos del ROADMAP, podremos cerrar formalmente la **Etapa 0** y pasar a la **Etapa 1**.

## 📦 Entrega

Crea:

`Ejercicios/Etapa 0 - Diagnostico y fundamentos/act-005/`

Puedes utilizar una estructura como:

`resp-1.py`  

`resp-2.py`  

...  

`resp-10.py`

Cuando sea necesario explicar decisiones, puedes utilizar archivos `.md` asociados.

**No necesitas esperar a terminar todo para preguntarme una duda conceptual**, pero durante la evaluación no te indicaré qué patrón aplicar a un ejercicio, porque precisamente eso forma parte de lo que estamos evaluando.