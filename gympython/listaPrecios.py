# escribir funcion que almacene precios y muestre por pantalla el menor y el mayor de ellos.
Zapatos= (50, 75, 46, 22, 80, 65, 8)
# obteniendo el precio mayor:
def precio_max():
    return max(Zapatos) 
print ("el precio más caro de zapatos es: ",precio_max())

def precio_min():
    return min(Zapatos) 
print ("el precio más barato de zapatos es: ",precio_min())