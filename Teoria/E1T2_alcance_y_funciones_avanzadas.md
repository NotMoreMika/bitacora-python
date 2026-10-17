# E1T2 --- Alcance y funciones avanzadas en Python

**Etapa:** 1 --- Python intermedio y diseño de programas\
**Tema:** 2 --- Alcance y funciones avanzadas\
**Tipo:** Clase teórica completa

## 1. Objetivo del tema

En el tema anterior aprendiste a dividir programas en módulos y a
separar la definición de una función de su ejecución. Ahora
profundizaremos en cómo Python resuelve los nombres que aparecen dentro
de las funciones, cómo se reciben los datos y cómo diseñar funciones
flexibles, predecibles y reutilizables.

Al terminar, debes comprender el alcance local y global, los ámbitos
envolventes, la regla LEGB, `global`, `nonlocal`, parámetros,
argumentos, valores predeterminados, `*args`, `**kwargs`, el
desempaquetado de argumentos y algunas herramientas para definir
interfaces claras.

No basta con reconocer la sintaxis: debes poder predecir qué hará un
programa y justificar por qué.

------------------------------------------------------------------------

## 2. Qué es una función y cómo se comporta

Una función agrupa instrucciones bajo un nombre. Puede recibir datos,
procesarlos y devolver un resultado.

``` python
def calcular_total(precios):
    total = sum(precios)
    return total

precios = [12.50, 8.00, 4.25]
resultado = calcular_total(precios)
print(resultado)
```

-   `def` inicia la definición.
-   `calcular_total` es el nombre.
-   `precios` es un parámetro.
-   El cuerpo calcula el total.
-   `return` entrega el resultado a quien llamó la función.
-   `calcular_total(precios)` es una llamada.

### 2.1 Definir no es ejecutar

La definición crea la función, pero no ejecuta su cuerpo hasta que se
llama:

``` python
def saludar():
    print("Hola")

# Aquí la función está definida, pero todavía no se ejecutó.
saludar()
```

Esta diferencia es importante al trabajar con módulos: definir una
función no ejecuta las instrucciones de su cuerpo. Se ejecutan cuando se
llama.

### 2.2 `return` frente a `print`

`print()` muestra información en la consola; `return` entrega un valor
al código que llamó la función.

``` python
def calcular_doble(numero):
    return numero * 2

resultado = calcular_doble(6)
print(resultado + 1)  # 13
```

En cambio:

``` python
def mostrar_doble(numero):
    print(numero * 2)

resultado = mostrar_doble(6)
print(resultado)  # None
```

La segunda función muestra `12`, pero no devuelve ese número. Cuando una
función termina sin devolver explícitamente un valor, Python devuelve
`None`.

Usa `return` cuando el resultado deba reutilizarse en otros cálculos.
Usa `print` cuando el propósito sea mostrar información. Una función
puede hacer ambas cosas, pero conviene que su comportamiento sea claro.

### 2.3 `return` termina la función

``` python
def dividir(a, b):
    if b == 0:
        return None
    return a / b
```

Si `b` es cero, la función termina en el primer `return`. En este
ejemplo `None` indica que no se obtuvo un resultado numérico; es una
decisión de diseño que debe documentarse. En otros casos puede ser más
apropiado lanzar una excepción.

------------------------------------------------------------------------

## 3. Alcance de los nombres

El **alcance** (*scope*) es la región del programa en la que un nombre
puede consultarse directamente.

``` python
def crear_mensaje():
    mensaje = "Hola desde la función"
    print(mensaje)

crear_mensaje()
# print(mensaje)  # NameError: ese nombre no existe en este ámbito
```

`mensaje` es local a la función. No se convierte en global solo por
haber sido creado durante la ejecución.

### 3.1 Variables locales

Los parámetros y los nombres creados dentro de una función normalmente
son locales a esa llamada.

``` python
def duplicar(numero):
    resultado = numero * 2
    return resultado

a = duplicar(4)
b = duplicar(10)
print(a)  # 8
print(b)  # 20
```

Cada llamada tiene sus propios parámetros y variables locales. La
llamada con `4` no sustituye los valores locales de la llamada con `10`.

### 3.2 Variables globales

Una variable definida en el nivel superior de un módulo es global
respecto a ese módulo.

``` python
impuesto = 0.15

def calcular_precio_final(precio):
    return precio * (1 + impuesto)
```

