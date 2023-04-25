# 2. Crear un diccionario que contenga los nombres de paises y sus capitales (máximo 10
# paises y 10 capitales). Pedirle al usuario que ingrese el nombre del pais e imprimir por
# pantalla el nombre de la capital si existe en el diccionario. De lo contrario informarlo.
paises = []
tam = 10
aux_pais = ""
contador = 0
seguir = 's'
for x in range(tam):
    diccionario_aux = {}
    
    while True: 
            aux_nombre = input("Ingrese el pais: ")
            if aux_nombre.isalpha():
                diccionario_aux["pais"] = aux_nombre
                break
            else:
                 print("Ingreso un elemento invalido")
    
    while True: 
            aux_capital = input("Ingrese la Capital: ")
            if aux_capital.isalpha():
                diccionario_aux["capital"] = aux_capital
                break
            else:
                 print("Ingreso un elemento invalido")
    paises.append(diccionario_aux)

while seguir == 's':
    while True: 
        aux_pais = input("Ingrese el pais que desea buscar: ")
        if aux_pais.isalpha():
            break
        else:
            print("Ingreso un elemento invalido. \n")
    for pais in paises:
        contador+=1
        if pais["pais"] == aux_pais:
            print(f"la capital de {pais['nombre']} es {pais['capital']}.")
            break
        elif contador == len(paises):
            print("El pais buscado no existe en el diccionario. \n")

    while True: 
        seguir = input("\n Desea seguir buscando paises(s/n): ")
        if aux_capital.isalpha() and seguir == 's' or seguir == 'n':
            if seguir == 'n':
                 print("Saliendo del programa. \n")
            break
        else:
            print("Ingreso un elemento invalido")
    