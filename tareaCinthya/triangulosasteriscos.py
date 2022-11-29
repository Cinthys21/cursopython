# Cinthya
n=int(input("Cinthya introduce el numero de niveles "))
# el numero de asteriscos va conforme al numero de reglones
for i in range(n+1):
    print("*"*i)

# AHORA UN TRIANGULO INVERTIDO
#USAMOS CICLO FOR
for i in range(n+1):
    espacios=n-i
    print(" "*espacios+"*"*i)

# AHORA UN TRIANGULO CENTRADO
for i in range(n+1):
    espacios=n-i
    # Es como el anterior, solo añadir un espacio al asterisco
    print(" "*espacios+"* "*i)