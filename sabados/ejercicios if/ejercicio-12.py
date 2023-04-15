#Escribir un programa que le pida al usuario que ingrese dos números enteros, y luego 
# imprima "El primer número es positivo" si el primer número es mayor que cero, "El 
# segundo número es positivo" si el segundo número es mayor que cero, o
# "Ambos números son negativos" si los dos números son negativos.

numero_a = int(input("Ingrese el primer numero entero: "))
numero_b = int(input("Ingrese el segundo numero entero: "))
contador = 0

if numero_a > 0:
    print("El primer numero es positivo")
else:
    contador += 1
    
if numero_b > 0:
    print("El segundo numero es positivo")
else:
    contador += 1
        
if contador == 2:
    print("Ambos numeros son negativos")
    