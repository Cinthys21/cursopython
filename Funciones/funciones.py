#----------------------FUNCIONES ---------------------------
# Una funcion, es la forma de agrupar expresiones y sentencias (algoritmos)
# estas realizan acciones, pero sólo se ejecutan cuando son llamadas.
# Es decir que al colocar un algoritmo dentro de una función,
# al correr el archivo, el algoritmo no será ejecutado si no se ha hecho una referencia a la función que lo contiene.
# En python se define funciones mediante la instruccion def más un nombre descriptivo.
# Seguido de parentesis de apertura y cierre.
# como toda estructura de control de python, la definicion de la funcion finaiza con dos puntos
# el algoritmo que la compone ira identado con 4 espacios.
#   def mi_funcion():
    #aqui el algoritmo
# Una funcion no es ejecutada hasta que sea invocada.
# para invocar una funcion. se le llama por su nombre:
#   def mi_funcion():
#       print "hola mundo"
#   funcion()

#cuando la funcion haga un retorno de datos, estos pueden ser asignados a una variable:
#   def funcion():
#       return "hola mundo"

#   frase = funcion()
#       print frase

#PARAMETROS:
# Un parametro es un valor que la funcion espera recibir cuando sea llamada(invocada)
#a fin de ejecutar acciones e base al mismo.
# una funcion puede esperar uno o mas parametros(van separados por coma) o ninguno.
#   def mi_funcion(nombre, apellido):
    #algoritmo
#FINALIDAD DE LA FUNCION
# Una funcion debe realizar una unica accion. reutilizable
# debe ser tan generica como sea posible.

# FUNCIONES EN PYTHON
#### INPUT()
####  Entrega como resultado el texto ingresado por el usuario mediante el teclado

#### ABS
####  Entrega el valor absoluto de su argumento

#### LEN
####  Recibe un string y entrega su largo

#### MIN y MAX
#### Entregan su minimo y maximo de sus argumentos.

#### ROUND 
####  Redondea un numero real al entero más cercano
#
#------------Construido en módulos y funciones---------------------
# PRIMERO VEAMOS QUE ES UN MODULO:
#   Un módulo es un archivo que contiene definiciones y declaraciones de Python. 
#   La función es un fragmento de código que ejecuta alguna lógica.
#   >>> pow(2,3) #8
# Para verificar la función incorporada en python podemos usar dir(). 
#   Si se llama sin un argumento, devuelve los nombres en el alcance actual. 
#   De lo contrario, devuelve una lista alfabética de nombres que comprenden;
#    el atributo del objeto dado y de los atributos a los que se puede acceder.
# >>> dir(__builtins__)
[
 'ArithmeticError',
 'AssertionError',
 'AttributeError',
 'BaseException',
 'BufferError',
 'BytesWarning',
 'DeprecationWarning',
 'EOFError',
 'Ellipsis',
 'EnvironmentError',
 'Exception',
 'False',
 'FloatingPointError',
 'FutureWarning',
 'GeneratorExit',
 'IOError',
 'ImportError',
 'ImportWarning',
 'IndentationError',
 'IndexError',
 'KeyError',
 'KeyboardInterrupt',
 'LookupError',
 'MemoryError',
 'NameError',
 'None',
 'NotImplemented',
 'NotImplementedError']

#---------------- Devolviendo valores desde funciones--------------------------------
# Las funciones pueden hacer return un valor que puede utilizar directamente:
def Dame_cinco():
 return 5
print(Dame_cinco()) # imprime el valor ue esta retornando
# Out: 5

# o tambien guarda el valor para su uso posterior:
num = Dame_cinco()
print(num) # imprime el valor que esta retornando
# Out: 5
#   o use el valor para cualquier operación:
print(Dame_cinco() + 10)
# Out: 15
# Si se encuentra return en la función, la función se cerrará inmediatamente y
# las operaciones subsiguientes no se evaluarán:
def Dame_otro_cinco():
 return 5
 print('This statement will not be printed. Ever.')
print(Dame_otro_cinco())
# Out: 5