#Dado un número entero n, imprimir la suma de los números pares menores o iguales a n.

numero = 8
acumulador = 0

for i in range(0, numero+1):
    if i % 2 == 0:
        acumulador += i
print(acumulador)