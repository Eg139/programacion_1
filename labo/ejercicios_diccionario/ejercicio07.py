# Desde ahora en más, los diccionarios deberian empezar vacíos.
# 7. Crear un diccionario que contenga los nombres, edades, alturas (en metros), pesos (en
# kilogramos) y ciudades de un numero indeterminados de personas. Luego calcular el
# indice de masa corporal (IMC) de cada persona y agregarlo al diccionario. Finalmente,
# imprimir en pantalla los nombres de las personas junto con su ciudad y si IMC
# (redondeando a 2 decimales).

personas = []
for x in range(5):
    diccionario_aux = {}
    
    while True: 
            aux_nombre = input("Ingrese un nombre: ")
            if aux_nombre.isalpha():
                diccionario_aux["nombre"] = aux_nombre
                break
            else:
                 print("Ingreso un elemento invalido")
    
    while True:
        try:   
            aux_edad = int(input("Ingrese su edad: "))
            if aux_edad > 0:
                diccionario_aux["edad"] = aux_edad
                break
            else:
                print("La edad mo puede ser 0 ni negativa")
        except ValueError:
            print("Trato de convertir algo diferente a un numero")   

    while True:
        try:   
            aux_altura = float(input("Ingrese su altura en metros: "))
            if aux_altura > 0:
                diccionario_aux["altura"] = aux_altura
                break
            else:
                print("La altura debe ser positiva")
        except ValueError:
            print("Trato de convertir algo diferente a un numero")

    while True:
        try:   
            aux_peso = int(input("Ingrese su peso: "))
            if aux_peso > 0:
                diccionario_aux["edad"] = aux_peso
                break
            else:
                print("El peso debe ser mayor a 0")
        except ValueError:
            print("Trato de convertir algo diferente a un numero")
    while True: 
            aux_ciudad = input("Ingrese su ciudad: ")
            if aux_ciudad.isalpha():
                diccionario_aux["ciudad"] = aux_ciudad
                break
            else:
                 print("Ingreso un elemento invalido")
    diccionario_aux["imc"] = aux_peso / (aux_altura*aux_altura)

    personas.append(diccionario_aux)


print("Listado de personas")
print("Nombre\t ciudad\t\t IMC")
for persona in personas:
     print(f"{persona['nombre']}\t {persona['ciudad']}\t\t {persona['imc']:.2f}")