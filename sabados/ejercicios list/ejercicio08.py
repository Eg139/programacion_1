# Crea una lista con los nombres de tus 5 libros favoritos y luego imprime solo los primeros 3 libros de la lista.
tam = 5
libros = []

for i in range(tam):
    while True:
        libro = input("Ingrese un libro: ")
        if libro.isalpha():  
            libros.append(libro)
            break
        else:
            print("Eror, no se puede ingresar numeros o caracteres especiales")

for x in range(0,3):
    print(libros[x])
                