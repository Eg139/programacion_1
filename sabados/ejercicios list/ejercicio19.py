# Crea una lista vacía y pide al usuario que ingrese una palabra. Luego, agrega la palabra a la lista si no se encuentra ya en la lista.
# Repite este proceso hasta que la lista tenga al menos 5 palabras.
palabras = []
tam = 5

for x in range(tam):        
    while True: 
            palabra =  input(f"Ingrese una palabra para la lista: ")
            if palabra.isalpha():
                if not palabra in palabras:
                    palabras.append(palabra)
                    break
                else:
                     print("La palabra ya se encuentra en la lista")
            else:
                 print("Ingreso un elemento invalido")


print(palabras)

