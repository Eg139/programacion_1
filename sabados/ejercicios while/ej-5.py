# Dado un número entero n, imprimir si el número es primo o no.
numero = 19
i= 2
es_primo = True
while i < numero:
    if numero % i == 0:
        es_primo = False
        break
    i += 1
    
if es_primo:
    print("Es primo")