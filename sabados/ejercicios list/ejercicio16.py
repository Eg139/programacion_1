# Crea dos listas con la misma cantidad de elementos y luego crea una tercera lista que contenga los elementos de ambas listas intercalados. 
#Por ejemplo, si las dos listas son [1, 2, 3] y ["a", "b", "c"], la tercera lista debería ser [1, "a", 2, "b", 3, "c"].

tam = 6
lista1 = [1,2,53,23,12,3]
lista2 = ['a','b','c','z','x','e']
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
            letra =  input(f"Ingrese una letra para la lista 2: ")
            if letra.isalpha():
                lista2.append(letra)
                break
            else:
                 print("Ingreso un elemento invalido")


for x in range(len(lista1)):
    lista_aux.append(lista1[x])
    lista_aux.append(lista2[x])

print(lista1)
print(lista2)
print(lista_aux)
