# 2. Crear un diccionario que contenga los nombres de paises y sus capitales (máximo 10
# paises y 10 capitales). Pedirle al usuario que ingrese el nombre del pais e imprimir por
# pantalla el nombre de la capital si existe en el diccionario. De lo contrario informarlo.
paises = [{"nombre":"Francia","capital":"Paris"},
          {"nombre":"Peru","capital":"Lima"},
          {"nombre":"Colombia","capital":"Bogota"},
          {"nombre":"Chile","capital":"Chile"},
          {"nombre":"China","capital":"Pekin"},
          {"nombre":"Brasil","capital":"Brasilia"},
          {"nombre":"Uruguay","capital":"Montevideo"},
          {"nombre":"Paraguay","capital":"Asuncion"},
          {"nombre":"Ecuador","capital":"Quito"},
          {"nombre":"USA","capital":"Washington"},
          {"nombre":"España","capital":"Madrid"},
          ]
aux_pais = ""
contador = 0
while True: 
    aux_pais = input("Ingrese un pais: ")
    if aux_pais.isalpha():
        break
    else:
        print("Ingreso un elemento invalido")
for pais in paises:
    contador+=1
    if pais["nombre"] == aux_pais:
        print(f"{pais['capital']}")
        break
    elif contador == len(paises):
        print("El pais buscado no existe en el diccionario")
    