La función puede leer `impuesto` porque Python lo busca si no encuentra
ese nombre en el ámbito local. Sin embargo, depender de muchas variables
globales hace que una función sea más difícil de probar y reutilizar.

Una alternativa más explícita:

``` python
def calcular_precio_final(precio, impuesto):
    return precio * (1 + impuesto)

print(calcular_precio_final(100, 0.15))
```

Ahora la dependencia se ve en los parámetros. Como regla general,
prefiere pasar los datos necesarios mediante parámetros antes que
compartirlos a través de muchas variables globales.

### 3.3 Una función puede leer un global sin declararlo

``` python
tasa = 0.2

def calcular(precio):
    return precio * tasa
```

No hace falta escribir `global tasa` porque la función solo lee el
nombre. `global` se necesita cuando quieres asignar al nombre global
desde dentro de la función.

------------------------------------------------------------------------

## 4. La regla LEGB

Cuando Python necesita resolver un nombre, lo busca siguiendo la regla
**LEGB**:

1.  **L --- Local:** ámbito de la función actual.
2.  **E --- Enclosing:** ámbitos de funciones exteriores que contienen a
    la función actual.
3.  **G --- Global:** ámbito del módulo actual.
4.  **B --- Built-in:** nombres incorporados de Python, como `len`,
    `sum`, `print` y `range`.

Si no encuentra el nombre, puede producir un `NameError`.

### 4.1 Local antes que global

``` python
mensaje = "global"

def mostrar():
    mensaje = "local"
    print(mensaje)

mostrar()        # local
print(mensaje)   # global
```

Dentro de `mostrar`, el nombre corresponde a la variable local. Fuera de
la función, la variable global conserva su valor.

### 4.2 Enclosing: funciones anidadas

Una función interior puede leer nombres definidos en una función
exterior:

``` python
def crear_saludo(nombre):
    prefijo = "Hola"

    def construir():
        return f"{prefijo}, {nombre}"

    return construir()

print(crear_saludo("Ana"))  # Hola, Ana
```

`construir` no define `prefijo` ni `nombre`; Python los encuentra en el
ámbito envolvente de `crear_saludo`.

### 4.3 Built-in: evita ocultar nombres incorporados

``` python
numeros = [4, 7, 2]
print(len(numeros))
```

`len` es un nombre incorporado. Evita usar nombres como `sum`, `list`,
`str` o `len` para tus propias variables:

``` python
sum = 100
# sum([1, 2, 3])  # Fallaría: sum ahora se refiere al entero 100
```

Es preferible usar nombres como `total`, `suma` o `total_gastos`.

------------------------------------------------------------------------

## 5. Asignaciones, `UnboundLocalError` y mutabilidad

Python trata como local un nombre al que se asigna dentro de una
función, salvo que se declare `global` o `nonlocal`.

``` python
contador = 10

def aumentar():
    contador = contador + 1
    print(contador)

aumentar()
```

Esto provoca `UnboundLocalError`. La asignación hace que Python trate
`contador` como local dentro de `aumentar`, pero el lado derecho intenta
leerlo antes de que ese nombre local tenga valor.

Una solución habitualmente preferible es pasar el valor y devolver el
nuevo:

``` python
def aumentar(contador):
    return contador + 1

contador = 10
contador = aumentar(contador)
print(contador)  # 11
```

### 5.1 Reasignar un nombre no es lo mismo que mutar un objeto

Observa:

``` python
numeros = [1, 2]

def agregar_numero():
    numeros.append(3)

agregar_numero()
print(numeros)  # [1, 2, 3]
```

La función modifica la lista a la que apunta el nombre global; no está
asignando una lista nueva al nombre `numeros`. Por eso no necesita
`global`.

Pero que funcione no significa que siempre sea el diseño más claro.
Puedes hacer explícita la dependencia:

``` python
def agregar_numero(numeros, numero):
    numeros.append(numero)

datos = [1, 2]
agregar_numero(datos, 3)
```

En cambio, reasignar el parámetro es distinto:

``` python
def reemplazar_lista(lista):
    lista = ["otra", "lista"]

elementos = ["inicial"]
reemplazar_lista(elementos)
print(elementos)  # ['inicial']
```

El nombre local `lista` apunta a otra lista; el nombre exterior
`elementos` no cambia.

**Idea clave:** pasar una lista no crea una copia automática. La función
puede modificar el objeto mutable recibido. Si no quieres esa mutación,
evita modificarlo o trabaja con una copia explícita cuando proceda.

