# 1-
# Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de
# autos que tienen disponible a la venta. Para esto se necesita saber de cada auto: la
# marca, el año del modelo y el precio (validar los tipos de datos ingresados) y
# mostrarlos por pantalla en forma secuencial y ordenada. Realizar el ejercicio sin usar
# listas primero, y despues usando listas y comparar la composición del código.
autos = [['Toyota',2000,5000],['BMW',2022,40000],['Audi',2015,30000]]
seguir = 's'

while seguir == 's':
    auto_nuevo = []
    while True:
        marca = input("Ingrese la marca del auto: ")
        if marca.isalpha():
            break
        else:
            print("Eror, no se puede ingresar numeros o caracteres especiales")

    while True:
        try:
            año = int(input("Ingrese el año del auto: "))
            if año > 1800 and año <= 2023:
                break
            else:
                print("Año invalido")
        except ValueError:
            print("Trataste de convertir algo diferente a un numero")

    while True:
        try:
            precio = float(input("Ingrese el precio del auto: "))
            if precio > 0:
                break
            else:
                print("Precio invalido")           
        except ValueError:
            print("Trataste de convertir algo diferente a un numero")
    auto_nuevo.append(marca)
    auto_nuevo.append(año)
    auto_nuevo.append(precio)
    autos.append(auto_nuevo)

    seguir = input("Desea seguir ingresando autos s/n: ")
    while seguir != 's' and seguir != 'n':
        print("Ingrese una opcion valida.")
        seguir = input("Desea seguir ingresando autos s/n: ")


for auto in autos:
    print(auto)

# marca = ''
# año = 0
# precio = 0
# seguir = 's'

# while seguir == 's':
#     try:
#         marca = input("Ingrese la marca del auto: ")
        
#         while True:
#             año = int(input("Ingrese el año del auto: "))
#             if año > 1800 and año <= 2023:
#                 break
#             else:
#                 print("Año invalido")
#         while True:
#             precio = float(input("Ingrese el precio del auto: "))
#             if precio > 0:
#                 break
#             else:
#                 print("Precio invalido")           
#     except ValueError:
#         print("Trataste de convertir algo diferente a un numero")
#     print(f"La marca del auto es {marca} del año {año} y su precio es {precio} \n")
#     seguir = input("Desea seguir ingresando autos s/n: ")
