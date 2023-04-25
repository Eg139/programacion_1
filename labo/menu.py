import os

while True:
    os.system('cls')
    print("          ********************    MENU DE OPCIONES    **************************         ")
    print("# 1. Generar un listado con todos los datos de los pacientes ordenados por edad.")
    print("# 2. Generar un listado de los perros que pesen más de 30 kilos y ordenarla por nombre.")
    print("# 3. Si la facturación en bruto supera los 5000$, hay que agregarle un 21% de impuesto por ingresos brutos e informarlo.")
    print("# 4. Informar el nombre y el peso del perro con más peso.")
    print("# 5 Ingresar paciente")
    print("# 6. salir")
    
    opcion = input("Ingrese una opcion:  ")

            
    if opcion == "1":
        print("Opcion 1")
    elif opcion == "2":
        print("Opcion 2")
    elif opcion == "3":
        print("Opcion 3")
    elif opcion == "4":
        print("Opcion 4")
    elif opcion == "5":
        print("Opcion 5")
    elif opcion == "6":
        print("Saliendo del programa")
        
        break
    else:
        print("Opcion invalida.")

    os.system('pause')