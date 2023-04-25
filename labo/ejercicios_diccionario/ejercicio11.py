# 11. Crear un diccionario que contenga los nombres, edades, saldos en cuentas bancarias y
# un codigo de cliente (debe ser un string de 8 caracteres alfanumérico) y un porcentaje
# de impuesto a aplicar. Imprimir por consola el codigo del cliente y el balance final de la
# cuenta.



tam = 5
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
            aux_saldo = float(input("Ingrese el saldo de su cuenta bancaria "))
            break
        except ValueError:
            print("Trato de convertir algo diferente a un numero")

    while True:
            aux_codigo = input("Ingrese su codigo alfanumerico de 8 numeros: ")
            if len(aux_codigo) == 8 and aux_codigo.isalpha():
                diccionario_aux["codigo"] = aux_codigo
                break
            else:
                print("Ingreso algo diferente a alfanumerico")

    while True:
        try:   
            aux_impuesto = int(input("Ingrese el impuesto: "))
            if aux_impuesto > 0 and aux_impuesto <= 100:
                break
            else:
                print("El impuesto no puede ser 0 ni negativo")
        except ValueError:
            print("Trato de convertir algo diferente a un numero")   

    diccionario_aux["saldo"] = aux_saldo - aux_saldo * aux_impuesto/100

    personas.append(diccionario_aux)


print("Listado de personas")
print("Codigo\t Balance final")
for persona in personas:
     print(f"{persona['codigo']}\t {persona['saldo']:.2f}")