------------------------------------------------------------------------

## 6. `global`: modificar un nombre global

`global` declara que las asignaciones a un nombre dentro de una función
se refieren al nombre global del módulo.

``` python
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
incrementar()
print(contador)  # 2
```

Sin `global`, `contador += 1` haría que el nombre se tratara como local,
y la lectura del valor anterior provocaría un error.

Aunque `global` es válido, un uso frecuente puede volver difícil
entender qué modifica cada función. En muchos casos puedes evitarlo:

``` python
def incrementar(contador):
    return contador + 1

contador = 0
contador = incrementar(contador)
contador = incrementar(contador)
```

Utiliza `global` cuando modificar estado global sea realmente la
intención, no como mecanismo habitual para pasar datos entre funciones.

------------------------------------------------------------------------

## 7. `nonlocal`: modificar un nombre de una función exterior

`nonlocal` se utiliza dentro de una función anidada para indicar que una
asignación debe modificar un nombre existente en una función envolvente,
en lugar de crear un nombre local nuevo o modificar uno global.

``` python
def crear_contador():
    contador = 0

    def incrementar():
        nonlocal contador
        contador += 1
        return contador

    return incrementar

siguiente = crear_contador()
print(siguiente())  # 1
print(siguiente())  # 2
print(siguiente())  # 3
```

`crear_contador()` crea `contador` y devuelve la función interior. La
función devuelta conserva acceso al nombre del ámbito donde fue creada.
Este mecanismo se conoce como **cierre** (*closure*).

Diferencias:

-   `global`: el nombre pertenece al ámbito del módulo.
-   `nonlocal`: el nombre pertenece a una función envolvente.
-   Sin declaración: una asignación normalmente crea un nombre local.

`nonlocal` no puede referirse a un nombre global ni crear un nombre
exterior inexistente. Es útil para cierres que mantienen un pequeño
estado. En programas mayores, a veces una clase u objeto explícito
representa ese estado con más claridad.

------------------------------------------------------------------------

## 8. Parámetros y argumentos

Un **parámetro** es el nombre que aparece en la definición. Un
**argumento** es el valor suministrado en una llamada.

``` python
def presentar(nombre, edad):
    print(f"{nombre} tiene {edad} años")

presentar("Luis", 25)
```

`nombre` y `edad` son parámetros; `"Luis"` y `25` son argumentos.

### 8.1 Los parámetros reciben referencias a objetos

Python vincula los nombres de los parámetros a los objetos que se pasan.
No copia automáticamente todos los objetos.

Con un entero:

``` python
def cambiar_numero(numero):
    numero = 99

valor = 10
cambiar_numero(valor)
print(valor)  # 10
```

La reasignación del nombre local `numero` no cambia el nombre exterior
`valor`.

Con una lista mutable:

``` python
def agregar_elemento(lista):
    lista.append("nuevo")

elementos = ["inicial"]
agregar_elemento(elementos)
print(elementos)  # ['inicial', 'nuevo']
```

Ambos nombres apuntan al mismo objeto lista, así que la mutación se
observa fuera de la función. Esto no ocurre porque Python reasigne la
variable exterior, sino porque el objeto compartido fue modificado.

------------------------------------------------------------------------

## 9. Argumentos posicionales y por nombre

``` python
def crear_usuario(nombre, edad, activo):
    return {"nombre": nombre, "edad": edad, "activo": activo}

crear_usuario("Marta", 28, True)
crear_usuario(nombre="Marta", edad=28, activo=True)
```

Ambas llamadas asignan los mismos valores.

### 9.1 Posicionales

El primer argumento corresponde al primer parámetro, el segundo al
segundo, etc.

``` python
def restar(a, b):
    return a - b

print(restar(10, 3))  # 7
print(restar(3, 10))  # -7
```

El orden importa.

### 9.2 Por nombre (*keyword arguments*)

Puedes indicar qué parámetro recibe cada valor:

``` python
def configurar(host, puerto, seguro):
    return f"{host}:{puerto}, seguro={seguro}"

configurar(host="localhost", puerto=8080, seguro=True)
```

Los nombres hacen más legible una llamada con varios valores. Puedes
combinar argumentos posicionales y por nombre, pero los posicionales
deben aparecer primero:

``` python
presentar("Ana", edad=30)  # Correcto
```

No hagas esto:

``` python
# presentar(nombre="Ana", 30)
```

Tampoco proporciones el mismo parámetro dos veces:

