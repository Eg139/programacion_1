#Dado un número entero n, imprimir la secuencia de números perfectos menores o iguales a n.

numero = 6
for divisor in range(1,numero+1):
    acumulador = 0
    for i in range(1,divisor):        
        if divisor % i == 0:
            acumulador += i
    if acumulador == divisor:
        print(divisor)
