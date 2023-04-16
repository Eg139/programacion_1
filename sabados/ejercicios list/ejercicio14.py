# Crea dos listas de 10 números enteros cada una y realiza una multiplicación de los elementos con el mismo índice en ambas listas.
tam = 6
lista1 = [1,2,53,23,12,3]
lista2 = [3,46,3,12,11,9]
lista_aux = []

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
    lista_aux.append(lista1[x] * lista2[x])

print(lista1)
print(lista2)
print(lista_aux)
