#--------------------Tuplas
# Una tupla es una variable que permite almacenar varios datos inmutables (no pueden
#ser modificados una vez creados) de tipos diferentes: 
mi_tupla = ('computacion', 15, 2.8, 'otro dato', 25) 
#Se puede acceder a cada uno de los datos mediante su índice correspondiente, siendo 0
# (cero), el índice del primer elemento: 
print mi_tupla[1] # Salida: 15 
# También se puede acceder a una porción de la tupla, indicando (opcionalmente) desde el
# índice de inicio hasta el índice de fin: 
print mi_tupla[1:4] # Devuelve: (15, 2.8, 'otro dato') 
print mi_tupla[3:] # Devuelve: ('otro dato', 25) 
print mi_tupla[:2] # Devuelve: ('computacion', 15) 

# Otra forma de acceder a la tupla de forma inversa (de atrás hacia adelante), es colocando
# un índice negativo: 
print mi_tupla[-1] # Salida: 25 
print mi_tupla[-2] # Salida: otro dato

# las tuplas van entre parentesis
# las listas van entre corchetes
# los diccionarios van entre llaves {}

