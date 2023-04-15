# Dada una lista de números, imprimir la suma de todos los elementos de la lista.
numeros = [2,32,453,12,23,10,9,11]
longitud = len(numeros)
acumulador = 0
i = 0
while i < longitud:
    acumulador += numeros[i]
    i += 1
print(acumulador)

