#TAREA: Hacer una funcion que me retorne los n numeros de FIBONACCI, segun pida el usuario#
#definimos las variables a operar#
x=0
y=1
z=0

#aplicamos while#
while True:
#pediremos al ususario que ingrese un numero para ejecutar la serie fibonacci#
   n=int(input("Humanito ingresa un numero mayor a 1: "))
   if n>1:
       break
print("1",end=" ")
#usaremos for para hacer el calculo matematico con las variables que ya definimos#
for i in range(0,n):
    z=x+y
    print(f"{z}",end=" ")
    x=y
    y=z
print(" ")