# 4. Crear un diccionario que contenga los nombres de 5 animales y la cantidad de patas
# que tienen. Pedir al usuario que ingrese el nombre del animal e imprimir en pantalla la
# cantidad de patas correspondiente.

animales = []
aux_animal = ""  
contador = 0
flag = False
tam = 3

for x in range(tam):
    diccionario_aux = {}
    
    while True: 
            aux_animal = input("Ingrese el animal: ")
            if aux_animal.isalpha():
                diccionario_aux['nombre'] = aux_animal
                break
            else:
                 print("Ingreso un elemento invalido.\n")
    
    while True:
        try:   
            aux_patas = int(input("Ingrese la cantidad de patas del animal: "))
            if aux_patas >= 0:
                diccionario_aux["patas"] = aux_patas
                break
            else:
                print("Debe ser un numero mayor o igual a 0")
        except ValueError:
            print("Trato de convertir algo diferente a un numero")

    animales.append(diccionario_aux)


print("*****Listado de Animales*****")
print("Nombre\t")
for animal in animales:
     print(f"{animal['nombre']}\t")

while True: 
    aux_animal = input("Ingrese un animal que desee ver: ")
    if aux_animal.isalpha():
        break
    else:
        print("Ingreso un elemento invalido")

for animal in animales:
    contador+=1
    if animal["nombre"] == aux_animal:
        print(f"El animal {animal['nombre']} tiene {animal['patas']}  patas")
        break
    elif contador == len(animales):
        print("El animal buscado no existe en el diccionario")

    