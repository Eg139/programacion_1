# Crear un programa que solicite al usuario ingresar: nombre del cantidad, cantidad y precio unitario.
# Guardar los datos en 3 listas distintas. Solicitar cantidades hasta que el nombre del cantidad sea ‘xxx’.
# Luego imprimir la lista de artículos con el siguiente formato:
# nombre_articulo	cantidad	$ precio_unitario 	$ total
# 	Ejemplo:
# 	alfajor capitan del espacio		6	$ 150		$ 900
# 	…

productos = []
cantidades = []
precios = []
flag = False
tam = 5

for x in range(tam):
    while True: 
            producto =  input(f"Ingrese el nombre del producto(Para dejar de ingresar productos ingrese xxx): ")
            if producto.isalpha():
                if producto == 'xxx':
                    flag = True
                    break
                else:
                    productos.append(producto)
                    break
            else:
                 print("Ingreso un elemento invalido")

    if flag:
        break
    else:
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
                cantidad =  int(input(f"Ingrese la cantidad de cantidades: "))
                cantidades.append(precio)
                if cantidad > 1:
                    break
                else:
                    print("Debe ingresar una cantidad mayor a uno")
            except ValueError:
                print("Trato de convertir algo diferente a un numero")


print(f"\n nombre_articulo  cantidad  $ precio_unitario  $ total")
for z in range(len(cantidades)):
    print(f" {productos[z]}          {cantidades[z]}         {precios[z]}     $ {precios[z] * cantidades[z]}")