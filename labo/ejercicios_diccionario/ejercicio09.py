# 9. Crear un diccionario que contenga los nombres, edades, fechas de nacimiento,
# numeros de telefono y correos electrónicos de un numero indeterminado de personas.
# Luego, concatenar la fecha de nacimiento y el número de teléfono de cada persona con
# el formato “11-1111-1111 – dd/mm/aaaa” y agregarlo al diccionario (usar un string
# interpolado con format para hacerlo más facil). Finalmente imprimir en consola el
# nombre, correo electrónico y los datos concatenados.


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
        while True:
            try:   
                aux_dia = int(input("Ingrese su dia de nacimiento(dd): "))
                if aux_dia > 0 and aux_dia <= 31:
                    break
                else:
                    print("El dia debe estar entre 1 y 31")
            except ValueError:
                print("Trato de convertir algo diferente a un numero")
        while True:
            try:   
                aux_mes = int(input("Ingrese su mes de nacimiento(mm): "))
                if aux_mes > 0 and aux_mes <= 12:
                    break
                else:
                    print("Debe ser un mes entre 1-12")
            except ValueError:
                print("Trato de convertir algo diferente a un numero")
        while True:
            try:   
                aux_anio = int(input("Ingrese su año de nacimiento(aaaa): "))
                if aux_anio > 1900 and aux_anio <= 2023:
                    break
                else:
                    print("El año debe estar entre 1900 y 2023")
            except ValueError:
                print("Trato de convertir algo diferente a un numero")
        diccionario_aux["fecha"] = str(aux_dia) + "/"+ str(aux_mes) + "/" + str(aux_anio)
        break

    while True:  
            aux_telefono = input("Ingrese su telefono: ")
            aux_telefono_format = ""

            if len(aux_telefono) == 10:
                for x in range(len(aux_telefono)):
                    aux_telefono_format += aux_telefono[x]
                    if x == 1 or x == 5:
                        aux_telefono_format += "-"
                diccionario_aux["telefono"] = aux_telefono_format
                break
            else:
                print("El telefono debe tener 10 digitos")

    while True:  
            aux_email = input("Ingrese su correo: ")
            if "@" in aux_email:
                diccionario_aux["email"] = aux_email
                break
            else:
                print("El correo debe tener un formato valido")

    personas.append(diccionario_aux)


print("Listado de personas")
print("Nombre\t correo\t fecha nacimiento\t telefono")
for persona in personas:
     print(f"{persona['nombre']}\t {persona['email']}\t {persona['fecha']}\t {persona['telefono']}")