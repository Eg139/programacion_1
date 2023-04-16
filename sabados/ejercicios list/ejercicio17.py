# Crea dos listas de números y encuentra los elementos que se encuentran en ambas listas.

tam = 3
lista1 = [1,12,3]
lista2 = [3,11,9]
lista_aux = []

# for x in range(tam):
#     while True:
#         try:   
#             numero1 =  int(input(f"Ingrese un numero para la lista 1: "))
#             lista1.append(numero1)
#             break
#         except ValueError:
#             print("Trato de convertir algo diferente a un numero")
        
#     while True:
#         try:   
#             numero2 =  int(input(f"Ingrese un numero para la lista 2: "))
#             lista2.append(numero2)
#             break
#         except ValueError:
#             print("Trato de convertir algo diferente a un numero")


for numero1 in lista1:
    for numero2 in lista2:
        if numero1 == numero2:
            numero_aux = numero1
            lista_aux.append(numero_aux)
    

print(lista1)
print(lista2)
print(lista_aux)
