#Dado un número entero n, imprimir la secuencia de números de Harshad menores o iguales a n.

numero_elegido = 30

    
for numero in range(1, numero_elegido+1):
    acumulador = 0
    numero_cadena = str(numero)

    for i in numero_cadena:
        acumulador += int(i)
    if numero % acumulador == 0:
        print(numero)
