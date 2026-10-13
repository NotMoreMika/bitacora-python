# Clase 1 de la Etapa 1 — Modularidad en Python
## Módulos, importaciones, paquetes y organización de programas

**Proyecto:** Bitácora Python  
**Etapa:** 1 — Python intermedio y diseño de programas  
**Objetivo:** aprender a dividir un programa en archivos con responsabilidades claras, reutilizar código mediante importaciones y comprender cómo Python carga y encuentra los módulos.

## Cómo estudiar esta clase

No intentes memorizarlo todo en una sola lectura. Lee cada sección, ejecuta los ejemplos en VS Code y cambia algunos valores para comprobar que entiendes qué ocurre. Al final encontrarás una autoevaluación. Esta clase es material de estudio, no una actividad evaluativa ni una entrega.

## 1. De los ejercicios aislados a los programas organizados

Hasta ahora muchos ejercicios podían resolverse en un solo archivo. Eso es útil al aprender, porque permite seguir el algoritmo de principio a fin. Pero un programa que administra gastos podría necesitar pedir datos, validarlos, calcular totales, guardar información y generar informes. Si toda esa lógica termina mezclada en un archivo enorme, cuesta encontrar funciones, modificar reglas y localizar errores.

La **modularidad** consiste en dividir el código en piezas con propósitos definidos que colaboran entre sí. Por ejemplo, un módulo puede contener cálculos, otro validaciones y un archivo principal puede coordinar el programa.

Sus beneficios son:
- **Legibilidad:** es más fácil encontrar dónde se hace cada cosa.
- **Reutilización:** podemos utilizar una función sin copiarla a otros archivos.
- **Mantenimiento:** los cambios quedan más localizados.
- **Pruebas y depuración:** es más fácil comprobar una parte de forma aislada.

Dividir no significa crear tantos archivos como sea posible. La separación debe aportar claridad; dividir un programa diminuto en muchos módulos puede añadir complejidad innecesaria.

## 2. ¿Qué es un módulo?

Un **módulo** es una unidad de código importable. En los ejemplos habituales, es un archivo con extensión `.py`. Puede contener funciones, variables, clases, importaciones y también instrucciones que se ejecutan cuando se carga.

Imagina esta estructura:

```text
calculadora/
├── principal.py
└── operaciones.py
```

El archivo `operaciones.py`:

```python
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def es_par(numero):
    return numero % 2 == 0
```

El nombre que utilizamos al importar es `operaciones`, sin la extensión `.py`.

Un módulo suele reunir herramientas relacionadas. Usa nombres claros y evita nombrar tus archivos `random.py`, `json.py` o `math.py` si pretendes importar esos módulos de la biblioteca estándar: tu archivo podría interferir con el módulo esperado.

## 3. ¿Qué significa importar?

Una importación permite que un archivo utilice código definido en otro módulo. En `principal.py`:

```python
import operaciones

resultado = operaciones.sumar(8, 5)
print(resultado)
print(operaciones.es_par(10))
```

En `operaciones.sumar(8, 5)`:
- `operaciones` es el módulo;
- `sumar` es una función definida en él;
- `8` y `5` son los argumentos que recibe la función.

El prefijo `operaciones.` deja claro de dónde procede la función. Esto ayuda especialmente si hay funciones con nombres iguales en módulos distintos.

## 4. Tres formas habituales de importar

### A. Importar el módulo

```python
import operaciones

total = operaciones.sumar(4, 6)
print(total)
```

El origen del nombre queda visible. Es una buena opción inicial porque facilita leer el código.

### B. Importar nombres concretos

```python
from operaciones import sumar, restar

print(sumar(4, 6))
print(restar(10, 3))
```

Puedes usar directamente los nombres importados. Es cómodo si importas pocos nombres y el origen sigue claro. La desventaja es que, al leer `sumar(...)`, no se ve el módulo en esa línea.

### C. Importar con un alias

```python
import operaciones as ops

print(ops.sumar(4, 6))
```

`as ops` asigna un alias al módulo. Usa alias comprensibles; una abreviatura críptica hace el código más difícil de leer.

