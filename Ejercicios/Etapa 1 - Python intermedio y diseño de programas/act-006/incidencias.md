# Respuesta

1. Si aparece un ModuleNotFoundError primero revisaria el nombre del archivo y el import para asegurar que no haya errores de ortografia. Luego revisaria a ver si la ruta de importacion es la correcta. Revisar despues si el programa y si el modulo se encuentran accesible para para Python. Luego si el interprete de Python es el correcto para el programa. De no ser nada de esto asumiria que es algun error en el entorno de python o de configuracion.

1. Conviene evitar nombres tipo json.py en los archivos propios porque puede chocar con modulos de la biblioteca estandar, tambien tendria cuidado a la hora de trabajar con modulos de terceros para que no se solape con mis archivos y cause errores inesperados

1. La diferencia esta en que cuando se define una funcion se declara el codigo y funcionamiento de esta. Al importar se permite acceder su funcionamiento en otro archivo donde no se declaro. Y al ejecutarla aunque sea redundante se ejecuta la funcion o sea se llama esto ejemplo ```calcular_total([3, 4, 5])```

