#Dado un número entero n, imprimir la secuencia de números impares menores o iguales a n.
numero = 9
#numero = int(input("Ingrese un numero: "))


for i in range(2, numero+1):
    if i % 2 != 0:
        print(i)