# Respuesta

Para el ejercicio 5
1. Necesitaba mantener:
- La suma de los positivos
- La cantidad de negativos
- El valor maximo
- El valor minimo

2. Se inicializa antes del recorrido:
- suma_positivos
- negativos
- maximo
- minimo

3. Dentro del recorrido cambia todos los valores de las variables si cumplen con las condiciones.

4. Cada vez que aparece un valor que cambie el resultado se actualiza. Ejemplo si aparece un numero mayor que el maximo actual, el maximo actual se convierte en ese numero, en caso de no ser mayor se evalua el siguiente numero. Algo similar sucede para minimo. En lo negativos es diferentes ya que solo se evalua si es o no, en caso de serlo aumenta en 1 el contador. Y para suma se va acumula los positivos, si es positivo se suma al valor actual de la suma de positivos y ese pasa a ser el valor actual de suma_positivos

5. Considere listas vacias, listas con 1 solo elemento y listas donde todos los elementos son iguales
