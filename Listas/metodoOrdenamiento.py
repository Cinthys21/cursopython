#                       Métodos de ordenamiento
# Ordenar una lista en reversa (invertir orden)
# Método: reverse()
nombres_masculinos)=['Ricky', 'Alvaro', 'David', 'Jacinto', 'Ricky', 'Jose', 'Jose']
nombres_masculinos.reverse() 
print nombres_masculinos 
#se imprimirá asi: ['Jose', 'Jose', 'Ricky', 'Jacinto', 'David', 'Alvaro', 'Ricky'] 

#                   Ordenar una lista en forma ascendente
# Método: sort()
nombres_masculinos.sort() 
print nombres_masculinos 
#Se ordenará asi:
# ['Alvaro', 'David', 'Jacinto', 'Jose', 'Jose', 'Ricky', 'Ricky'] 

#                   Ordenar una lista en forma descendente
# Método: sort(reverse=True)
nombres_masculinos.sort(reverse=True) 
print nombres_masculinos 
#ASI: ['Ricky', 'Ricky', 'Jose', 'Jose', 'Jacinto', 'David', 'Alvaro']