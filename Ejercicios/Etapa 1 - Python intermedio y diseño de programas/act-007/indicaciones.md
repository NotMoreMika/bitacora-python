**Etapa:** 1 — Python intermedio y diseño de programas  

**Tema:** E1T2 — Alcance y funciones avanzadas  

**Estado:** Pendiente  

**Requisito previo:** estudiar la clase teórica `E1T2_alcance_y_funciones_avanzadas.md` y ejecutar sus ejemplos principales.  

**Entrega:** subir los archivos `.py` a GitHub, dentro de `Ejercicios/Etapa 1 - Python intermedio y diseño de programas/act-007/`. Si necesitas explicar decisiones o registrar incidencias, añade un `.md` en esa carpeta.

## Objetivo

Demostrar que puedes razonar sobre el alcance de los nombres, diseñar funciones reutilizables y utilizar argumentos posicionales, nominales, predeterminados, `*args` y `**kwargs` sin depender de variables globales innecesarias.

## Reglas de trabajo

- Puedes consultar la clase, la documentación oficial de Python y los mensajes de error. No hace falta memorizar de memoria la sintaxis.
- Intenta resolver cada ejercicio antes de mirar soluciones externas. Si consultas algo, anota brevemente qué buscaste y qué aprendiste.
- No avances a ciegas: prueba las funciones con entradas normales, casos límite y llamadas incorrectas cuando corresponda.
- Mantén cada función enfocada en una responsabilidad clara y devuelve resultados con `return` cuando deban usarse después.

## Ejercicio 1 — Alcance local y global

Crea `ejercicio_1_alcance.py`.

1. Define una variable global `descuento = 0.10`.
2. Crea una función `calcular_precio_final(precio)` que use ese descuento y devuelva el precio final.
3. Crea una segunda función que tenga una variable local llamada `descuento` con un valor distinto y demuestra que ese nombre local no modifica la variable global.
4. Prueba ambas funciones y muestra los resultados.
5. Añade comentarios explicando qué nombre se consulta en cada caso.

**Comprobación:** cambia el descuento local y verifica que el global conserva su valor.

## Ejercicio 2 — Detectar y corregir un error de alcance

Crea `ejercicio_2_error_alcance.py`. Incluye una función que intenta leer y después asignar a una variable con el mismo nombre global, provocando un `UnboundLocalError`.

1. Explica por qué ocurre el error.
2. Corrige el diseño sin utilizar `global`: pasa el valor necesario como argumento y devuelve el resultado.
3. Compara las dos versiones en comentarios o en un archivo `incidencias.md`.

No basta con eliminar la línea que falla: explica qué regla del alcance produce el problema.

## Ejercicio 3 — Parámetros, argumentos y valores predeterminados

Crea `ejercicio_3_parametros.py` con una función:

`calcular_total(precio, cantidad=1, descuento=0)`

La función debe devolver el total después de aplicar el descuento. Define claramente si el descuento se representa como una proporción entre 0 y 1.

Prueba al menos:

- una llamada solo con `precio`;
- una llamada con argumentos posicionales;
- una llamada con argumentos nominales;
- una llamada que omita `cantidad` pero indique `descuento`;
- valores límite razonables, incluido un descuento de cero y uno.

Decide cómo tratar precios negativos, cantidades no válidas y descuentos fuera del intervalo permitido. Documenta la decisión y aplícala de forma coherente.

## Ejercicio 4 — El peligro de los valores predeterminados mutables

Crea `ejercicio_4_predeterminado_mutable.py`.

1. Implementa una función que recibe una lista opcional de elementos y añade un elemento.
2. Reproduce el problema de usar una lista vacía como valor predeterminado.
3. Explica por qué dos llamadas pueden compartir la misma lista.
4. Corrige la función utilizando `None` y creando una lista nueva dentro de la función cuando corresponda.
5. Prueba dos llamadas independientes y demuestra que no comparten estado accidentalmente.

## Ejercicio 5 — Cantidad variable de argumentos

Crea `ejercicio_5_args_kwargs.py`.

1. Implementa `sumar_numeros(*args)`, que devuelva la suma de todos los números recibidos.
2. Define qué debe devolver si no recibe argumentos.
3. Implementa `crear_ficha(nombre, **datos)`, que construya y devuelva un diccionario con el nombre y los datos adicionales.
4. Prueba llamadas con cero, uno y varios argumentos para la función de suma, y con diferentes campos para la ficha.
5. Incluye al menos una llamada que desempaquete una lista o tupla con `*` y otra que desempaquete un diccionario con `**`.

## Ejercicio 6 — Diseñar una función con distintos tipos de parámetros

Crea `ejercicio_6_diseno.py`.

Diseña una función `generar_resumen(titulo, *valores, prefijo="Resultado", mayusculas=False, **metadatos)` que:

- reciba un título obligatorio;
- permita recibir cualquier cantidad de valores numéricos;
- permita personalizar el prefijo mediante un argumento nominal;
- permita convertir el texto final a mayúsculas;
- acepte metadatos adicionales;
- devuelva una cadena bien organizada, sin imprimirla desde dentro de la función.

Prueba llamadas que utilicen solo el título, varios valores, opciones nominales y metadatos. Si decides restringir los tipos de los valores, valida esa regla y explica tu decisión.

## Ejercicio 7 — Cierre e independencia de funciones

Crea `ejercicio_7_diseno_funciones.py`.

Implementa `crear_multiplicador(factor)`, que devuelva una función capaz de multiplicar un número por ese factor. Debes poder crear dos multiplicadores con factores distintos y usarlos de forma independiente.

Explica con tus palabras qué valor conserva cada función devuelta y por qué no necesitas una variable global para almacenar el factor.

## Ejercicio 8 — Integración: calculadora de gastos configurable

Crea una pequeña solución distribuida en archivos:

- `calculadora_gastos.py`: funciones de cálculo y construcción del informe.
- `principal.py`: interacción mínima o pruebas de ejemplo.

Requisitos:

1. Implementa una función que reciba una lista de gastos y devuelva el total.
2. Implementa una función para calcular el promedio; decide y documenta qué ocurre con una lista vacía.
3. Implementa una función que genere un resumen configurable mediante argumentos nominales y valores predeterminados.
4. Utiliza `*args` o `**kwargs` donde tenga sentido real; no los añadas solo para cumplir una formalidad.
5. Evita que las funciones de cálculo dependan de variables globales modificables.
6. Mantén separadas la lógica de cálculo y la presentación.
7. Protege el punto de entrada con `if __name__ == "__main__":` en `principal.py`.
8. Prueba los casos normales, la lista vacía y al menos una entrada inválida.

## Revisión final antes de entregar

- [ ]  Distingo parámetros de argumentos y sé cuándo usar argumentos nominales.
- [ ]  Puedo explicar el alcance local y global y diagnosticar `UnboundLocalError`.
- [ ]  Entiendo por qué los valores predeterminados se evalúan una vez y evito listas o diccionarios mutables predeterminados por accidente.
- [ ]  Sé usar `*args`, `**kwargs` y desempaquetar argumentos.
- [ ]  Las funciones devuelven resultados en lugar de imprimirlos cuando estos se necesitan en otros cálculos.
- [ ]  Probé casos normales y límite, y documenté las decisiones importantes.
- [ ]  La solución integrada está organizada y se ejecuta correctamente.

**Criterio de revisión:** se valorará la comprensión y el razonamiento, no la ausencia absoluta de consultas. En la revisión comprobaremos especialmente el alcance, los valores predeterminados mutables, el uso correcto de argumentos y la claridad del diseño.