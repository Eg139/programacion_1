# 8. Crear un diccionario que contenga los nombres, edades, salario por día, días trabajados
# de 10 empleados. Luego, calcular el salario total de cada empleado y agregarlo al
# diccionario. Finalmente, imprimir en consola los nombres de los empleados junto con
# la edad y el salario total.

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
            aux_salario = float(input("Ingrese su salario diario: "))
            if aux_salario > 0:
                diccionario_aux["salario_diario"] = aux_salario
                break
            else:
                print("La altura debe ser positiva")
        except ValueError:
            print("Trato de convertir algo diferente a un numero")

    while True:
        try:   
            aux_dias_trabajo = int(input("Ingrese los dias trabajados: "))
            if aux_dias_trabajo > 0:
                diccionario_aux["dias"] = aux_dias_trabajo
                break
            else:
                print("Los dias no pueden ser negativos")
        except ValueError:
            print("Trato de convertir algo diferente a un numero")

    diccionario_aux["sueldo"] = aux_salario * aux_dias_trabajo

    personas.append(diccionario_aux)


print("Listado de personas")
print("Nombre\t edad\tsueldo")
for persona in personas:
     print(f"{persona['nombre']}\t {persona['edad']:2d}\t {persona['sueldo']:.2f}")