# Dada una lista de números, imprimir todos los números que son mayores que el promedio de la lista.
numeros = [2,5,876,56,23,12,5,8, 200]
i = 0
k = 0
acumulador = 0
while i < len(numeros):
    acumulador += numeros[i]
    i+=1
promedio = acumulador / i


while k < len(numeros):
    if numeros[k] >= promedio:
        print(numeros[k])
    k += 1