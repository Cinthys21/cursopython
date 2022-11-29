#------------------ESTRUC CICLO ----------------
## USAREMOS 2:
#               FOR Y WHILE.

###-----------------------FOR
## SE USA PARA RECORRER LOS ELEMENTOS DE UN OBJETO "iterable"
## un objeto iterable puede ser: 
##   *una lista
##   *una tupla
##   *un conjunto
##   *un diccionario.
## for recorre los elementos del objeto y ejecuta un bloque de codigo.
## su sintaxis es:
#   for <elem> in <iterable>;
#       <tu codigo>
## aqui ELEM es la variable en cada paso del buble.
## el bucle finaliza cuando ha recorrido todos los elementos.
# For permite iterar sobre una variable compleja, como lista o tupla.
# ejemplo:Por cada nombre en mi_lista imprimir nombre.
#   mi_lista = ["juan", "Antonio", "Pedro", "Herminio"]
#   for nombre in mi_lista:
#    print nombre
    
###-----------------------WHILE
#       BUCLE WHILE
# Ejecuta una misma acción
"mientras que"
# mientras una condición se cumpla.
# EJEMPLO:
# Mientras que año sea menor o igual a 2022, imprimir "informes del Año año" 
#   anio = 2001
#   While anio <= 2012
#     Print "informes del año", str(anio)
#     anio +=1
# Si el valor que condiciona la iteración no es numérico
# Se puede usar estructura de control anidada dentro del bucle.
# se frenará la ejecución cuando el condicional deje de cumplirse.
# Se usa la palabra break:
# EJEMPLO
#   While True:
#     nombre = raw_input("indique su nombre")
#  if nombre:
#     break
# Este condicional anidado verifica si la variable nombre es verdadera.
# La variable solo es verdadera su el usuario tipea un texto en la pantalla
# Si es verdadera el bucle para(break) sino, seguirá ejecutandose
#esto ocurirá hasta que el usuario ingrese un texto en pantalla.