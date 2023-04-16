# Crea una lista con los nombres de tus 3 películas favoritas y luego imprime los elementos en orden inverso (sin utilizar el método reverse())
tam = 3
peliculas = []

for x in range(tam):
    while True:
        pelicula = input("Ingrese un pelicula: ")
        if pelicula.isalpha():
            peliculas.append(pelicula)
            break
        else:
            print("No es un texto valido")



for z in range(tam-1,-1,-1):
    print(peliculas[z])