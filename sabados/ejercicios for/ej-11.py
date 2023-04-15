#Dado un número entero n, imprimir la secuencia de números primos menores o iguales a n.
numero_entero = 7

for numero in range(0, numero_entero+1):
    primo = True
    if numero > 0:
        for i in range(2,numero):
            if numero % i == 0:
                primo = False
                break
        if primo == True:
            print(numero)
