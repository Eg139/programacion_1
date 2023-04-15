#Escribir un programa que le pida al usuario que ingrese un número entero positivo, y luego imprima 
# "El número es primo" si el número es primo, o "El número no es primo" si el número no es primo.
numero = int(input("Ingrese un numero entero positivo: "))
primo = True
if numero > 0:    
    for i in range(2,numero):
        if numero % i == 0:
            primo = False
            break
    if primo == False:
        print("El", numero ,"no es primo")
    else:
        print("El",numero,"es primo")
else:
    print("No es un numero positivo.")
