# Es la gala final de Gran Hermano y la producción nos pide un programa para contar
# los votos de los televidentes y saber cuál será el participante que ganará el juego.
# Los participantes finalistas son: Nacho, Julieta y Marcos.
# El televidente debe ingresar:
# ● Nombre del votante
# ● Edad del votante (debe ser mayor a 13)
# ● Género del votante (masculino, femenino, otro)
# ● El nombre del participante a quien le dará el voto positivo.
# No se sabe cuántos votos entrarán durante la gala.
# Se debe informar al usuario:
# A. El promedio de edad de las votantes de género femenino
# B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a
# Nacho o Julieta.
# C. Nombre del votante más joven que votó a Nacho.
# D. Nombre de cada participante y porcentaje de los votos qué recibió.
# E. El nombre del participante que ganó el reality (El que tiene más votos)
votos = ['Nacho','Marcos','Julieta','Nacho']
edades = [15,25,40,60]
generos = ['masculino','femenino','masculino','femenino']
nombres = ['Pepe', 'Mar', 'Nicolas', 'Fernanda']

def porcentaje(num, total):
    return (num/total)*100
def votar():
    seguir = 's'

    while seguir == 's':
        nombre = input("Ingrese su nombre: ")
        while True:
            try:
                edad = int(input("Debe ser mayor de 13: "))
                if edad > 13:
                    break
                else:
                    print("Edad menor de lo permitida")
            except ValueError:
                print("Trataste de convertir algo diferente a un numero")
        genero = input("Ingrese su genero (masculino, femenino, otro):  ")
        voto = input("Ingrese el nombre del particimante al cual quiere elegir (Nacho, Julieta y Marcos): ")
        #Agregar los datos ingresados a la lista
        nombres.append(nombre)
        edades.append(edad)
        generos.append(genero)
        votos.append(voto)
        seguir = input("Desea seguir votando s/n: ")



while True:
    print("# A. El promedio de edad de las votantes de género femenino")
    print("# B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta.")
    print("# C. Nombre del votante más joven que votó a Nacho.")
    print("# D. Nombre de cada participante y porcentaje de los votos qué recibió.")
    print("# E. El nombre del participante que ganó el reality (El que tiene más votos)")
    print("# V. Votar")
    print("#S salir")
    opcion = input("Ingrese una opcion:  ")
    if opcion == 'A':
        i = 0
        contador = 0
        acumulador = 0
        while i < len(generos):
            if generos[i] == 'femenino':
                acumulador += edades[i]
                contador += 1
            i += 1
        promedio = acumulador / contador
        print(f"El promedio de edades de las votantes femeninos es de : {promedio}")

    elif opcion == 'B':
        i = 0
        contador = 0
        acumulador = 0        
        while i < len(generos):
            if generos[i] == 'masculino' and votos[i] == 'Nacho' or votos[i] == 'Julieta':
                if edades[i] >= 25 and edades[i] <= 40: 
                    contador += 1
            i += 1
        print(f"La cantidad de votantes fue: {contador}")
    elif opcion == 'C':
        i = 0
        menor = 0
        nombre_joven = ''
        while i < len(edades):
            if i == 0 or edades[i] < menor :
                menor = edades[i]
                nombre_joven = nombres[i]
            i += 1
        print(f"El Nombre del votante mas joven de nacho es {nombre_joven}")
    elif opcion == 'D':
        i= 0
        voto_j = 0
        voto_m = 0
        voto_n = 0
        contador = 0
        contador = 1
        while i < len(votos):
            if votos[i] == 'Nacho':
                voto_n += 1
            elif votos[i] == 'Marcos':
                voto_m += 1
            else:
                voto_j += 1
            i += 1
            contador +=1
        print(f"Los participantes son Julieta, Marcos y Nacho, el porcentaje de los votos es: {porcentaje(voto_j,contador)}%, {porcentaje(voto_m,contador)}% y {porcentaje(voto_n,contador)}%")
    elif opcion == 'E':
        i= 0
        voto_j = 0
        voto_m = 0
        voto_n = 0
        nombre_ganador = ''
        while i < len(votos):
            if votos[i] == 'Nacho':
                voto_n += 1
            elif votos[i] == 'Marcos':
                voto_m += 1
            else:
                voto_j += 1
            i += 1
        if voto_n > voto_m and voto_n > voto_j:
            nombre_ganador = "Nacho"
        elif voto_m > voto_n and voto_m > voto_j:
            nombre_ganador = "Marcos"
        elif voto_j > voto_n and voto_j > voto_m:
            nombre_ganador = "Julieta"

        print(f"El ganador del concurso es {nombre_ganador}")
        break
    elif opcion == 'V':
        votar()
    elif opcion == 'S':
        print("Saliendo del programa")
        break

