#Dada una lista de números, imprimir la suma de los números en la lista que son mayores que el promedio de la lista.

numeros = [7,54,102,7,-5,478,507]
promedio = 0
acumulador = 0
contador = 0
for numero in numeros:
    contador+=1
    acumulador += numero
promedio = acumulador / contador
acumulador = 0

for numero in numeros:
    if numero > promedio:
        acumulador += numero
print(acumulador)