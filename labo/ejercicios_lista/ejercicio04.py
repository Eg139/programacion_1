# 4-
# Debemos desarrollar un algoritmo que permita computar los votos del Senado de
# Berlinberlín. Se deberá ingresar el nombre de cada senador y si está Presente o no en
# la sesión. Si el senador está presente, se deberá pedir el valor del voto
# El voto de los senadores berliberlineses puede ser Afirmativo, Negativo o Abstención
# (validar). El valor por defecto para los senadores ausentes será Abstención.
# Se deberá Informar:

nombres = ['Roberto','Marco','Lucia','Carla','Fernando']
votos = ['Afirmativo','Negativo','Negativo','Abstencion','Abstencion']
asistencias = ['Presente','Presente','Presente','Ausente','Presente']

def alta_senador():
    while True:
        nombre = input("Ingrese el nombre: ")
        if nombre.isalpha():
            break
        else:
            print("Eror, no se puede ingresar numeros o caracteres especiales")

    while True:
        asistencia = input("Ingrese la asistencia del senador(Presente o Ausente): ")
        if asistencia.isalpha():
            if(asistencia == 'Presente' or asistencia == 'Ausente'):
                break
            else:
                print("Opcion invalida")
        else:
            print("Eror, no se puede ingresar numeros o caracteres especiales")    
    
    if asistencia == 'Ausente':
        voto = 'Abstencion'
    else:
        while True:
            voto = input("Su voto va a ser(Afirmativo, Negativo o Abstencion)?: ")
            if voto.isalpha:
                if voto == 'Afirmativo' or voto == 'Negativo' or voto == 'Abstencion':
                    break
                else:
                    print("Opcion invalida.")
            else:
                print("Eror, no se puede ingresar numeros o caracteres especiales")
    nombres.append(nombre)
    asistencias.append(asistencia)
    votos.append(voto)

while True:
    
    tam = len(votos)
    print("# A. Cantidad total de senadores.")
    print("# B. Cantidad de senadores presentes.")
    print("# C. Cantidad y porcentaje de votos afirmativos.")
    print("# D. Cantidad y porcentaje de votos negativos.")
    print("# E. Cantidad y porcentaje de abstenciones.")
    print("# F. Generar una lista de senadores por cada tipo de voto y mostrarlas por pantalla.")
    print("# G Ingresar senadores")
    print("# S. salir")
    opcion = input("Ingrese una opcion:  ")
    if opcion == 'A':
        contador = 0
        for i in range(0, tam):
            contador += 1
        print(f"La cantidad de senadores es de {contador}")
    elif opcion == 'B':
        contador = 0
        for asistencia in asistencias:
            if asistencia == 'Presente':
                contador += 1
        print(f"La cantidad de senadores presentes es de {contador}")
    elif opcion == 'C':
        contador = 0
        for voto in votos:
            if voto == 'Afirmativo':
                contador += 1
        porcentaje = (contador / tam)*100
        print(f"La cantidad de votos afirmativos es de {contador} con un porcentaje de {porcentaje} %")
    elif opcion == 'D':
        contador = 0
        for voto in votos:
            if voto == 'Negativo':
                contador += 1
        porcentaje = (contador / tam)*100
        print(f"La cantidad de votos negativos es de {contador} con un porcentaje de {porcentaje} %")
    elif opcion == 'E':
        contador = 0
        for voto in votos:
            if voto == 'Abstencion':
                contador += 1
        porcentaje = (contador / tam)*100
        print(f"La cantidad de votos abstenciones es de {contador} con un porcentaje de {porcentaje} %")        
    elif opcion == 'F':
        positivos = []
        negativos = []
        abstenciones = []
        for i in range(0, tam):
            aux = []
            if votos[i] == 'Afirmativo':
                aux.append(nombres[i])
                aux.append(asistencias[i])
                aux.append(votos[i])
                positivos.append(aux)
            elif votos[i] == 'Negativo':
                aux.append(nombres[i])
                aux.append(asistencias[i])
                aux.append(votos[i])
                negativos.append(aux)
            else:
                aux.append(nombres[i])
                aux.append(asistencias[i])
                aux.append(votos[i])
                abstenciones.append(aux)

        print(f"Lista de afirmativos {positivos}")
        print(f"Lista de negativos {negativos}")
        print(f"Lista de abstenciones {abstenciones}")    
    elif opcion == 'G':
        alta_senador()
    elif opcion == 'S':
        print("Saliendo del programa")
        
        break

