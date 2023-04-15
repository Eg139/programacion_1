#Dada una lista de números, imprimir el número más pequeño de la lista.

numeros = [7,54,102,7,-5,478,507]
flag = 0

for i in numeros:
    if flag == 0 or i < minimo :
        minimo = i
        flag = 1
        
print("El numero mas grande es: ",minimo)