# 5-
# Para una veterinaria se pide clasificar el ingreso de pacientes hasta que el usuario
# quiera (se limita a 1 perrito por ingreso), se les pide:
# nombre, precio de la consulta (validar entre 500$ y 2500$) raza: (validar entre caniche,
# ovejero, siberiano), edad (validar 1 a 15) y peso (entre 25 y 40 kilos) determinar:
import os

nombres = ['Pepe','Abi','Dona','Charlie','Rubio','Michifus']
valor_consulta = [500,1000,2500,900,1500,500]
razas = ['caniche','siberiano','ovejero','ovejero','siberiano','siberiano']
edades = [15,1,5,10,9,4]
kilaje = [25,40,35,30,38,27]

while True:
    os.system('cls')
    tam = len(nombres)
    print("# 1. Generar un listado con todos los datos de los pacientes ordenados por edad.")
    print("# 2. Generar un listado de los perros que pesen más de 30 kilos y ordenarla por nombre.")
    print("# 3. Si la facturación en bruto supera los 5000$, hay que agregarle un 21% de impuesto por ingresos brutos e informarlo.")
    print("# 4. Informar el nombre y el peso del perro con más peso.")
    print("# 5 Ingresar paciente")
    print("# 6. salir")
    while True:
        try:
            opcion = int(input("Ingrese una opcion:  "))
            if opcion >= 1 and opcion <= 6:
                break
            else:
                print("Opcion invalida")
        except ValueError:
            print("Trataste de convertir algo diferente a un numero")
            
    if opcion == 1:
        for i in range(0, tam-1):
                for k in range(0,tam -1):
                    if edades[k] > edades[k+1]:
                        aux_edad= edades[k]
                        edades[k] = edades[k+1]
                        edades[k+1] = aux_edad

                        aux_nombre= nombres[k]
                        nombres[k] = nombres[k+1]
                        nombres[k+1] = aux_nombre

                        aux_precio= valor_consulta[k]
                        valor_consulta[k] = valor_consulta[k+1]
                        valor_consulta[k+1] = aux_precio

                        aux_raza= razas[k]
                        razas[k] = razas[k+1]
                        razas[k+1] = aux_raza


                        aux_kilaje= kilaje[k]
                        kilaje[k] = kilaje[k+1]
                        kilaje[k+1] = aux_kilaje

        for x in range(tam):
            print(f"{nombres[x]} --- {valor_consulta[x]} --- {razas[x]} --- {edades[x]} --- {kilaje[x]}")

    elif opcion == 2:
        aux_nombre = []
        aux_edad = []
        aux_kilaje = []
        aux_raza = []
        aux_precio = []
        for x in range(tam):
            if kilaje[x] >= 30:
                aux_nombre.append(nombres[x])
                aux_edad.append(edades[x])
                aux_kilaje.append(kilaje[x])
                aux_raza.append(razas[x])
                aux_precio.append(valor_consulta[x])

        for i in range(0, tam-1):
            for k in range(len(aux_nombre) -1):
                if aux_nombre[k] > aux_nombre[k+1]:
                    
                    aux_e= aux_edad[k]
                    aux_edad[k] = aux_edad[k+1]
                    aux_edad[k+1] = aux_e

                    aux_n= aux_nombre[k]
                    aux_nombre[k] = aux_nombre[k+1]
                    aux_nombre[k+1] = aux_n

                    aux_p= aux_precio[k]
                    aux_precio[k] = aux_precio[k+1]
                    aux_precio[k+1] = aux_p

                    aux_r= aux_raza[k]
                    aux_raza[k] = aux_raza[k+1]
                    aux_raza[k+1] = aux_r


                    aux_k= aux_kilaje[k]
                    aux_kilaje[k] = aux_kilaje[k+1]
                    aux_kilaje[k+1] = aux_k

        for z in range(len(aux_nombre)):
            print(f"{aux_nombre[z]} --- {aux_precio[z]} --- {aux_raza[z]} --- {aux_edad[z]} --- {aux_kilaje[z]}")

    elif opcion == 3:
        acumulador = 0
        impuesto = 0
        for precio in valor_consulta:
            acumulador += precio
        if acumulador > 5000:
            impuesto = acumulador * 0.21
            print(f"Supero la facturacion de 5000$, debera abonar el impuesto a ingresos brutos del 21% equivalente a {impuesto}$")

    elif opcion == 4:
        max_peso = 0
        posicion = 0
        for x in range(0,tam):
            if x == 0 or max_peso < kilaje[x]:
                max_peso = kilaje[x]
                posicion = x
        print(f"El nombre del paciente mas pesado es {nombres[posicion]} y su peso es de {max_peso}")
    elif opcion == 5:
        while True:
            nombre = input("Ingrese el nombre del paciente: ")
            if nombre.isalpha():
                break
            else:
                print("Eror, no se puede ingresar numeros o caracteres especiales")

        while True:
            try:
                precio_consulta = float(input("Ingrese el precio de la consulta(500$ a 2500$): "))
                if precio_consulta >= 500 and precio_consulta <= 2500:
                    break
                else:
                    print("Precio invalido")
            except ValueError:
                print("Trataste de convertir algo diferente a un numero")

        while True:
            raza = input("Ingrese la raza del paciente(caniche, ovejero o siberiano): ")
            if raza.isalpha():
                if raza == 'caniche' or raza == 'ovejero' or raza == 'siberiano':
                    break
                else:
                    print("Raza incorrecta")
            else:
                print("Eror, no se puede ingresar numeros o caracteres especiales")

        while True:
            try:
                edad = int(input("Ingrese la edad del paciente(1 a 15): "))
                if edad >= 1 and edad <= 15:
                    break
                else:
                    print("Edad invalida")           
            except ValueError:
                print("Trataste de convertir algo diferente a un numero")

        while True:
            try:
                peso = float(input("Ingrese el peso del paciente(25 a 40): "))
                if peso >= 25 and peso <= 40:
                    break
                else:
                    print("Peso invalido")           
            except ValueError:
                print("Trataste de convertir algo diferente a un numero")


        nombres.append(nombre)
        valor_consulta.append(precio_consulta)
        razas.append(raza)
        edades.append(edad)
        kilaje.append(peso)


    elif opcion == 6:
        print("Saliendo del programa")
        
        break

    os.system('pause')