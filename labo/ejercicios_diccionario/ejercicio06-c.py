# 3. Crear un diccionario que contenga los frutas de 10 frutas y su precio en dolares.
# Pedir al usuario que ingrese el fruta de una fruta y luego imprimir en pantalla su
# precio correspondiente en pesos.
frutas = []
tam = 10
aux_fruta = ""  
contador = 0
peso_dolar = 437

for x in range(tam):
    diccionario_aux = {}
    
    while True: 
            aux_fruta = input("Ingrese la fruta: ")
            if aux_fruta.isalpha():
                diccionario_aux["fruta"] = aux_fruta
                break
            else:
                 print("Ingreso un elemento invalido.\n")
    
    while True:
        try:   
            aux_precio = float(input("Ingrese el precio de la fruta: "))
            if aux_precio > 0:
                diccionario_aux["precio"] = aux_precio
                break
            else:
                print("El precio debe ser mayor a 0")
        except ValueError:
            print("Trato de convertir algo diferente a un numero")

    frutas.append(diccionario_aux)

print("*****Listado de frutas*****\n")
print("Nombre\t")
for fruta in frutas:
     print(f"{fruta['fruta']}\t")

while True: 
    aux_fruta = input("Ingrese la fruta que desea ver: ")
    if aux_fruta.isalpha():
        break
    else:
        print("Ingreso un elemento invalido")

for fruta in frutas:
    contador+=1
    if fruta["fruta"] == aux_fruta:
        print(f"La {fruta['fruta']} tiene un precio de $ {fruta['precio']*peso_dolar} pesos")
        break
    elif contador == len(frutas):
        print("La fruta buscado no existe en el diccionario")

    