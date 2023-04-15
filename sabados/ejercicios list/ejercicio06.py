# Crea una lista con 3 números enteros y luego agrega un nuevo número al final de la lista.
tam = 3

numeros = [100,4,8]

while True:
    try:
            numero_aux = int(input("Ingrese un nuevo numero: "))
            numeros.append(numero_aux)
            break
    except ValueError:
        print("Trataste de convertir algo diferente a un numero")
