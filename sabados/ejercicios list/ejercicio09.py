# Crea una lista de números enteros y pide al usuario que ingrese otro número entero. 
# Luego, busca el número ingresado en la lista y muestra la posición en la que se encuentra. 
# Si el número no se encuentra en la lista, muestra un mensaje indicando que no se encontró



numero_aux = 0
numeros = [100,4,8]
indices = []
tam = len(numeros)

while True:
    try:
        numero_aux = int(input("Ingrese un nuevo numero: "))
        break
    except ValueError:
        print("Trataste de convertir algo diferente a un numero")

for x in range(tam):
     if numeros[x] == numero_aux:
          indices.append(x)

if len(indices) > 0:
     for indice in indices:
          print(f"el numero se encuentra en el indice {indice}")
else:
     print("El numero no se encuentra en la lista")