# 6-
# Se nos pide realizar un programa que le pida al usuario una N cantidad de veces y
# calcular la máxima diferencia en la secuencia de números ingresada.
numeros = []
tam = 5
max_dif = 0


for i in range(tam):
    while True:
        try:
            numero = int(input("Ingrese una opcion:  "))
            numeros.append(numero)
            break
        except ValueError:
            print("Trataste de convertir algo diferente a un numero")

for x in range(len(numeros)-1):
    aux = 0
    if numeros[x] < 0 or numeros[x+1] < 0:
        aux = numeros[x] + numeros[x+1]
        if aux < 0:
            aux = aux * (-1)
    elif numeros[x] >= 0 and numeros[x+1] >= 0:
        aux = numeros[x] - numeros[x+1]
        if aux < 0:
            aux = aux * (-1)

    if x == 0 or max_dif < aux:
        max_dif = aux

print(f"La maxima diferencia entre los numeros es {max_dif}")