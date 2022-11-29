#------------- TIPOS DE DATOS -----------------------------

##este es un tipo de dato numerico
9
##este es un tipo de dato float
9.5
##este es un tipo de dato numerico grande
9E
##este es un tipo de dato float
3.403456789
##este es un tipo de dato booleano
##dos tipos:
True
False
#-------------MUTABLES E INMUTABLES-------------------------
#   Ejemplos de tipos de datos inmutables:
#   int , long , float , complex
#   str
#   bytes
#   tuple
#   frozenset
#   Ejemplos de tipos de datos mutables:
#   bytearray
#   list
#   set
#   dict

# ---------PYTHON POSEE ADEMÁS 3 TIPOS MÁS COMPLEJOS:
# Tuplas, listas y diccionarios.
# Estos pueden almacenar colecciones de datos de diversos tipos.
# Se diferencian por su sintaxis y por la forma en la cual los datos pueden ser manipulados.
#   @Tuplas
#Permite almacenar varios datos inmutables.
#No pueden ser modificados una vez que han sido creados.
#   mi_tupla=("cadena de texto", 15, 2.8, "otro dato", 25)
#se puede acceder a cada uno de los datos mediante su indice.
#   print mi_tupla[1]  #salida:15

#   @listas
#Las listas permiten modificar los datos una vez creados.
#   mi_lista = ["cadena de texto", 15, 2.8, "otro dato", 25]
#se puede acceder a cada uno de los datos mediante su indice.

#   @diccionarios
#permiten utilizar una clave para declarar y acceder a un valor.
#   mi_diccionario = {"clave_1":valor_1, "clave_2":valor_2}
#   print mi_diccionario["clave_2"] #salida:valor_2
#El diccionario permite modificar los valores.
#Permite modificar cualquier entrada.

#   Convertir entre tipos de datos
#   Puede realizar la conversión explícita de tipos de datos.
#   Por ejemplo, '123' es de tipo str y se puede convertir en entero usando la función int .
a = '123'
b = int(a)
#   La conversión de una cadena flotante como '123.456' se puede hacer usando la función float .
a = '123.456'
b = float(a)
c = int(a) # ValueError: invalid literal for int() with base 10: '123.456'
d = int(b) # 123
#   También se puede convertir secuencias o tipos de colección.
a = 'hello'
list(a) # ['h', 'e', 'l', 'l', 'o']
set(a) # {'o', 'e', 'l', 'h'}
tuple(a) # ('h', 'e', 'l', 'l', 'o')

#-------------------------TIPO DE DATO COMPLEJO
# las tuplas van entre parentesis
# las listas van entre corchetes
# los diccionarios van entre llaves {}
