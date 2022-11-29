#                   Métodos de búsqueda
# Contar cantidad de apariciones elementos
# Método: count(elemento)
nombres_masculinos = ["Alvaro", "Miguel", "Edgardo", "David", "Miguel"] 
nombres_masculinos.count("Edgardo") 
#sera asi: 1
nombres_masculinos = ["Alvaro", "Miguel", "Edgardo", "David", "Miguel"] 
nombres_masculinos.count("Miguel") 
#sera asi: 2 

#                   Obtener número de índice
# Método: index(elemento[, indice_inicio, indice_fin])
nombres_masculinos.index("Williams") 
# el resultado será:  
nombres_masculinos.index("Claudio", 2, 5) 
# el resultado será: 