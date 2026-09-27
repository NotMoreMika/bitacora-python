## Objetivo

Consolidar fundamentos de Python y comprobar que puedes combinar tipos de datos, strings, listas, diccionarios, operadores, condicionales y recorridos en pequeños problemas.

## Preparación

Lee **Repaso inicial — Fundamentos de Python** antes de comenzar. Después ciérralo y resuelve por tu cuenta.

En esta actividad quiero priorizar tu capacidad de recordar y aplicar. **No busques soluciones completas en Internet ni uses IA para resolver los ejercicios.** Si un ejercicio te obliga a consultar documentación porque olvidaste un método o una función, puedes hacerlo cuando la actividad lo indique y anota qué consultaste.

## Entrega

Guarda la actividad en:

`Ejercicios/Etapa 0 - Diagnostico y fundamentos/act-003/`

Usa `.py` para ejercicios cuyo objetivo principal sea escribir código. Usa `.md` cuando se pida explicar razonamiento o comportamiento.

---

## Parte 1 — Tipos y conversiones

Crea variables para representar:

- un nombre;
- una edad;
- una altura con decimales;
- si una persona está activa;
- un valor que represente ausencia de información.

Imprime cada valor junto con su tipo utilizando `type()`.

Después:

1. Convierte `"25"` a entero.
2. Convierte `25` a string.
3. Convierte `"3.14"` a `float`.
4. Explica brevemente en un `.md` qué diferencia hay entre `"25"` y `25`.

---

## Parte 2 — Strings

Trabaja con:

```python
texto = "  Python es divertido  "
```

Crea código que:

1. elimine los espacios exteriores;
2. convierta el texto a mayúsculas;
3. convierta el texto a minúsculas;
4. obtenga su longitud;
5. compruebe si contiene la palabra `"Python"`;
6. reemplace `"divertido"` por `"poderoso"`.

No necesitas memorizar los métodos: intenta recordar primero. Si después de intentarlo necesitas consultar la documentación oficial, **esta vez está permitido**. Registra en un `.md` qué consultaste.

---

## Parte 3 — Listas

Crea:

```python
numeros = [10, 25, 7, 40, 15]
```

Realiza las siguientes operaciones:

1. imprime la cantidad de elementos;
2. imprime el primer elemento;
3. imprime el último elemento usando índice negativo;
4. agrega `50` al final;
5. inserta `5` al principio;
6. elimina `25` por su valor;
7. extrae y guarda el último elemento usando un método de lista;
8. ordena la lista de menor a mayor;
9. crea una copia de la lista y demuestra que es una lista independiente.

**Importante:** intenta recordar los métodos antes de consultar documentación.

---

## Parte 4 — Condiciones

Escribe una función `clasificar_numero(numero)` que:

- devuelva `"positivo"` si es mayor que 0;
- devuelva `"negativo"` si es menor que 0;
- devuelva `"cero"` si es igual a 0.

Después crea otra función `puede_acceder(edad, tiene_permiso)` que devuelva `True` si la persona tiene al menos 18 años **o** tiene permiso, y `False` en caso contrario.

Prueba ambas funciones con varios casos.

---

## Parte 5 — Recorridos

Dada:

```python
numeros = [3, 8, 12, 5, 7, 20]
```

Crea un programa que recorra la lista y:

1. imprima solamente los números mayores que 10;
2. cuente cuántos números son pares;
3. calcule la suma de todos los números sin utilizar `sum()`.

En una explicación breve, indica cuándo utilizarías:

```python
for numero in numeros
```

frente a:

```python
for indice in range(len(numeros))
```

---

## Parte 6 — Diccionarios

Crea un diccionario que represente a una persona:

```python
persona = {
    "nombre": "Mika",
    "edad": 0,
    "lenguaje": "Python"
}
```

Después:

1. accede al nombre;
2. modifica la edad;
3. agrega una clave `"activo"`;
4. elimina una clave que tú elijas;
5. recorre el diccionario mostrando claves y valores;
6. comprueba si existe una clave concreta antes de intentar acceder a ella.

---

## Parte 7 — Mezcla de conceptos

Crea una lista de diccionarios que represente varios usuarios. Por ejemplo:

```python
usuarios = [
    {"nombre": "Ana", "edad": 25, "activo": True},
    {"nombre": "Luis", "edad": 16, "activo": False},
    {"nombre": "Carlos", "edad": 32, "activo": True}
]
```

Recorre la lista y muestra solamente los usuarios que sean mayores de edad y estén activos.

Después crea una función `contar_activos(usuarios)` que devuelva cuántos usuarios tienen `"activo"` en `True`.

---

## Parte 8 — Razonamiento algorítmico

Sin escribir código al principio, explica paso a paso cómo resolverías:

> Recibes una lista de números. Debes encontrar el segundo número más grande sin utilizar `sorted()` ni `max()`.
> 

Después, si te sientes preparado, implementa tu algoritmo en Python.

No importa si necesitas varios intentos. Lo que interesa aquí es observar cómo transformas un problema en pasos antes de programarlo.

---

## Parte 9 — Mini-reto

Crea un pequeño programa que gestione una lista de compras.

Debe permitir que exista una lista como:

```python
compras = ["pan", "leche", "huevos"]
```

El programa debe:

1. mostrar los productos actuales;
2. agregar un producto;
3. eliminar un producto si existe;
4. mostrar cuántos productos quedan;
5. indicar si un producto concreto está en la lista.

No necesitas crear un menú interactivo ni utilizar conceptos que todavía no hayamos estudiado. El objetivo es combinar correctamente listas, `if`, `in`, métodos y funciones si decides utilizarlas.

---

## Parte 10 — Investigación controlada

Ahora sí quiero que practiques una habilidad que utilizaremos durante todo el aprendizaje: **consultar documentación oficial**.

Elige **tres** funciones o métodos de los utilizados en esta actividad que no recuerdes con seguridad.

Consulta la documentación oficial de Python y registra en un `.md`:

- qué buscaste;
- dónde lo encontraste;
- qué aprendiste;
- un ejemplo propio que demuestre que lo entendiste.

No copies una solución completa de otra persona. La consulta debe servir para recuperar información concreta.

---

## Reglas de la actividad

- Puedes leer los apuntes antes de empezar.
- Cierra los apuntes durante la resolución.
- Primero intenta recordar; después consulta documentación cuando esté permitido.
- No utilices IA para generar las soluciones.
- Si un ejercicio requiere varios intentos, conserva el resultado final y, si hubo un error interesante, puedes conservar también una breve nota sobre él.
- No busques escribir código sofisticado. Queremos comprobar fundamentos.

## Evidencia que voy a evaluar

- comprensión de tipos y conversiones;
- manejo de strings;
- longitud, índices y métodos de listas;
- diferencia entre elemento e índice;
- condicionales y operadores lógicos;
- recorridos con `for`;
- diccionarios;
- combinación de estructuras de datos;
- funciones;
- capacidad para convertir razonamiento algorítmico en código;
- capacidad de consultar documentación para resolver una duda concreta.

La actividad es deliberadamente amplia. No necesitas resolverla toda de una sola sesión; puedes avanzar por partes según tu disponibilidad.