# Dado un número entero n, imprimir la suma de todos los números pares menores o iguales a n.
numeros = [2,5,876,56,23,12,5,8]
i= 0
acumulador = 0
while i < len(numeros):
    if numeros[i] % 2 == 0:
        acumulador += numeros[i]
    i += 1
print(acumulador)
