#Dada una lista de números, imprimir la cantidad de números pares en la lista.
numeros = [7,54,102,7,-5,478,507]
contador = 0
for numero in numeros:
    if numero % 2 == 0 :
        contador += 1
print("La cantidad de numeros pares es de: ",contador)