No acostumbres a usar `from operaciones import *`. Importa nombres sin enumerarlos y dificulta saber de dónde procede cada nombre.

**Regla inicial:** usa `import modulo` cuando el prefijo aporte claridad; usa `from modulo import nombre` cuando importes pocos nombres y la lectura siga siendo clara.

## 5. Importar también puede ejecutar código

Este punto es fundamental. Al importar un módulo, Python ejecuta sus instrucciones de nivel superior durante la carga. Las definiciones de funciones quedan disponibles, pero otras instrucciones que estén fuera de las funciones también pueden ejecutarse.

Por ejemplo, `informe.py`:

```python
print("Preparando informe...")

def calcular_total(valores):
    return sum(valores)
```

Si otro archivo importa `informe`, el mensaje se muestra aunque solo quiera reutilizar `calcular_total()`. Si el módulo pidiera datos o modificara archivos automáticamente, el efecto podría ser más serio.

Es preferible encapsular las acciones:

```python
def preparar_informe():
    print("Preparando informe...")

def calcular_total(valores):
    return sum(valores)
```

Ahora el mensaje solo aparece si alguien llama a `preparar_informe()`.

**Idea clave:** un módulo debería ofrecer herramientas reutilizables; el código que coordina el programa decide cuándo utilizarlas.

## 6. `__name__` y `if __name__ == "__main__":`

Python asigna una variable especial `__name__` a cada módulo:
- al ejecutar un archivo directamente, normalmente vale `"__main__"`;
- al importar ese archivo desde otro módulo, suele contener el nombre del módulo.

Podemos aprovecharlo:

```python
# operaciones.py
def sumar(a, b):
    return a + b

if __name__ == "__main__":
    print(sumar(2, 3))
```

Si ejecutas `python operaciones.py`, se muestra `5`. Si otro archivo importa `operaciones`, la función queda disponible, pero el `print()` dentro del bloque no se ejecuta por esa importación.

En programas algo mayores se suele crear una función `main()` para coordinar la ejecución:

```python
def sumar(a, b):
    return a + b

def main():
    print(sumar(4, 6))

if __name__ == "__main__":
    main()
```

`main()` no es una palabra reservada ni una función automática: es una convención de nombre. El bloque `if` es el que llama a `main()` cuando el archivo se ejecuta directamente. Este patrón separa las herramientas reutilizables de las instrucciones que ponen en marcha el programa.

## 7. ¿Qué es un paquete?

Un **paquete** organiza módulos relacionados dentro de una estructura de directorios.

```text
gestion_gastos/
├── principal.py
└── gastos/
    ├── __init__.py
    ├── calculos.py
    └── validaciones.py
```

En el ejemplo, `gastos` agrupa los módulos `calculos.py` y `validaciones.py`. El archivo `__init__.py` se usa habitualmente en los paquetes tradicionales; puede estar vacío. Python moderno también permite ciertos paquetes sin ese archivo, pero por ahora basta con aprender la estructura tradicional.

Si `calculos.py` define `sumar_gastos()`, puedes importarla así:

```python
from gastos.calculos import sumar_gastos
```

O importar el módulo:

```python
from gastos import calculos

total = calculos.sumar_gastos()
```

El punto de `gastos.calculos` indica que `calculos` pertenece al paquete `gastos`.

**Diferencia esencial:**
- una **función** representa una tarea que se puede llamar;
- un **módulo** es una unidad de código importable, normalmente un archivo `.py`;
- un **paquete** organiza módulos relacionados;
- el **programa principal** coordina el uso de esas piezas.

## 8. ¿Cómo encuentra Python los módulos?

Cuando escribes `import operaciones`, Python busca un módulo siguiendo sus reglas de importación. En proyectos sencillos, la estructura de carpetas y el modo de ejecutar el programa son importantes.

Si aparece `ModuleNotFoundError`, revisa en orden:

1. ¿El archivo se llama exactamente `operaciones.py`?
2. ¿El nombre del `import` coincide y está bien escrito?
3. ¿El archivo está en la ubicación esperada?
4. ¿Desde qué carpeta estás ejecutando Python?
5. ¿VS Code utiliza el intérprete de Python que esperas?
6. ¿Existe un archivo local con el nombre de otro módulo que pueda interferir?

