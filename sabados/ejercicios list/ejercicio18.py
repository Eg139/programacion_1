# Solicitar al usuario números enteros hasta que ingrese el 0. Almacenar los números en una lista y luego imprimir el mayor (sin utilizar la función max())

numeros = []
maximo = 0

while True:
    try:   
        numero1 =  int(input(f"Ingrese un numero, para terminar ingrese 0: "))
        numeros.append(numero1)
        if numero1 == 0:
            break
    except ValueError:
        print("Trato de convertir algo diferente a un numero")
        

for x in range(len(numeros)):
    if x == 0 or numeros[x] > maximo:
        maximo = numeros[x]
    
print(maximo)
