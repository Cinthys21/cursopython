#TAREA: Hacer una funcion que me retorne si una palabra es palindroma#
#ejemplo: sabemos que reconocer es una palabra palindroma#
#   reconocer, tiene 9 letrasentonces son de 0 a 8vo indice del array  #
#pedimos al usuario que ingrese una palabra para evaluar si es palindroma o no#

palabra = input("Humanito ingresa tu palabra: ")

#definimos como primer indice a y ultimo indice b, para saber el ultimo indice usamos funcion len #

a = 0
b = len(palabra) - 1

for i in range(0, len(palabra)):
    if palabra[a] == palabra [b]:
	    a += 1
	    b -= 1
    else:
	return False

return True

if espalindroma(palabra):
   print("es palindroma: " + palabra)

else:
   print("No es palindroma: " + palabra)