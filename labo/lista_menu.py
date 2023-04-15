# Ejercicio con Menú de Opciones
# Realizar un programa utilizando los conceptos de la clase del lunes:
# Para utilizar las opciones 2 a la 10 hay que cargar los números en la opción 1
# Si se vacía la lista con la opción 10 se deben bloquear nuevamente las opciones hasta que se
# cargue de nuevo los números con la opción 1
import os
tam = 10
# numeros = [4,48,-8,45,0,4,7,10,100,7]
numeros = []
flag_numeros = False
while True:
    os.system('cls')
    print("# 1 cargar una lista con 10 números")
    print("# 2 mostrar el total de los números ingresados")
    print("# 3 mostrar el promedio")
    print("# 4 mayor")
    print("# 5 menor")
    print("# 6 pedir un número y decir si está en la lista")
    print("# 7 pedir un número e informar todos los índices donde aparece")
    print("# 8 informar cuantos números pares y cuantos impares hay en la lista")
    print("# 9 informar cuantos positivos, cuantos negativos y cuantos ceros hay en la lista")
    print("# 10 vaciar lista")
    print("# 11 salir")
    while True:
        
        try:
            opcion = int(input("Ingrese una opcion:  "))
            if opcion >= 1 and opcion <= 11:
                break
            else:
                print("Opcion invalida")
        except ValueError:
            print("Trataste de convertir algo diferente a un numero")
            
    if opcion == 1:
        for x in range(tam):
            try:
                numero = int(input("Ingrese un numero:  "))
                numeros.append(numero)
                flag_numeros = True
            except ValueError:
                print("Trataste de convertir algo diferente a un numero")
    elif opcion == 2:
        if flag_numeros:
            contador = 0
            for numero in numeros:
                contador +=1
            print(f"Los numeros ingresados son {contador}")
        else:
            print("Antes debe ingresar numeros")

    elif opcion == 3:
        if flag_numeros:
            acumulador = 0
            contador = 0
            for numero in numeros:
                contador += 1
                acumulador += numero
            promedio = acumulador / contador
            print(f"El promedio es {promedio}")
        else:
            print("Antes debe ingresar numeros")

    elif opcion == 4:
        if flag_numeros:
            mayor = 0
            flag = False
            for numero in numeros:
                if flag == False or numero > mayor:
                    mayor = numero
                    flag = True
            print(f"El numero mayor es {mayor}")
        else:
            print("Antes debe ingresar numeros")

    elif opcion == 5:
        if flag_numeros:
            menor = 0
            flag = False
            for numero in numeros:
                if flag == False or numero < menor:
                    menor = numero
                    flag = True
            print(f"El numero menor es {menor}")
        else:
            print("Antes debe ingresar numeros")
    elif opcion == 6:
        if flag_numeros:
            while True:
                try:
                    numero_pedido = int(input("Ingrese el numero que desea buscar:  "))
                    if numero_pedido in numeros:
                        print("El numero se encuentra en la lista")
                        break
                    else:
                        print("El numero no se encuentra en la lista")
                except ValueError:
                    print("Trataste de convertir algo diferente a un numero")
        else:
            print("Antes debe ingresar numeros")                
    elif opcion == 7:
        if flag_numeros:
            while True:
                posiciones = []
                try:
                    numero_pedido = int(input("Ingrese el numero que desea buscar:  "))
                    for i in range(tam):
                        if numero_pedido == numeros[i]:
                            posiciones.append(i)
                    if len(posiciones) > 0:
                        print(f"El numero solicitado se encuentra en la/s poscion/es {posiciones}")
                    else:
                        print("El numero no se encuentra en la lista")
                    break
                except ValueError:
                    print("Trataste de convertir algo diferente a un numero")
        else:
            print("Antes debe ingresar numeros")

    elif opcion == 8:
        if flag_numeros:
            contador_pares = 0
            contador_impares = 0
            for numero in numeros:
                if numero % 2 == 0:
                    contador_pares += 1
                elif numero % 2 != 0:
                    contador_impares += 1
            print(f"Los numeros pares son {contador_pares} y los impares son {contador_impares}")
        else:
            print("Antes debe ingresar numeros")
    elif opcion == 9:
        if flag_numeros:
            contador_positivos = 0
            contador_Negativos = 0
            contador_ceros = 0
            for numero in numeros:
                if numero > 0:
                    contador_positivos += 1
                elif numero < 0:
                    contador_Negativos += 1
                else:
                    contador_ceros += 1
            print(f"Los numeros positivos son {contador_positivos}, los negativos son {contador_Negativos} y los ceros son {contador_ceros}")
        else:
            print("Antes debe ingresar numeros")

    elif opcion == 10:
        if flag_numeros:
            numeros.clear()
        else:
            print("Antes debe ingresar numeros")
    elif opcion == 11:
        print("Saliendo del programa")
        break
    os.system('pause')