``` python
# presentar("Ana", nombre="Luis", edad=30)
```

Python generará un `TypeError`.

------------------------------------------------------------------------

## 10. Valores predeterminados

Un parámetro puede tener un valor predeterminado que se utiliza si se
omite el argumento.

``` python
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}"

print(saludar("Ana"))                 # Hola, Ana
print(saludar("Ana", "Buenos días"))  # Buenos días, Ana
print(saludar("Ana", saludo="Buenas tardes"))
```

Los parámetros requeridos deben aparecer antes que los que tienen
valores predeterminados:

``` python
def registrar(nombre, activo=True):
    ...
```

La definición `def registrar(activo=True, nombre):` no es válida.

### 10.1 `None` como marcador

`None` puede representar que no se proporcionó un valor o que no hay un
valor aplicable, según el contrato de la función:

``` python
def obtener_etiqueta(texto, prefijo=None):
    if prefijo is None:
        prefijo = "INFO"
    return f"[{prefijo}] {texto}"
```

Aquí `None` significa "utiliza el prefijo habitual".

### 10.2 El peligro de los valores predeterminados mutables

Este es uno de los errores más importantes del tema:

``` python
def agregar_nombre(nombre, nombres=[]):
    nombres.append(nombre)
    return nombres

print(agregar_nombre("Ana"))   # ['Ana']
print(agregar_nombre("Luis"))  # ['Ana', 'Luis']
```

La lista predeterminada se crea cuando Python ejecuta la definición de
la función, no en cada llamada. Las llamadas reutilizan el mismo objeto,
así que el estado se acumula inesperadamente.

Usa `None` como marcador y crea una lista nueva dentro de la función:

``` python
def agregar_nombre(nombre, nombres=None):
    if nombres is None:
        nombres = []
    nombres.append(nombre)
    return nombres

print(agregar_nombre("Ana"))   # ['Ana']
print(agregar_nombre("Luis"))  # ['Luis']
```

Si se pasa una lista explícitamente, esa lista sí será modificada:

``` python
grupo = ["Marta"]
agregar_nombre("Luis", grupo)
print(grupo)  # ['Marta', 'Luis']
```

**Regla práctica:** evita listas, diccionarios y otros objetos mutables
como valores predeterminados cuando esperes un objeto nuevo en cada
llamada.

------------------------------------------------------------------------

## 11. `*args`: cantidad variable de argumentos posicionales

`*args` reúne los argumentos posicionales sobrantes en una tupla. `args`
es un nombre convencional, no una palabra reservada.

``` python
def sumar_todos(*args):
    return sum(args)

print(sumar_todos(2, 3))       # 5
print(sumar_todos(2, 3, 4, 5)) # 14
print(sumar_todos())           # 0
```

Dentro de la función, `args` es una tupla:

``` python
def inspeccionar(*args):
    print(type(args))
    print(args)

inspeccionar("a", 10, True)
# <class 'tuple'>
# ('a', 10, True)
```

Puedes recorrerla, consultar su longitud y acceder a posiciones, pero no
reasignar sus elementos.

### 11.1 Combinar con parámetros normales

``` python
def registrar_evento(tipo, *detalles):
    return {"tipo": tipo, "detalles": detalles}

print(registrar_evento("error", "archivo", 404, "no encontrado"))
```

`tipo` recibe el primer argumento y los restantes se agrupan en
`detalles`.

### 11.2 `*` en una llamada: desempaquetar una secuencia

El asterisco también distribuye los elementos de un iterable como
argumentos posicionales:

``` python
def sumar_tres(a, b, c):
    return a + b + c

valores = [2, 4, 6]
print(sumar_tres(*valores))  # Equivale a sumar_tres(2, 4, 6)
```

No es lo mismo `sumar_tres(valores)`, que pasa una lista como un
argumento, que `sumar_tres(*valores)`, que distribuye los elementos. La
cantidad y el orden deben coincidir con la función.

------------------------------------------------------------------------

## 12. `**kwargs`: cantidad variable de argumentos por nombre

`**kwargs` reúne argumentos por nombre no asignados a parámetros
explícitos. Dentro de la función se reciben como un diccionario.

``` python
def crear_perfil(**kwargs):
    return kwargs

perfil = crear_perfil(nombre="Eva", edad=27, ciudad="Sevilla")
print(perfil)
# {'nombre': 'Eva', 'edad': 27, 'ciudad': 'Sevilla'}
```

