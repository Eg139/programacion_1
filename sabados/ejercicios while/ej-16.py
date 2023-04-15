# Dada una lista de números, imprimir todos los números que son múltiplos de 3.
numeros = [25,-123,12,-45,-234,90, 22]
i= 0

while i < len(numeros):
    if numeros[i] % 3 == 0:
        print(numeros[i])
    i += 1