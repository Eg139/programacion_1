#Dado un número entero n, imprimir la secuencia de números triangulares menores o iguales a n.
#Formula n*(n+1)/2
numero_elegido = 100

# for numero in range(1,numero_elegido+1):
#     acumulador = 0
#     for item in range(1,numero+1):
#         acumulador += item
#     if numero_elegido >= acumulador:
#         print(acumulador)
for numero in range(1,numero_elegido+1):
    formula = (numero *(numero+1)) // 2            
    if numero_elegido >= formula:
        print(formula)
   