`kwargs` también es un nombre convencional.

### 12.1 Recorrer las opciones

``` python
def mostrar_configuracion(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_configuracion(modo="desarrollo", depuracion=True, intentos=3)
```

Es útil para opciones realmente flexibles. Pero si una función solo
acepta tres opciones conocidas, declararlas explícitamente suele ser más
claro y permite detectar errores de escritura.

### 12.2 `**` en una llamada: desempaquetar un diccionario

``` python
def crear_usuario(nombre, edad, activo):
    return f"{nombre}, {edad}, activo={activo}"

datos = {"nombre": "Leo", "edad": 22, "activo": True}
print(crear_usuario(**datos))
```

Las claves deben coincidir con los nombres de los parámetros, salvo que
la función acepte opciones adicionales mediante `**kwargs`.

### 12.3 Diferencia que debes memorizar

-   `*args` en una **definición** reúne argumentos posicionales en una
    tupla.
-   `**kwargs` en una **definición** reúne argumentos por nombre en un
    diccionario.
-   `*secuencia` en una **llamada** distribuye elementos por posición.
-   `**diccionario` en una **llamada** distribuye claves y valores como
    argumentos por nombre.

------------------------------------------------------------------------

## 13. Orden y combinación de parámetros

Una función puede combinar parámetros requeridos, valores
predeterminados, `*args`, parámetros exclusivamente por nombre y
`**kwargs`.

``` python
def crear_informe(titulo, *valores, moneda="EUR", **metadatos):
    total = sum(valores)
    informe = {
        "titulo": titulo,
        "valores": valores,
        "total": total,
        "moneda": moneda,
    }
    informe.update(metadatos)
    return informe

resultado = crear_informe(
    "Gastos semanales",
    20,
    35,
    12.50,
    moneda="EUR",
    responsable="Ana",
    periodo="semana 42",
)
```

-   `titulo` recibe el primer argumento.
-   `valores` recibe una tupla con `20`, `35` y `12.50`.
-   `moneda` recibe su valor por nombre.
-   `responsable` y `periodo` se reúnen en `metadatos`.

**Advertencia:** si todo se recibe mediante `**kwargs`, una opción mal
escrita podría aceptarse silenciosamente. Declara los parámetros
importantes de forma explícita.

------------------------------------------------------------------------

## 14. Parámetros exclusivamente por nombre y posicionales

Estas herramientas permiten restringir cómo se pasan los argumentos y
crear interfaces más claras.

### 14.1 Exclusivamente por nombre: `*`

Después de un `*` independiente, los parámetros siguientes deben darse
por nombre:

``` python
def calcular_precio(precio, *, impuesto=0.0, descuento=0.0):
    return precio * (1 + impuesto) * (1 - descuento)

print(calcular_precio(100, impuesto=0.15, descuento=0.10))
```

La llamada `calcular_precio(100, 0.15, 0.10)` no es válida. Es útil
exigir nombres cuando los valores posicionales serían ambiguos.

### 14.2 Exclusivamente posicionales: `/`

Los parámetros anteriores a `/` solo pueden pasarse por posición:

``` python
def dividir(a, b, /):
    return a / b

print(dividir(10, 2))
```

`dividir(a=10, b=2)` no es válido. Esto puede ser útil cuando no quieres
que los nombres de los parámetros formen parte de la interfaz pública.

### 14.3 Combinar ambos

``` python
def ejemplo(posicional, /, normal, *, opcion):
    return posicional, normal, opcion

ejemplo(1, 2, opcion=3)
```

-   `posicional` debe darse por posición.
-   `normal` puede darse por posición o por nombre.
-   `opcion` debe darse por nombre.

No necesitas imponer estas restricciones en todas las funciones. Úsalas
cuando mejoren la claridad y el contrato.

------------------------------------------------------------------------

## 15. Diseñar funciones reutilizables

La sintaxis por sí sola no garantiza un buen diseño. Una función debería
tener un propósito identificable y un contrato comprensible.

### 15.1 Responsabilidades claras

Una función que valida datos, calcula, escribe archivos, pide entrada y
muestra resultados puede ser difícil de probar. Separar las
responsabilidades permite reutilizar y probar cada parte:

``` python
def calcular_total(gastos):
    return sum(gastos)

def calcular_promedio(gastos):
    return sum(gastos) / len(gastos)

def mostrar_informe(total, promedio):
    print(f"Total: {total}")
    print(f"Promedio: {promedio}")
```

