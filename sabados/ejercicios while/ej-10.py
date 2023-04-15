# Dada una lista de números, imprimir la cantidad de números pares en la lista.
numeros = [25,123,12,45,234,90]
i= 0
contador = 0
 
while i < len(numeros):
    if i % 2 == 0:
        contador +=1
    i += 1
    
print(contador)
 