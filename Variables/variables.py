# VARIABLES

##Una variable es un espacio para almacenar datos modificables, en la memoria de un ordenador
# Python usa el signo = para asignar valores a las variables. 
#   *** No es necesario declarar una variable por adelantado (o asignarle un tipo de datos)
#       al asignar un valor a una variable, se declara e inicializa la variable con ese valor. 
#       No hay forma de declarar una variable sin asignarle un valor inicial.

##En Python una variable se define con la sintaxis:
nombre_de_la_variable = valor_de_la_variable
#   variable y luego asignarle un valor.
#       <variable name> = <value>
##cada variable, tiene un nombre y un valor.
##el valor de la variable se define una sola vez.
##cada variable tiene un tipo de dato.
##Existe un tipo de variable que no es variable, es llamada:
"constante"
##la constante se utiliza para definir valores fijos que no requieran cambiar su valor.
# EJEMPLO: 
### DNI
### CODIGO POSTAL
### GRUPO SANGUINEO
### FECHA DE NACIMIENTO

### TIPOS DE VARIABLE
#------------POR SU CONTENIDO
# VARIABLE NUMERICAS
EDAD = 23
# VARIABLE LOGICAS
True
# VARIABLE ALFANUMERICAS
direccion= "Jr. Ica# 130"

#------------POR SU USO

# VARIABLES DE TRABAJO
suma= a + b

# VARIABLES CONTADORES
# VARIABLES ACUMULADORES

#           EJEMPLOS DE VARIABLES:

# Integer
a = 2
print(a)
# Output: 2

# Integer - entero
b = 9223372036854775807
print(b)
# Output: 9223372036854775807

# Floating point - Decimales
pi = 3.14
print(pi)
# Output: 3.14

# String - letras o cadena
c = 'INSTITUTO JMA'
print(c)
# Output: INSTITUTO JMA
# String
name = 'Estudiantes'
print(name)
# Output: Estudiantes

# Boolean - Verdadero o Falso
queso = True
print(queso)
# Output: True

# Empty value or null data type
x = None
print(x)
# Output: None

##---------------------Reglas para nombrar variables:
#    1. Los nombres de las variables deben comenzar con una letra o un guión bajo.
# ximena = True # valido
# _yesenia = True # valido
#           ERRORES:
#        9x = False # starts with numeral
#        => SyntaxError: invalid syntax
#        $y = False # starts with symbol
#        => SyntaxError: invalid syntax
#    2. El resto de su nombre de variable puede consistir en letras, números y guiones bajos.
#       puquio_1_jma_python = "nombre Valido"
#    3. Los nombres son mayúsculas y minúsculas.
#       x = 9
#       y = X*5
#       =>NameError: name 'X' is not defined
#Aunque no es necesario especificar un tipo de datos al declarar una variable en Python
# mientras se asigna el área necesaria en la memoria para la variable, 
# el intérprete de Python selecciona automáticamente el tipo incorporado más adecuado para ella:
#       cicloCompu = 6
#         print(type(cicloCompu))
# Output: <type 'int'>

# IMPORTANTE DATO: También puede asignar un solo valor a varias variables simultáneamente.
#       a = b = c = 1
#       print(a, b, c)
# Output: 1 1 1
