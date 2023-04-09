# La división de higiene está trabajando en un control de stock para productos
# sanitarios. Debemos realizar la carga de
# una compra de productos de prevención de contagio, de cada una debe obtener los
# siguientes datos:
# · El tipo ("barbijo", "jabón" o "alcohol")
# · El precio
# · La cantidad de unidades
# · La marca
# · El fabricante
# Se debe informar los datos de la compra procesados para poder iniciar el control de
# stock.
tipo = ""
precio = 0
unidades = 0
marca = ""
fabricante = ""

try:
    tipo = input("Ingrese el tipo de producto (barbijo, jabón o alcohol): ")
    precio = float(input("Ingrese el precio de producto: "))
    unidades = int(input("Ingrese las unidades de producto: "))
    marca = input("Ingrese la marca de producto: ")
    fabricante = input("Ingrese el fabricante de producto: ")
except ValueError:
    print("Trataste de convertir algo diferente a un numero")

else:
    print(f"El tipo de producto es {tipo} con un precio de {precio}, se ingreso la cantidad de {unidades} unidades de la marca {marca} fabricada por {fabricante}")
    # unidades = int(input("Ingrese las unidades de producto: "))
    # marca = input("Ingrese la marca de producto: ")
    # fabricante = input("Ingrese el fabricante de producto: ")
    # seguir = input("Desea continuar s/n  ")

# print(f"El tipo de producto es {tipo} con un precio de {precio}, se ingreso la cantidad de {unidades} unidades de la marca {marca} fabricada por {fabricante}")