# Crear un programa que solicite al usuario ingresar precio unitario y cantidad de 5 productos. 
# Almacenar cada valor en dos listas distintas.
# Luego imprimir el precio total de cada artículo.
productos = []
precios = []

tam = 5

for x in range(tam):        
    while True:
        try:   
            precio =  int(input(f"Ingrese el precio: "))
            precios.append(precio)
            if precio > 0:
                break
            else:
                print("El precio no puedes er 0 ni negativo")
        except ValueError:
            print("Trato de convertir algo diferente a un numero")

    while True:
        try:   
            producto =  int(input(f"Ingrese la cantidad de productos: "))
            productos.append(precio)
            if producto > 1:
                break
            else:
                print("Debe ingresar una cantidad mayor a uno")
        except ValueError:
            print("Trato de convertir algo diferente a un numero")

for z in range(len(productos)):
    print(f"EL precio total del producto es: {productos[z] * precios[z]}")