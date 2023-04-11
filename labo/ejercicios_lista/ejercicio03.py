# 3-
# Realizar una carga indefinida de números, añadirlos a una lista e indicar que posición
# de memoria es la que mas ocurrencias tiene dentro de esa lista.

numeros = []
seguir = 's'
while seguir == 's':
    try:
        while True:
            numero = int(input("Ingrese un numero: "))
            break
    except ValueError:
        print("Trataste de convertir algo diferente a un numero")
    numeros.append(numero)
    
    seguir = input("Desea seguir? s/n: ")
    while seguir != 's' and seguir != 'n':
        print("Ingrese una opcion valida.")
        seguir = input("Desea seguir? s/n: ")

print(f"posicion de memoria de la lista {id(numeros)}")
for numero in numeros:
    print(f"posicion de memoria los numeros en la lista {id(numero)}")
