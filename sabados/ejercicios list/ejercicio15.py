# Crea una lista de números enteros y luego encuentra la suma de los números en índices impares.

tam = 6
lista1 = [1,2,53,23,12,3]
acumulador = 0
for x in range(tam):
    while True:
        try:   
            numero1 =  int(input(f"Ingrese un numero para la lista 1: "))
            lista1.append(numero1)
            break
        except ValueError:
            print("Trato de convertir algo diferente a un numero")
        
    while True:
        try:   
            numero2 =  int(input(f"Ingrese un numero para la lista 2: "))
            lista2.append(numero2)
            break
        except ValueError:
            print("Trato de convertir algo diferente a un numero")


for x in range(tam):
    if x % 2 == 0:
        acumulador += lista1[x]

print(acumulador)

