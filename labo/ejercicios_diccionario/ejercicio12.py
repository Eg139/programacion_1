# Listas de diccionarios.
# 12. Crear una lista de diccionarios que contenga información sobre 5 libros, incluyendo
# título, autor, editorial, año de publicación, y género. Luego, pedir al usuario que ingrese
# un género y mostrar en pantalla todos los títulos de ese género con todos los datos.


tam = 5
libros = []
for x in range(tam):
    diccionario_aux = {}

    while True: 
            aux_titulo = input("Ingrese el titulo: ")
            if aux_titulo.isalpha():
                diccionario_aux["titulo"] = aux_titulo
                break
            else:
                 print("Ingreso un elemento invalido")    
    while True: 
            aux_nombre = input("Ingrese el nombre del autor nombre: ")
            if aux_nombre.isalpha():
                diccionario_aux["nombre"] = aux_nombre
                break
            else:
                 print("Ingreso un elemento invalido")
    while True: 
            aux_editorial = input("Ingrese el nombre de la editorial: ")
            if aux_editorial.isalpha():
                diccionario_aux["editorial"] = aux_editorial
                break
            else:
                 print("Ingreso un elemento invalido")    
    while True:
        try:   
            aux_anio_publicacion = int(input("Ingrese el año de publicacion: "))
            if aux_anio_publicacion > 0:
                diccionario_aux["publicacion"] = aux_anio_publicacion
                break
            else:
                print("La edad mo puede ser 0 ni negativa")
        except ValueError:
            print("Trato de convertir algo diferente a un numero")   
    while True: 
            aux_genero = input("Ingrese el genero: ")
            if aux_genero.isalpha():
                diccionario_aux["genero"] = aux_genero
                break
            else:
                 print("Ingreso un elemento invalido")   
    libros.append(diccionario_aux)

while True: 
        genero_pedido = input("Ingrese el genero de los libros que busca: ")
        if genero_pedido.isalpha():
            break
        else:
                print("Ingreso un elemento invalido")   

print(f"Listado de libros del genero {genero_pedido}")
print("Titulo\t Autor\t Editorial\t Año de Publicacion")
for libro in libros:
    if libro["genero"] == genero_pedido:
        print(f"{libro['titulo']}\t {libro['nombre']}\t {libro['editorial']}\t {libro['publicacion']:4d}\t")