En este ejemplo `calcular_promedio` presupone una lista no vacía. La
función que la llame debe garantizar esa precondición, o la función debe
definir cómo manejar la lista vacía.

No significa que cada línea deba convertirse en una función. Divide
cuando eso ayude a comprender, reutilizar o probar el programa.

### 15.2 Entradas y salidas explícitas

Una función suele ser más reutilizable si recibe los datos por
parámetros y entrega el resultado con `return`:

``` python
def calcular_total(gastos):
    return sum(gastos)
```

No necesita saber de dónde vino la lista ni cómo se mostrará el
resultado. Puede utilizarse desde una aplicación de consola, una
interfaz gráfica o una prueba automática.

### 15.3 Efectos secundarios

Un **efecto secundario** es un cambio o acción observable aparte del
valor devuelto: modificar una lista, imprimir, escribir un archivo o
cambiar una variable global.

Los efectos secundarios no son necesariamente malos; guardar un archivo
puede ser justamente el propósito de una función. El problema es que
ocurran de forma inesperada o que se mezclen demasiadas
responsabilidades.

### 15.4 Nombres y docstrings

Los nombres deben expresar la intención. Una *docstring* es la cadena
situada inmediatamente después de la cabecera de una función:

``` python
def calcular_promedio(valores):
    """Devuelve la media de una colección no vacía."""
    return sum(valores) / len(valores)
```

La docstring puede explicar el propósito, las entradas, la salida, las
precondiciones y los casos especiales.

### 15.5 Anotaciones de tipos

``` python
def calcular_total(valores: list[float]) -> float:
    return sum(valores)
```

Las anotaciones documentan la intención y ayudan a editores y
herramientas. Python no valida automáticamente los tipos en tiempo de
ejecución por el simple hecho de que exista una anotación. No sustituyen
las comprobaciones necesarias.

------------------------------------------------------------------------

## 16. Ejemplo integrado: un informe de gastos

Este ejemplo combina parámetros, valores predeterminados, alcance y
separación de responsabilidades:

``` python
def calcular_total(gastos):
    """Devuelve la suma de los gastos."""
    return sum(gastos)


def calcular_promedio(gastos):
    """Devuelve el promedio, o None si no hay gastos."""
    if not gastos:
        return None
    return calcular_total(gastos) / len(gastos)


def construir_informe(gastos, *, moneda="EUR", incluir_detalle=True):
    """Construye y devuelve los datos de un informe."""
    total = calcular_total(gastos)
    promedio = calcular_promedio(gastos)

    informe = {
        "cantidad": len(gastos),
        "total": total,
        "promedio": promedio,
        "moneda": moneda,
    }

    if incluir_detalle:
        informe["gastos"] = list(gastos)

    return informe


def mostrar_informe(informe):
    """Presenta el informe en la consola."""
    print(f"Cantidad de gastos: {informe['cantidad']}")
    print(f"Total: {informe['total']} {informe['moneda']}")

    if informe["promedio"] is None:
        print("No se puede calcular el promedio sin gastos.")
    else:
        print(f"Promedio: {informe['promedio']:.2f} {informe['moneda']}")

    if "gastos" in informe:
        print(f"Detalle: {informe['gastos']}")


gastos = [120, 35.50, 18]
informe = construir_informe(gastos, moneda="EUR", incluir_detalle=True)
mostrar_informe(informe)
```

Observa:

-   `calcular_total` recibe datos y devuelve un valor.
-   `calcular_promedio` define qué ocurre con una lista vacía.
-   `construir_informe` exige que `moneda` e `incluir_detalle` se pasen
    por nombre, porque están después del `*`.
-   `informe` es local a `construir_informe`; no es global.
-   `mostrar_informe` presenta datos, no realiza los cálculos.
-   `list(gastos)` crea una copia superficial de la lista para incluirla
    en el informe. Si hubiera objetos mutables dentro de la lista, esos
    objetos internos seguirían compartidos.

La elección de devolver `None` para una lista vacía es una decisión de
diseño. Quien use la función debe comprobar ese caso. En otro programa
puede ser más apropiado validar antes o lanzar una excepción. Lo
esencial es elegir una política coherente y documentarla.

------------------------------------------------------------------------

## 17. Errores frecuentes y cómo diagnosticarlos

### Error A: intentar usar una variable local fuera de la función

``` python
def calcular():
    resultado = 10

calcular()
# print(resultado)  # NameError
```

