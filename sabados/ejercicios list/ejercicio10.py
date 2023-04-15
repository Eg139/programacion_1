# Crea una lista de palabras y muestra las palabras que tienen más de 5 letras.

tam = 5
palabras = []
for x in range(tam):
    while True:
        palabra = input("Ingrese un palabra: ")
        if palabra.isalpha():
            palabras.append(palabra)
            break
        else:
            print("No es una palabra")
for palabra in palabras:
    if len(palabra) >= 5:
        print(palabra)
