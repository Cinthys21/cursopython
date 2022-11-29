#-----------------EJERCICIO EN CLASE-----------------------------
casaCinthya=[
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
]
# QUEREMOS ESTE RESULTADO
# i0 = [0,1,1,1,0]
# i1 = [1,0,1,0,1]
# i2 = [1,1,0,1,1]
# i3 = [1,0,1,0,1]
# i4 = [0,1,1,1,0]

contador=4
for i in range(0,len(casaCinthya)):
    for j in range (0,len(casaCinthya[i])):
        casaCinthya[i][j] ='1'
        casaCinthya[i][i]='0'
        casaCinthya[i][contador]='0'
    if contador>=0:
            contador=contador-1
    print(casaCinthya[i], end='\n')