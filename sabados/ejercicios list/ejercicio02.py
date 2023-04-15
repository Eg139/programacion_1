# Crea una lista con 5 números enteros. Luego solicita un nuevo número y reemplaza el tercer elemento de la lista por el número ingresado. 
#Finalmente imprime todos los números

numeros = []
for i in range(5):
    while True:
        try:
                numero = int(input("Ingrese un numero: "))
                numeros.append(numero)
                break
        except ValueError:
            print("Trataste de convertir algo diferente a un numero")

while True:
    try:
            numero = int(input("Ingrese el nuevo numero: "))
            numeros[2] = numero
            break
    except ValueError:
        print("Trataste de convertir algo diferente a un numero")    

for numero in numeros:
    print(numero)