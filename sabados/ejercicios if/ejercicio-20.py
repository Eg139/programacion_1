#Escribir un programa que le pida al usuario que ingrese dos números enteros, y luego imprima
# "Los dos números son iguales" si los dos números son iguales, "El primer número es mayor" si el primer 
# número es mayor que el segundo, o "El segundo número es mayor" si el segundo número es mayor que el primero.
numero_a = int(input("Ingrese el primer numero: "))
numero_b = int(input("Ingrese el segundo numero: "))

if numero_a == numero_b:
    print("Los dos numeros son iguales")
elif numero_a > numero_b:
    print("El primer numero es mayor")
else:
    print("El segundo numero es mayor")