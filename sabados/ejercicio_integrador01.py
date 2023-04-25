# Gimnasio - Listas paralelas
# Un gimnasio desea llevar el control de sus miembros. Cada miembro tiene un número de identificación, nombre, edad y tipo de membresía
# (por ejemplo, mensual o anual). La información se encuentra almacenada en cuatro listas paralelas: una lista con los números de identificación, 
# otra lista con los nombres, una lista con las edades y una lista con los tipos de membresía.

# Escriba un programa que permita a los usuarios realizar las siguientes operaciones:

# Agregar un nuevo miembro: el programa debe pedir al usuario que ingrese el número de identificación, nombre, edad y tipo de membresía del nuevo miembro. 
# La información debe ser agregada a las listas paralelas.

# Mostrar toda la información de todos los miembros (número de identificación, nombre, edad y tipo de membresía).

# Actualizar el tipo de membresía de un miembro: el programa debe pedir al usuario que ingrese el número de identificación del miembro y el nuevo tipo de membresía.
#  El programa debe buscar el número de identificación en la lista de números de identificación y actualizar el tipo de membresía correspondiente 
# en la lista de tipos de membresía. En caso de no encontrar al miembro informar con un mensaje de que el mismo no se encontró

# Buscar información de un miembro: el programa debe pedir al usuario que ingrese el número de identificación del miembro. 
# El programa debe buscar el número de identificación en la lista de números de identificación y mostrar el nombre, edad y tipo de membresía
#  correspondientes en las listas de nombres, edades y tipos de membresía.


# Calcular el promedio de edad de los miembros: el programa debe recorrer la lista de edades y calcular el promedio de edad de los miembros.

# Buscar el miembro más joven y el más viejo: el programa debe buscar la edad máxima y mínima en la lista de edades y mostrar el nombre y número de identificación
#  correspondientes en las listas de nombres y números de identificación.

# El programa debe permitir al usuario realizar estas operaciones tantas veces como desee, hasta que decida salir del programa.
#  El programa debe mostrar un menú de opciones para que el usuario pueda elegir la operación que desea realizar.
import os
identificaciones = [1,12,5,4]
nombres = ["Pepe","Moni","Dardo","Paola"]
edades = [50,49,30,19]
membresias = ["mensual","mensual","anual","anual"]

while True:
    tam = len(membresias)
    os.system('cls')
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1. Agregar un nuevo miembro")
    print("2. Mostrar la informacion de todos los miembros")
    print("3. Actualizar el tipo de membresía de un miembro")
    print("4. Buscar información de un miembro")
    print("5. Calcular el promedio de edad de los miembros")
    print("6. Buscar el miembro más joven y el más viejo")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")


    # Opción 1: Agregar un nuevo miembro
    if opcion == "1":

        while True:
            try:
                identificacion = int(input("Ingrese el numero de identificacion: "))
                if identificacion > 0 and not identificacion in identificaciones:
                    identificaciones.append(identificacion)
                    break
            except ValueError:
                print("Trataste de convertir algo diferente a un numero")

        while True: 
                nombre =  input("Ingrese el nombre: ")
                if nombre.isalpha():
                    nombres.append(nombre)
                    break
                else:
                    print("Ingreso un elemento invalido")
        while True:
            try:
                edad = int(input("Ingrese la edad:  "))
                if edad > 0:
                    edades.append(edad)
                    break
                else:
                    "La edad debe ser mayor a 0"
            except ValueError:
                print("Trataste de convertir algo diferente a un numero")

        while True: 
                membresia =  input("Ingrese el tipo de membresia(mensual o anual): ")
                if membresia.isalpha():
                    if membresia == "mensual" or membresia == "anual":
                        membresias.append(membresia)
                        break
                    else:
                        print("Tipo de membresia no valido")
                else:
                    print("Ingreso un elemento invalido")                      

       
    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        print("Nro ID.\tNombre\tEdad\tTipo membresia")
        for x in range(len(identificaciones)):
            print(f"{identificaciones[x]} \t{nombres[x]} \t{edades[x]} \t{membresias[x]}")
       
    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        flag = False
        while True:
            try:
                print("Nro ID.\tTipo membresia")
                for x in range(len(identificaciones)):
                    print(f"{identificaciones[x]}  \t{membresias[x]}")

                aux_id = int(input("Ingrese el numero de identificacion para cambiar la membresia:  "))
                if aux_id in identificaciones:
                    flag = True
                    break
                else:
                    print("Nro de identificacion no encontrado.\n")

            except ValueError:
                 print("Trataste de convertir algo diferente a un numero.\n")
        if flag:
            for z in range(len(identificaciones)):
                if aux_id == identificaciones[z]:
                    while True: 
                        membresia_aux =  input("Ingrese el tipo de membresia(mensual o anual): ")
                        if membresia_aux.isalpha():
                            if membresia_aux == "mensual" or membresia_aux == "anual":
                                membresias[z] = membresia_aux
                                break
                            else:
                                print("Tipo de membresia no valido.\n")
                        else:
                            print("Ingreso un elemento invalido.\n")   
        
    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        flag = False
        while True:
            try:
                print("Nro ID.\tNombre")
                for x in range(len(identificaciones)):
                    print(f"{identificaciones[x]}  \t{nombres[x]}")

                aux_id = int(input("Ingrese el numero de identificacion para cambiar la membresia:  "))
                if aux_id in identificaciones:
                    flag = True
                    break
                else:
                    print("Nro de identificacion no encontrado.\n")

            except ValueError:
                 print("Trataste de convertir algo diferente a un numero.\n")
        if flag:
            print("Nro ID.\tNombre\tEdad\tTipo membresia")
            for z in range(len(identificaciones)):
                if aux_id == identificaciones[z]:
                    print(f"{identificaciones[z]} \t{nombres[z]} \t{edades[z]} \t{membresias[z]}")


    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        promedio = 0
        acumulador = 0
        for edad in edades:
            acumulador += edad
        promedio = acumulador / tam
        print(f"El promedio de edad de todos los miembros es de: {promedio}")



    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
       
        menor = 0
        mayor = 0
        id_mayor = 0
        id_menor = 0

        for z in range(tam):
            if z == 0 or menor > edades[z]:
                menor = edades[z]
                id_menor = identificaciones[z]

        for x in range(tam):
            if x == 0 or mayor < edades[x]:
                mayor = edades[x]
                id_mayor = identificaciones[x]
        
        for i in range(tam):
            if id_mayor == identificaciones[i]:
                print(f"El miembro mas veterano es: ")
                print(f"{identificaciones[i]} \t{nombres[i]} \t{edades[i]} \t{membresias[i]}")
            
            if id_menor == identificaciones[i]:
                print(f"El miembro mas joven es: ")
                print(f"{identificaciones[i]} \t{nombres[i]} \t{edades[i]} \t{membresias[i]}")

    # Opcion 0: Salir
    elif opcion == "0":
        break


    else:
        print("Opción inválida. Intente de nuevo.")

    os.system('pause')
