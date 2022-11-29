#                   Concatenación simple de colecciones
# En Python es muy simple unir varias colecciones de un mismo tipo. 
# Simplemente, se requiere utilizar el operador suma (+) para lograrlo:
Cinthya1 = [1, 2, 3, 4] 
Cinthya2 = [3, 4, 5, 6, 7, 8] 
Cinthya3 = lista1 + lista2 
# Cinthya3 
# [1, 2, 3, 4, 3, 4, 5, 6, 7, 8] 
tupla1 = (1, 2, 3, 4, 5) 
tupla2 = (4, 6, 8, 10) 
tupla3 = (3, 5, 7, 9) 
tupla4 = tupla1 + tupla2 + tupla3 
# tupla4 
# (1, 2, 3, 4, 5, 4, 6, 8, 10, 3, 5, 7, 9) 

#                               Valor máximo y mínimo
# Podemos obtener además, el valor máximo y mínimo tanto de listas como de tuplas:
max(tupla4)  # 10 
max(tupla1)  # 5 
min(tupla1)  # 1 
max(Cinthya3)  # 8 
min(Cinthya1)  # 1 