#-----------------EJERCICIO EN CLASE-----------------------------
casacinthya=[
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
]
for i in range(0,len(casacinthya)):
    for j in range(0,len(casacinthya[i])):
        casacinthya[i][j]="1"
        casacinthya[i][i]="0"
print(casacinthya)