Si necesitas el resultado fuera, devuélvelo y asigna la llamada a un
nombre exterior.

### Error B: asignar a un global sin `global`

``` python
contador = 0

def incrementar():
    contador += 1
```

La asignación convierte `contador` en local dentro de la función, pero
se intenta leer antes de inicializarlo. Suele ser mejor recibir el valor
por parámetro y devolver el nuevo.

### Error C: declarar `global` para leer una variable

No hace falta `global` si solo lees el nombre. Es necesario para
reasignar el nombre global.

### Error D: confundir `print` con `return`

Una función puede imprimir un número y devolver `None`. Pregunta si
necesitas mostrar un resultado o entregarlo a otro cálculo.

### Error E: usar una lista predeterminada

Una lista predeterminada se crea una vez al definir la función y se
reutiliza. Usa `None` y crea una lista dentro si cada llamada debe
empezar vacía.

### Error F: cantidad incorrecta de argumentos

Si una función espera dos argumentos y recibe tres, Python normalmente
genera `TypeError`. Revisa la definición y la llamada antes de añadir
`*args`.

### Error G: confundir reunión y desempaquetado

En una definición, `*args` reúne y `**kwargs` reúne. En una llamada,
`*secuencia` expande y `**diccionario` expande.

### Error H: confiar en las anotaciones para validar

Una anotación `numero: int` no impide que alguien pase una cadena. Añade
validaciones si el programa las necesita.

### Error I: ocultar errores con `**kwargs`

Un parámetro escrito mal podría terminar como una clave inesperada.
Declara explícitamente las opciones importantes.

### Error J: confundir mutación y reasignación

`lista.append(4)` modifica el objeto. `lista = [4]` cambia a qué objeto
apunta el nombre local. Esa diferencia explica muchos resultados que
parecen contradictorios.

------------------------------------------------------------------------

## 18. Cómo razonar sobre una función

Al leer o escribir una función, pregúntate:

1.  ¿Qué parámetros declara?
2.  ¿Qué argumentos recibe la llamada y cómo se vinculan?
3.  ¿Qué nombres son locales?
4.  ¿Qué nombres se leen desde ámbitos envolventes o globales?
5.  ¿Hay asignaciones que requieran `global` o `nonlocal`?
6.  ¿Devuelve un valor o produce un efecto secundario?
7.  ¿Qué ocurre si se omite un argumento con valor predeterminado?
8.  ¿Algún valor predeterminado mutable podría conservar estado entre
    llamadas?
9.  ¿Qué tipo de objeto contiene `args` o `kwargs`?
10. ¿La función modifica objetos que recibió?
11. ¿Qué precondiciones debe cumplir la entrada?
12. ¿Su interfaz deja claro qué acepta y qué devuelve?

Una práctica útil es predecir la salida antes de ejecutar el código.
Después, ejecútalo y explica cualquier diferencia. Puedes consultar los
apuntes y la documentación oficial; intenta primero razonar y luego
verifica tu hipótesis.

------------------------------------------------------------------------

## 19. Autoevaluación conceptual

Estas preguntas sirven para comprobar la comprensión antes de la
actividad práctica. Intenta responderlas con tus propias palabras.

### Alcance y resolución de nombres

1.  ¿Qué diferencia hay entre una variable local y una global?
2.  ¿Qué significan las letras de LEGB y en qué orden busca Python?
3.  ¿Por qué una asignación dentro de una función puede producir
    `UnboundLocalError` aunque exista una variable global con ese
    nombre?
4.  ¿Cuándo se necesita `global`?
5.  ¿Cuándo se necesita `nonlocal` y en qué se diferencia de `global`?
6.  ¿Por qué depender de muchas variables globales puede dificultar las
    pruebas?

### Parámetros y argumentos

7.  ¿Cuál es la diferencia entre parámetro y argumento?
8.  ¿Qué diferencia hay entre pasar argumentos por posición y por
    nombre?
9.  ¿Qué ocurre cuando se omite un argumento con valor predeterminado?
10. ¿Por qué una lista predeterminada puede conservar datos entre
    llamadas?
11. ¿Qué diferencia hay entre mutar una lista recibida y reasignar el
    nombre del parámetro?
12. ¿Qué es una precondición?

### Argumentos variables y diseño

13. ¿Qué objeto contiene `args` dentro de una función definida con
    `*args`?
14. ¿Qué objeto contiene `kwargs` dentro de una función definida con
    `**kwargs`?
