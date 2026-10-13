**Etapa:** 1 — Python intermedio y diseño de programas  

**Bloque:** 1 — Modularidad  

**Estado inicial:** Pendiente  

**Apuntes relacionados:** 06 — Modularidad en Python: módulos, importaciones y paquetes

## Objetivo

Demostrar que puedes dividir un programa pequeño en módulos con responsabilidades claras, reutilizar funciones mediante importaciones y separar las herramientas reutilizables de la ejecución principal.

## Reglas de trabajo

- Guarda los ejercicios en tu repositorio de GitHub, dentro de la carpeta correspondiente a la Etapa 1. No es necesario modificar archivos anteriores.
- Usa archivos `.py` para el código. Puedes añadir un `.md` breve si necesitas explicar decisiones o incidencias.
- **Puedes consultar** los apuntes de la clase, la documentación oficial de Python y los mensajes de error. No hace falta resolverlo todo de memoria.
- Primero intenta comprender el error y comprobar la estructura de archivos antes de buscar una solución completa.
- No copies el ejemplo de la calculadora tal cual como entrega: los ejercicios cambian el contexto y requieren tomar decisiones propias.

## Ejercicio 1 — Un módulo reutilizable

Crea un módulo llamado `estadisticas.py` que incluya estas funciones:

- `calcular_total(valores)`: devuelve la suma de los valores.
- `contar_positivos(valores)`: devuelve cuántos valores son mayores que cero.
- `obtener_promedio(valores)`: devuelve el promedio. Decide qué resultado debe producir si la lista está vacía y deja esa decisión clara en el código o en un comentario.

Después crea `prueba_estadisticas.py`, importa el módulo y llama a las tres funciones con al menos dos listas distintas. Comprueba los resultados.

**Puedes consultar:** apuntes, documentación oficial y ejemplos de uso de `sum()` y `len()`.

## Ejercicio 2 — Separar responsabilidades

Crea un pequeño programa de registro de gastos con esta estructura inicial:

```
registro_gastos/
├── principal.py
├── calculos.py
└── validaciones.py
```

Responsabilidades:

- `calculos.py`: contiene funciones que calculan el total y el promedio de una lista de gastos.
- `validaciones.py`: contiene una función que comprueba si un importe es válido según una regla que tú definas y documentes brevemente.
- `principal.py`: importa las funciones necesarias, prepara una lista de ejemplo y muestra un informe sencillo.

No es necesario crear un menú interactivo ni solicitar datos al usuario. Prioriza la organización y la claridad.

**Puedes consultar:** apuntes y documentación oficial sobre importaciones. La decisión de cómo dividir las funciones debes tomarla tú.

## Ejercicio 3 — Diferentes formas de importar

En un archivo de prueba, demuestra las siguientes formas usando tus propios módulos:

1. `import calculos` y una llamada con el prefijo del módulo.
2. `from calculos import calcular_total` y una llamada directa a la función.
3. `import calculos as calc` y una llamada usando el alias.

Puedes hacerlo en un archivo separado llamado `prueba_importaciones.py`. Añade comentarios cortos que permitan distinguir las tres variantes.

**Puedes consultar:** apuntes y documentación oficial.

## Ejercicio 4 — Evitar efectos al importar

Modifica `principal.py` para que el programa se inicie mediante una función `main()` y el bloque `if __name__ == "__main__":`.

Después crea `prueba_import_principal.py`, que importe `principal` sin ejecutar el informe completo. Comprueba que la importación no inicia el programa ni pide datos.

**Puedes consultar:** apuntes. Si lo necesitas, busca en la documentación oficial el significado de `__name__`.

## Ejercicio 5 — Diagnóstico de importaciones

Crea un archivo de texto `incidencias.md` o incluye comentarios en un archivo de prueba para responder:

1. ¿Qué revisarías si aparece `ModuleNotFoundError` al importar `calculos`?
2. ¿Por qué conviene evitar nombres como `json.py` para archivos propios?
3. ¿Qué diferencia hay entre definir una función, importarla y ejecutarla?

No provoques errores peligrosos ni cambies la configuración del equipo: describe cómo los diagnosticarías.

**Puedes consultar:** apuntes, documentación oficial y el mensaje de error.

## Criterios de revisión

- Los módulos se importan y las llamadas funcionan.
- Las funciones devuelven resultados útiles en vez de limitarse a imprimirlos.
- Las responsabilidades están separadas de manera razonable, sin crear archivos innecesarios.
- Importar `principal` no pone en marcha automáticamente el programa.
- Los nombres de archivos y las importaciones coinciden.
- Se han probado varios casos, incluido el caso de lista vacía donde corresponda.
- Las decisiones relevantes están explicadas brevemente, sin exigir documentación extensa que no se haya solicitado.

## Cuándo se considera superada

La actividad se considera superada cuando los módulos funcionan juntos, puedes explicar por qué organizaste así el programa y puedes identificar los problemas básicos de importación. Si aparece una dificultad puntual, revisaremos si se trata de un concepto no comprendido, una decisión de diseño, una interpretación del enunciado o un descuido de ejecución antes de decidir si hace falta repetir algo.

## Entrega

Sube los archivos de la actividad a tu repositorio de GitHub en la carpeta de Etapa 1 y comparte el enlace a la carpeta o a los archivos cuando termines. No modifiques ni elimines las entregas de etapas anteriores.