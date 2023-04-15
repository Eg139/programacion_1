# Dado un número entero n, imprimir todos los números primos menores o iguales a n.
numero_entero = 7
for numero in range(0, numero_entero+1):
    primo = True
    i = 2
    if numero > 0:
        while i < numero:
            if numero % i == 0:
                primo = False
                break
            i += 1
        if primo == True:
            print(numero)