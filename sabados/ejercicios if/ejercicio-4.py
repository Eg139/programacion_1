#Escribir un programa que le pida al usuario que ingrese dos números enteros,
# y luego imprima "El primer número es mayor" si el primer número es mayor que el segundo, 
# "El segundo número es mayor" si el segundo número es mayor que el primero, 
# o "Los dos números son iguales" si los dos números son iguales.

numero_A = int(input("Ingrese el primer numero: "))
numero_B = int(input("Ingrese el segundo numero: "))
if numero_A > numero_B:
    print("El primer numero es mayor")
elif numero_A < numero_B:
    print("El segundo numero es mayor")
else:
    print("Los dos numeros son iguales")