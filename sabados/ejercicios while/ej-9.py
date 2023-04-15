# Dado un número entero n, imprimir todos los números impares menores o iguales a n.
numero = 25
i= 0
    
while i <= numero:
    if i % 2 != 0:
        print(i)
    i += 1
