# Crea una lista de palabras y pide al usuario que ingrese una palabra. 
# Luego, muestra todas las palabras de la lista que tienen la misma longitud que la palabra ingresada.

tam = 5
palabras = []
palabra_nueva = ""
for x in range(tam):
    while True:
        palabra = input("Ingrese un palabra: ")
        if palabra.isalpha():
            palabras.append(palabra)
            break
        else:
            print("No es una palabra")
while True:
    palabra_nueva = input("Ingrese un palabra nueva: ")
    if palabra_nueva.isalpha():
        break
    else:
        print("No es una palabra")

for palabra in palabras:
    if len(palabra) == len(palabra_nueva):
        print(palabra)