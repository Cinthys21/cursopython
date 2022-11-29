#   Conversión de tipos LISTA/TUPLA y viceversa
# En el conjunto de las funciones integradas de Python, podemos encontrar dos funciones
# que nos permiten convertir listas en tuplas y viceversa.
# Estas funciones pueden ser muy útiles cuando por ejemplo, una variable declarada como
# tupla, necesita ser modificada en tiempo de ejecución, para lo cual, debe convertirse en
# una lista puesto que las tuplas, son inmutables. Lo mismo sucede en el caso contrario:
# una variable que haya sido declarada como lista y sea necesario convertirla en una colección inmutable.
#                   TUPLA A LISTA:
tupla = (1, 2, 3, 4) 
tupla 
(1, 2, 3, 4) 
list(tupla) 
# EL RESULTADO SERA: [1, 2, 3, 4]
 
#                   LISTA A TUPLA:
lista = [1, 2, 3, 4] 
lista 
[1, 2, 3, 4] 
tuple(lista) 
# EL RESULTADO SERA: (1, 2, 3, 4) 