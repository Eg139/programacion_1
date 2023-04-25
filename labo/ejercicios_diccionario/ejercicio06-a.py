# 6. Rehacer los primeros 5 ejercicios pero sin hardcodear los diccionarios, es decir, el
# diccionario debe empezar vacio y deberán cargar las claves y valores del diccionario
# por consola.

# 1. Crear un diccionario que contenga los nombres y edades de 5 personas. Luego
# imprimir por pantalla el nombre y la edad de cada persona.

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
    personas.append(diccionario_aux)

print("Listado de personas")
print("Nombre\t Edad\t")
for persona in personas:
     print(f"{persona['nombre']}\t {persona['edad']:2d}\t")