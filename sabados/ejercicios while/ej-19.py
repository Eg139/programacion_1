# Dada una lista de números, imprimir todos los números que son mayores que el número anterior en la lista.
numeros = [25,-123,12,-45,-234,90, 22]
i= 0
numero_anterior = 0

while i < len(numeros):
    if numeros[i] > numero_anterior and i > 0:
        print(numeros[i])
    numero_anterior = numeros[i]
    i += 1
