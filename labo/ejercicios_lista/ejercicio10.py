# 10-
# Se necesita un programa que solicite al usuario que ingrese una lista de números
# enteros de tamaño N. El programa deberá remover el valor máximo y mínimo de la
# lista y luego calcular y mostrar el promedio de los valores restantes y determinar si el
# promedio es mayor o menor que la diferencia entre el máximo y el mínimo valor
# previamente removido.
numeros = []
tam = 5
max = 0
min = 0
acumulador = 0
promedio = 0
diferencia = 0
for i in range(tam):
    while True:
        try:
            numero = int(input("Ingrese una numero:  "))
            numeros.append(numero)
            break
        except ValueError:
            print("Trataste de convertir algo diferente a un numero")

for x in range(tam):
    if x == 0 or numeros[x] < min:
        min = numeros[x]

for y in range(tam):
    if y == 0 or numeros[y] > max:
        max = numeros[y]
numeros.remove(max)
numeros.remove(min)
if max >= 0 and min >= 0:
    diferencia = max - min
else:
    diferencia = max + min
for numero in numeros:
    acumulador += numero
promedio = acumulador / len(numeros)
if promedio > diferencia:
    print(f"El promedio de la lista es {promedio} y supera la diferencia entre el max y el min")
else:
    print(f"El promedio de la lista es {promedio} y no supera la diferencia entre el max y el min")