Que un archivo exista en el ordenador no significa que Python pueda importarlo con cualquier nombre desde cualquier ubicación. Antes de añadir rutas manuales, comprueba la estructura y el contexto desde el que ejecutas el programa.

## 9. Errores frecuentes

**Llamar a un nombre que no se importó directamente.** Con `import operaciones`, normalmente debes escribir `operaciones.sumar(2, 3)`. Si importas `from operaciones import sumar`, puedes escribir `sumar(2, 3)`.

**Confundir `print()` con `return`.** `print()` muestra información; `return` entrega un valor a quien llamó a la función. Si otra parte del programa necesita usar el resultado, devolverlo suele ser más útil que solo imprimirlo.

**Ejecutar acciones al importar.** Evita pedir datos, mostrar menús o modificar archivos automáticamente en el nivel superior de un módulo. Coloca esas acciones en funciones y ejecútalas cuando corresponda.

**Nombrar un archivo como un módulo estándar.** Evita nombres como `random.py` si pretendes usar la biblioteca estándar `random`.

**Importaciones circulares.** Si A importa B y B importa A, puede ser difícil controlar qué nombres están disponibles durante la carga. Si ocurre, revisa si ambos módulos dependen demasiado entre sí y si conviene trasladar una función compartida a un tercer módulo.

**Dividir demasiado.** No crees un archivo por cada función sin motivo. Agrupa código que tenga una responsabilidad común.

## 10. Diseñar responsabilidades

Imagina un programa que recibe una lista de gastos, valida los datos, calcula el total y muestra un resumen. Una posible estructura:

```text
gestion_gastos/
├── principal.py
├── validaciones.py
├── calculos.py
└── informes.py
```

Responsabilidades posibles:
- `principal.py`: coordina el flujo;
- `validaciones.py`: comprueba las reglas de los datos;
- `calculos.py`: calcula y devuelve resultados;
- `informes.py`: organiza cómo se presentan los resultados.

Es una propuesta, no una regla rígida. En un programa pequeño, varias responsabilidades podrían seguir juntas. Antes de crear un módulo, pregúntate:

1. ¿Qué responsabilidad concreta tendrá?
2. ¿Su nombre describe lo que contiene?
3. ¿Hay funciones que naturalmente pertenecen juntas?
4. ¿Otros módulos reutilizarán esas funciones?
5. ¿La división hace el programa más claro?
6. ¿Estoy añadiendo complejidad sin necesidad?

Cuanto más claras sean las responsabilidades y los datos de entrada y salida, más fácil será reutilizar cada pieza.

## 11. Ejemplo integrado paso a paso

Crea estos archivos:

```text
calculadora/
├── principal.py
└── operaciones.py
```

En `operaciones.py`:

```python
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b
```

En `principal.py`:

```python
import operaciones

def main():
    primer_numero = 12
    segundo_numero = 5

    suma = operaciones.sumar(primer_numero, segundo_numero)
    resta = operaciones.restar(primer_numero, segundo_numero)
    producto = operaciones.multiplicar(primer_numero, segundo_numero)

    print("Suma:", suma)
    print("Resta:", resta)
    print("Multiplicación:", producto)

if __name__ == "__main__":
    main()
```

Al ejecutar `principal.py`, el resultado esperado es:

```text
Suma: 17
Resta: 7
Multiplicación: 60
```

Analiza las responsabilidades:
- `operaciones.py` contiene funciones reutilizables;
- `principal.py` decide qué operaciones ejecutar y muestra los resultados;
- `main()` agrupa el flujo principal;
- el bloque `if` inicia el programa cuando ejecutas directamente `principal.py`.

Ahora crea temporalmente `prueba.py`:

```python
import operaciones

print(operaciones.sumar(100, 25))
```

Deberías ver `125`. Has reutilizado la función sin copiarla. Ese es uno de los beneficios centrales de la modularidad.

## 12. Cómo conecta esta clase con lo que ya sabes

