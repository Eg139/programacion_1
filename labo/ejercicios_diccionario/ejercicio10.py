# 10. Crear un diccionario que contenga los nombres, edades, alturas (en centímetros) y
# géneros de 10 personas. Luego, convertir las alturas de centímetros a pies y pulgadas
# sabiendo que un pie son 30.48 cm y 1 pulgada son 2.54 cm) y agregar los datos al
# diccionario. Finalmente, imprimir en consola los nombres de las personas con su
# genero y su altura en pies y pulgadas.


tam = 10
personas = []
for x in range(tam):
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
            aux_altura = float(input("Ingrese su altura en cm: "))
            if aux_altura > 0:
                diccionario_aux["altura_cm"] = aux_altura
                break
            else:
                print("La altura debe ser positiva")
        except ValueError:
            print("Trato de convertir algo diferente a un numero")

    while True:
            aux_genero = input("Ingrese su genero(f/m/otro): ")
            if aux_genero == 'f' or aux_genero == 'm' or aux_genero == 'otro':
                diccionario_aux["genero"] = aux_genero
                break
            else:
                print("Los dias no pueden ser negativos")

    diccionario_aux["altura_pulgadas"] = aux_altura / 2.54
    diccionario_aux["altura_pies"] = aux_altura / 30.48

    personas.append(diccionario_aux)


print("Listado de personas")
print("Nombre\t genero\t pulgadas\t Pies")
for persona in personas:
     print(f"{persona['nombre']}\t {persona['genero']}\t {persona['altura_pulgadas']:.2f}\t {persona['altura_pies']:.2f}")