# Dado un número entero n, imprimir la suma de todos los números impares menores o iguales a n.
numero = 9
i= 0
acumulador = 0
while i <= numero:
    if i % 2 != 0:
        acumulador += i
    i +=1
print(acumulador)
