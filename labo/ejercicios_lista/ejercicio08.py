# 8-
# Escribir un programa que le pida al usuario ingresar una lista de nombres de personas
# (previamente validada) y luego le pidan 1 solo nombre en específico. Se debe buscar
# el nombre especifico en la lista de nombres y si esta presente el programa deberá
# imprimir la posición del nombre en la lista, la posición de memoria donde se encuentra
# ese nombre y la cantidad de caracteres que tiene el nombre, si no se encuentra, se
# deberá informar por pantalla.
nombres = []
tam = 5
nombre_buscado = ""
for x in range(tam):
    while True:
        nombre = input("Ingrese un nombre: ")
        if nombre.isalpha():
            nombres.append(nombre)
            break
        else:
            print("Eror, no se puede ingresar numeros o caracteres especiales")

nombre_buscado = input("Ingrese el nombre que esta buscando: ")

if nombre_buscado in nombres:
    for y in range(tam):
        if nombre_buscado == nombres[y]:
            print(f"La posicion del nombre({nombre}) en la lista es {y}, en memoria es {id(nombres[y])}, la longitud de la palabra es {len(nombres[y])}")
else:
    print(f"No se encuentra el nombre {nombre_buscado} en la lista")