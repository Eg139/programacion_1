# 3. Crear un diccionario que contenga los nombres de 10 frutas y su precio en dolares.
# Pedir al usuario que ingrese el nombre de una fruta y luego imprimir en pantalla su
# precio correspondiente en pesos.
frutas = [{"nombre":"Banana","precio":2.5},
          {"nombre":"Sandia","precio":3},
          {"nombre":"Melon","precio":5},
          {"nombre":"Mandaria","precio":1.8},
          {"nombre":"Pitahaya","precio":20.4},
          {"nombre":"Naranja","precio":2},
          {"nombre":"Uva","precio":2.7},
          {"nombre":"Manzana","precio":3.4},
          {"nombre":"Pera","precio":5},
          {"nombre":"Mango","precio":15},
          {"nombre":"Papaya","precio":12},
          ]
aux_fruta = ""  
contador = 0
    
while True: 
    aux_fruta = input("Ingrese un fruta: ")
    if aux_fruta.isalpha():
        break
    else:
        print("Ingreso un elemento invalido")

for fruta in frutas:
    contador+=1
    if fruta["nombre"] == aux_fruta:
        print(f"La fruta {fruta['nombre']} tiene un precio de $ {fruta['precio']*437} pesos")
        break
    elif contador == len(frutas):
        print("El fruta buscado no existe en el diccionario")

    