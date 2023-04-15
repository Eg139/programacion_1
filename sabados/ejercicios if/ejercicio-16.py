#Escribir un programa que le pida al usuario que ingrese su nombre y su edad, y luego imprima
# "Eres adolescente" si la edad está entre 13 y 17 inclusive, "Eres adulto" si la edad está 
# entre 18 y 64 inclusive, o "Eres adulto mayor" si la edad es mayor o igual a 65.
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
if edad >= 13 and edad <= 17:
    print("Eres un adolescente")
elif edad >= 18 and edad <= 64:
    print("Eres un adulto")
elif edad >= 65:
    print("Eres un adulto mayor")