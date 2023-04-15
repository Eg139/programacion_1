
#Escribir un programa que le pida al usuario que ingrese un número entero positivo,
# y luego imprima "El número ingresado es positivo" si el número es mayor que cero, 
# o "El número ingresado es cero o negativo" si el número es menor o igual a cero.


numero = int(input("Ingrese un numero entero positivo:  "))
if numero > 0:
    print("El Ingresado es positivo")
else:
    print("El numero ingresado es 0 o negativo")
