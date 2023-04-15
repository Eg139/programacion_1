# 7-
# Un grupo de cinco amigos se juntan para jugar una partida de CS:GO, deciden que
# van a jugar 10 partidas y necesitan realizar datos estadísticos sobre las partidas
# jugadas. Para eso necesitan ingresar los siguientes datos en el siguiente orden
# especifico: nombre, edad, bajas confirmadas (el murió), muertes confirmadas (el mate
# a otro jugador). Con esos datos se necesita saber:

# Nota: los datos tienen que ingresar en 1 solo string separado por espacios, y ser
# almacenados en una lista, investigar que función les permite lograrlo y como hacer una
# lista de listas.
import os

tam = 10
jugadores = [
    ['pepe', 50, 30, 20], ['moni', 49, 50, 10], ['coki', 18, 15, 40], 
    ['paola', 19, 25, 34], ['dardo', 35, 18, 40], ['mari', 23, 60, 39],
    ['santi', 25, 12, 12], ['jack', 19, 30, 20], ['Papatito', 34, 15, 25],
    ['nala', 22, 10, 24]
    ]

opciones = ["1","2","3","4","5","6","7","8"]

while True:
    aux = ""
    os.system('cls')
    print("          ********************    MENU DE OPCIONES    **************************         ")
    print("# 1• Nombre del jugador más joven.")
    print("# 2• Jugador que más bajas tuvo.")
    print("# 3• Jugador con menos muertes")
    print("# 4• El promedio de bajas del equipo")
    print("# 5• La cantidad de jugadores que tienen entre 20 y 30 años cuyas bajas estan entre 10 y 20")
    print("# 6• El nombre y edad del jugador que más muertes tuvo (MVP)")
    print("# 7• Ingresar Jugador")
    print("# 8• salir")
    while True:
        opcion = input("Ingrese una opcion:  ")
        if opcion in opciones:
            break
        else:
            print("Opcion invalida")
            
    if opcion == "1":
        min_edad = 0
        nombre = ""
        flag = False
        for jugador in jugadores:
            if flag == False or int(jugador[1]) < min_edad:
                nombre = jugador[0]
                min_edad = int(jugador[1])
                flag = True
        print(f"El jugador mas joven se llama {nombre}")

    elif opcion == "2":
        max_bajas = 0
        nombre = ""
        flag = False
        for jugador in jugadores:
            if flag == False or int(jugador[2]) > max_bajas:
                nombre = jugador[0]
                max_bajas = int(jugador[2])
                flag = True
        print(f"El jugador con mas bajas es {nombre}")
    elif opcion == "3":
        min_muertes = 0
        nombre = ""
        flag = False
        for jugador in jugadores:
            if flag == False or int(jugador[3]) < min_muertes:
                nombre = jugador[0]
                min_muertes = int(jugador[3])
                flag = True
        print(f"El jugador con menos muertes es {nombre}")
    elif opcion == "4":
        acumulador = 0
        promedio = 0
        for jugador in jugadores:
            acumulador += int(jugador[2])
        promedio = acumulador / len(jugadores)
        print(f"El promedio de bajas del equipo es {promedio}")
    elif opcion == "5":
        contador = 0
        flag = False
        for jugador in jugadores:
            if (int(jugador[1]) >= 20 and int(jugador[1]) <= 30) and (int(jugador[2]) >= 10 and int(jugador[2]) <= 20):
                contador += 1


        print(f"La cantidad de jugadores que tienen entre 20 y 30 años cuyas bajas estan entre 10 y 20 es: {contador}")
    elif opcion == "6":
        max = 0
        nombre = ""
        flag = False
        for jugador in jugadores:
            if flag == False or int(jugador[3]) > max:
                nombre = jugador[0]
                max = int(jugador[3])
                flag = True
        print(f"MVP {nombre} con {max} muertes confirmadas")

    elif opcion == "7":
        for x in range(tam): 
            aux_edad = 0
            aux_bajas = 0
            aux_muertes = 0
            aux = input("Ingrese el nombre: ")
            while True:
                try:
                    aux_edad = input("Ingrese la edad:  ")
                    if int(aux_edad):
                        aux += " " + aux_edad
                    break
                except ValueError:
                    print("Trataste de convertir algo diferente a un numero")

            while True:
                try:
                    aux_bajas = input("Ingrese las bajas confirmadas: ")
                    if int(aux_bajas):
                        aux += " " + aux_bajas
                    break
                except ValueError:
                    print("Trataste de convertir algo diferente a un numero")

            while True:
                try:
                    aux_muertes = input("Ingrese las muertes confirmadas: ")
                    if int(aux_muertes):
                        aux += " " + aux_muertes
                    break
                except ValueError:
                    print("Trataste de convertir algo diferente a un numero")                           
            jugadores.append(aux.split())
            jugadores[x][1] = int(jugadores[x][1])
            jugadores[x][2] = int(jugadores[x][2])
            jugadores[x][3] = int(jugadores[x][3])

    elif opcion == "8":
        print("Saliendo del programa")
        
        break

    os.system('pause')