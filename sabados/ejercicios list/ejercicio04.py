# Crea una lista vacía y pide al usuario que ingrese una palabra. Luego, muestra la primera letra de la palabra. 
#Repite este proceso hasta que el usuario ingrese una palabra que comience con la letra "z".

palabras = []
while True:
    palabra = input("Ingrese un palabra, para terminar ingrese un palabra que empiece con z: ")
    if palabra.isalpha():
        print(palabra[0])
        palabras.append(palabra)
        if palabra[0] == 'z' or palabra[0] == 'Z':
            break
    else:
        print("No es una palabra")


