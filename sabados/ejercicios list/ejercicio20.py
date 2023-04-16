# A partir de la lista: [1,80,5,0,15,-5,1,79] determinar, el mayor, el menor, el promedio y la suma total de todos los elementos

numeros = [1,80,5,0,15,-5,1,79]
maximo = 0
minimo = 0
promedio = 0
acumulador = 0

for x in range(len(numeros)):
    if x == 0 or numeros[x] > maximo:
        maximo = numeros[x]
    if x == 0 or numeros[x] < minimo:
        minimo = numeros[x]
    acumulador += numeros[x]
promedio = acumulador / len(numeros)
print(f"El maximo es {maximo}")
print(f"El minimo es {minimo}")
print(f"La suma de todos los numeros es {acumulador}")
print(f"El promedio es {promedio}")