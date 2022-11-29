#------------------ESTRUC DECISION ----------------------------------------
# LAS ESTRUCTURAS DE CONTROL DE FLUJO CONDICIONALES
# Se definen mediante el uso de tres palabras clave reservadas.
# VEREMOS 3 ESTRUCTURAS DE DECISION
#   IF  --- ELIF -----IF ELSE.
## IF = si
## ELIF = Sino, si.
## ELSE = sino
# EJEMPLO: 
#Si semáforo esta en verde, cruzar la calle. Sino, esperar.
#   if semaforo == verde:
#       Print "cruzar la calle"
#   else:
#       print "esperar"
# EJEMPLO:
#Si gasto hasta s/100, pago con efectivo. 
#Sino, si gasto más de s/100 pero menos de s/300,
#pago con targeta débito.Sino,ago con targeta de crédito.
#   if compra <=100:
#       print "pago en efectivo"
#   elif compra > 100 and compra < 300:
#       print "pago con tarjeta debito"
#   else:
#       print "pago con tarjeta credito"

# EJEMPLO: Si la compra es mayor a s/100, obtengo descuento del 10%

#   importe_a_pagar = total_compra
#   if total_compra > 100:
#    tasa_descuento = 10
#    importe_descuento = total_compra * tasa_descuento/100
#    importe_a_pagar = total_compra - importe_descuento