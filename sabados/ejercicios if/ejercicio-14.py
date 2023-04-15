#Escribir un programa que le pida al usuario que ingrese un número entero, y luego imprima
# "El número es múltiplo de 4 y de 6" si el número es múltiplo de 4 y de 6, o "El número no
# es múltiplo de 4 y de 6" si el número no es múltiplo de 4 y de 6.
numero = int(input("Ingrese un numero: "))
if numero % 4 == 0 and numero % 6 == 0:
    print("El numero es multiplo de 4 y 6")
else:
    print("El numero no es multiplo de 4 y 6")