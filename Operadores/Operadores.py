#--------------OPERADORES ------------------------

##LOS OPERADORES.
# OPERADORES ARITMETICOS:
#Los operadores aritmeticos permiten realizar operaciones matematicas
# entre variables y constantes
## son:
# + suma
# - resta
# * multiplicación
# / divisiOn
# % modulo (el resto de la division entera)

# PRIORIDAD DE LOS OPERADORES ARITMETICOS:
## 1.- **Exponenciación
## 2.- *, /, %,
## 3.- +, -

# Se usan para describir a evaluación a realizar sobre una condición.
# especificamente OPERADORES RELACIONALES:
# Se usan para establecer una relacion entre dos valores
# compara estos valores entre si y esta comparacion produce un resultado de certeza o falsedad (v o f)
# comparan valores del mismo tipo sea numerico o cadenas
# tienen el mismo nivel de prioridad en su evaluación.
# tienen menor prioridad que los operadores aritmeticos.

#  SIMBOLO   SIGNIFICADO     EJEMPLO       RESULTADO
#     ==       Igual que      5==7         Falso
#     !=     Distinto que   rojo!=verde    Verdadero
#     <      Menor que         8<12        verdadero
#     >      Mayor que         12>7        Falso
#     <=     Menor=que       12<=12        Verdadero
#     >=     Mayor=que       4>=5          Falso

# OPERADORES LOGICOS:
# Para evaluar más de una condición simultáneamente.
# son: y, or(o), xor(o excluyente), not.
# Los operadores AND y OR son binarios.
# NOT es unitario.

# OPERADORES DE TEXTO
# Los operadores + y * tienen otras interpretaciones cuando se trata de STRINGS
### + ES EL OPERADOR DE CONCATENACION
#   <<<"PERRO"+"GATO"
#   "PERROGATO"
### * ES EL OPERADOR DE REPETICION DE STRINGS
# EJEMPLO:
#   "WAKA"*3
#   "WAKAWAKAWAKA"

# PROCEDENCIA DE OPERADORES
# Orden en que deben ser evaluadas las operaciones de una expresion:
# De menor a mayor precedencia:

#  or
#  and
#  not
#  <, <=, >, >=, !=, ==
#  +, -
#  *, /, %
#  **, (), -, +