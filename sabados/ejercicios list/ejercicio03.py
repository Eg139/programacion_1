# Crea una lista vacía y pide al usuario que ingrese números enteros hasta que ingrese un número negativo. 
#Luego, muestra la suma de todos los números ingresados.

numeros = []
acumulador = 0
while True:
    try:
            numero = int(input("Ingrese un numero, para terminar ingrese un numero negativo: "))
            numeros.append(numero)
            if numero < 0:
                 break
    except ValueError:
        print("Trataste de convertir algo diferente a un numero")
for numero in numeros:
     acumulador += numero

print(acumulador)