15. ¿Qué hacen `*secuencia` y `**diccionario` en una llamada?
16. ¿Para qué sirve el `*` independiente en una definición?
17. ¿Para qué sirve `/`?
18. ¿Por qué `**kwargs` no debería reemplazar siempre a parámetros
    explícitos?
19. ¿Qué diferencia hay entre imprimir un resultado y devolverlo?
20. ¿Qué hace que una función sea reutilizable y fácil de probar?

**Criterio de dominio:** no basta con reconocer las palabras `global`,
`nonlocal`, `*args` y `**kwargs`. Debes poder leer una función, predecir
cómo se resuelven sus nombres, explicar cómo se asignan sus argumentos y
justificar si su diseño es claro y coherente.

------------------------------------------------------------------------

## 20. Glosario

-   **Alcance (*scope*):** región donde un nombre puede resolverse
    directamente.
-   **Variable local:** nombre local a una función o ámbito.
-   **Variable global:** nombre definido en el nivel superior del
    módulo.
-   **Ámbito envolvente (*enclosing scope*):** ámbito de una función
    exterior que contiene otra función.
-   **LEGB:** orden Local, Enclosing, Global y Built-in.
-   **Parámetro:** nombre declarado en la definición de una función.
-   **Argumento:** valor suministrado en una llamada.
-   **Argumento posicional:** se asocia por su posición.
-   **Argumento por nombre:** se asocia mediante el nombre del
    parámetro.
-   **Valor predeterminado:** valor utilizado cuando se omite el
    argumento correspondiente.
-   **Objeto mutable:** objeto cuyo contenido puede cambiar, como una
    lista o un diccionario.
-   **`*args`:** reúne argumentos posicionales sobrantes en una tupla.
-   **`**kwargs`:** reúne argumentos por nombre sobrantes en un
    diccionario.
-   **Desempaquetado:** expansión de los elementos de una secuencia o
    diccionario en una llamada.
-   **`return`:** termina la función y entrega un valor si se
    especifica.
-   **Efecto secundario:** cambio o acción observable, como modificar
    una lista o escribir un archivo.
-   **Precondición:** condición que debe cumplirse para que una función
    opere según lo esperado.
-   **Docstring:** cadena que documenta una función, clase o módulo.
-   **Cierre (*closure*):** función que conserva acceso a nombres del
    ámbito donde fue creada.

------------------------------------------------------------------------

## 21. Documentación oficial

Cuando quieras confirmar la sintaxis o consultar la descripción formal,
utiliza la documentación oficial de Python:

-   Tutorial --- Definición de funciones:
    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
-   Tutorial --- Parámetros especiales:
    https://docs.python.org/3/tutorial/controlflow.html#special-parameters
-   Tutorial --- Más sobre la definición de funciones:
    https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
-   Modelo de ejecución --- Resolución de nombres:
    https://docs.python.org/3/reference/executionmodel.html#resolution-of-names
-   Referencia --- Declaración `global`:
    https://docs.python.org/3/reference/simple_stmts.html#the-global-statement
-   Referencia --- Declaración `nonlocal`:
    https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement

La documentación puede emplear términos más técnicos. Utilízala para
confirmar reglas y profundizar cuando lo necesites.

------------------------------------------------------------------------

## 22. Qué debes dominar antes de la actividad

Al terminar esta clase deberías poder:

-   distinguir los ámbitos local, envolvente, global e incorporado;
-   explicar LEGB y detectar errores de resolución de nombres;
-   comprender `global` y `nonlocal` y saber cuándo no son necesarios;
-   diferenciar parámetros y argumentos, y comprender llamadas
    posicionales y por nombre;
-   usar valores predeterminados sin introducir estado mutable
    accidental;
-   leer y escribir funciones sencillas con `*args` y `**kwargs`;
-   desempaquetar secuencias y diccionarios en llamadas;
-   reconocer parámetros exclusivamente posicionales y exclusivamente
    por nombre;
-   explicar qué devuelve una función, qué modifica y qué precondiciones
    tiene;
-   justificar decisiones básicas para crear funciones reutilizables,
    legibles y comprobables.

No necesitas memorizar cada detalle de la referencia del lenguaje. Sí
necesitas comprender los mecanismos principales, poder leerlos en código
real y aplicarlos con criterio. La actividad práctica posterior servirá
para comprobar tu comprensión y detectar qué puntos necesitan más
trabajo.
