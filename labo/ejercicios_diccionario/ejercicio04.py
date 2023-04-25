# 4. Crear un diccionario que contenga los nombres de 5 animales y la cantidad de patas
# que tienen. Pedir al usuario que ingrese el nombre del animal e imprimir en pantalla la
# cantidad de patas correspondiente.

animales = [{"nombre":"leon","patas":4},
          {"nombre":"tigre","patas":4},
          {"nombre":"pato","patas":2},
          {"nombre":"mono","patas":4},
          {"nombre":"cangrejo","patas":8}
          ]
aux_animal = ""  
contador = 0
flag = False
    
while True: 
    aux_animal = input("Ingrese un animal: ")
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

    