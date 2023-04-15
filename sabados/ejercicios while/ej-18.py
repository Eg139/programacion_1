# Dado un número entero n, imprimir la suma de todos los números que son múltiplos de 5 menores o iguales a n.
numero = 25
i= 0
acumulador = 0
while i <= numero:
    if i % 5 == 0:
        acumulador += i
    i += 1
print(acumulador)