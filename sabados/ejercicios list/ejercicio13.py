# Crea una lista de números y encuentra el promedio de todos los números en la lista.
acumulador = 0
promedio = 0
numeros = [100,11,32,4,8]

# while True:
#     try:
#         numero_aux = int(input("Ingrese un nuevo numero: "))
#         break
#     except ValueError:
#         print("Trataste de convertir algo diferente a un numero")
for numero in numeros:
    acumulador += numero

promedio = acumulador / len(numeros)
print(f"El promedio es {promedio}")