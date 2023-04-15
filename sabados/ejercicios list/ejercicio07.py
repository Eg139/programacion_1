# Crea una lista con los nombres de tus 3 deportes favoritos y luego agrega otro deporte al final de la lista.


deportes = ["tenis","basquet","natacion"]

while True:
    deporte = input("Ingrese un nuevo deporte: ")
    if deporte.isalpha():  
        deportes.append(deporte)
        break
    else:
        print("Eror, no se puede ingresar numeros o caracteres especiales")

# print(deportes)
                
