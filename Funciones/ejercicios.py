## escriba una funcion en python que 
# acepte una lista y genere otra lista, eliminando los duplicados numeros.

numerosDup = [1,1,2,2,3,4,4,5,6,6]
def delDuplicate(numerosDup):
    unicoNumero = []
    for numero in numerosDup:
        if numero not in unicoNumero:
            unicoNumero.append(numero)
    return unicoNumero 
print (delDuplicate(numerosDup))

# ESCRIBA una funcion que acepte una lista y genera otra con los numeros pares
#y otra con los numeros pares
def numPar (array):
    newArray=[]
    cinthya=set(array)
    for n in cinthya:
        if n % 2 == 0:
            newArray.append(n)
    return newArray
ArrayA = [2,4,5,8,6,3,21]
print(numPar(ArrayA))



#TAREA: escriba una funcion que acepte una lista y genere otra lista con los numeros primos
#array[3,4,5,6,7,8,9,10,13]