La modularidad no sustituye las funciones, los condicionales, los bucles, las listas ni los diccionarios. Permite organizar esas herramientas en un programa más grande.

Una función que recorre una lista y calcula un total puede vivir en `calculos.py`. Otro módulo puede importarla y pasarle una lista. Dentro de la función, los bucles y acumuladores siguen funcionando igual que en la Etapa 0.

- **Funciones:** encapsulan una tarea.
- **Módulos:** agrupan y permiten reutilizar código.
- **Paquetes:** organizan módulos relacionados.
- **Programa principal:** coordina el uso de las piezas.

La nueva habilidad consiste en decidir dónde vive cada parte, además de saber resolver el algoritmo.

## 13. Vocabulario esencial

| Término | Significado |
|---|---|
| Modularidad | Organización en piezas con responsabilidades claras. |
| Módulo | Unidad de código importable, normalmente un archivo `.py`. |
| Importar | Cargar un módulo o nombres para poder utilizarlos. |
| Espacio de nombres | Contexto donde se encuentran nombres definidos o accesibles. |
| Paquete | Estructura que agrupa módulos relacionados. |
| `__init__.py` | Archivo usado habitualmente en paquetes tradicionales; puede estar vacío. |
| `__name__` | Variable especial que identifica cómo se usa un módulo. |
| `__main__` | Valor habitual de `__name__` cuando el archivo se ejecuta directamente. |
| `main()` | Convención de nombre para la función que coordina la ejecución. |
| Importación circular | Dependencia en la que los módulos se importan formando un ciclo. |
| Efecto secundario | Acción como imprimir, pedir datos o modificar un archivo. |

## 14. Ideas que debes recordar

1. Un módulo es una unidad importable, normalmente un archivo `.py`.
2. `import operaciones` permite acceder a nombres mediante `operaciones.nombre`.
3. `from operaciones import sumar` permite usar `sumar` directamente.
4. Importar ejecuta las instrucciones de nivel superior del módulo durante la carga.
5. Evita que un módulo realice acciones importantes solo por ser importado.
6. `if __name__ == "__main__":` separa la ejecución directa de la importación.
7. Un paquete agrupa módulos relacionados.
8. La organización debe responder a responsabilidades claras.
9. El programa modular sigue utilizando las mismas funciones y estructuras de control que ya conoces.

## 15. Autoevaluación de comprensión

Responde con tus palabras, sin consultar primero las secciones anteriores. No necesitas repetir definiciones literalmente; importa que puedas explicarlas y aplicarlas.

1. ¿Qué problema intenta resolver la modularidad?
2. ¿Qué diferencia hay entre una función, un módulo y un paquete?
3. Si escribes `import operaciones`, ¿por qué llamarías a `operaciones.sumar(2, 3)`?
4. ¿Qué diferencia hay entre `import operaciones` y `from operaciones import sumar`?
5. ¿Qué podría ocurrir si un módulo solicita datos en una instrucción situada fuera de una función?
6. ¿Para qué sirve `if __name__ == "__main__":`?
7. ¿Qué revisarías si aparece `ModuleNotFoundError` al importar un archivo propio?
8. ¿Por qué no conviene llamar `random.py` a un archivo de tu proyecto?
9. ¿Cómo separarías un programa que lee datos, los valida, calcula resultados y genera un informe?
10. ¿Por qué crear muchos módulos no garantiza una mejor organización?

Vuelve a las secciones donde tengas dudas. Si puedes explicar los conceptos, pero todavía te cuesta decidir cómo dividir los archivos, es normal: esa habilidad se consolida con práctica.

## 16. Qué viene después

Después de estudiar esta clase, prepararemos una práctica para crear y utilizar módulos propios. Comprobaremos que puedes crear una estructura sencilla, definir funciones reutilizables, importarlas desde otro archivo, separar la lógica de la ejecución principal e investigar errores sencillos de importación.

Más adelante ampliaremos estos fundamentos con alcance de variables, funciones avanzadas, comprehensions, iteradores, excepciones, archivos, JSON y entornos virtuales. No necesitas adelantarte a esos temas todavía.
