#Escribir un programa que le pida al usuario que ingrese su edad, y luego imprima "Eres un niño" 
# si la edad es menor a 12, "Eres un adolescente" si la edad está entre 12 y 17 inclusive, "Eres un adulto" 
# si la edad está entre 18 y 64
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Eres un niño")
elif edad >= 12 and edad<=17:
    print("Eres un adolescente")
elif edad >= 18 and edad <= 64:
    print("Eres un adulto")