# Crea una lista con los nombres de 5 ciudades y luego imprime el último elemento de la lista.
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

print(palabras[len(palabras)-1])

