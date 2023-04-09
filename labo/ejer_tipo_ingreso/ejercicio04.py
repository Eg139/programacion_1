# La división de alimentos está trabajando en un pequeño software para cargar las
# compras de ingredientes para la cocina de Industrias Wayne.
# Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
# para preparar comida al por mayor. En total, sabemos que se realizarán 15 compras
# de ingredientes.
# Se registra por cada compra:
# 1. PESO: (entre 10 y 100 kilos)
# 2. PRECIO POR KILO: (mayor a 0 [cero]).
# 3. TIPO VARIEDAD: (vegetal, animal, mezcla).
# Además tener en cuenta que si compro más de 100 kilos en total tengo un 15% de
# descuento sobre el precio bruto, o si compro más de 300 kilos en total, tengo un 25%
# de descuento sobre el precio bruto.
# Se desea saber:
# A. El importe total a pagar, BRUTO sin descuento.
# B. El importe total a pagar con descuento (Solo si corresponde).
# C. Informar el tipo de alimento más caro.
# D. El promedio de precio por kilo en total.

ingredientes = ['Papa','Arroz','Pescado','Nachos','Carne de res', 'Pasta', 'Tomates', 'Sake', 'Ron','Jugos','Yogurt','Leche', 'Queso']
pesos = [20,100,50,55,50,10,30,80,10,10,20,35,25]
precio_x_kilo = [100,50,300,500,200,100,50,300,200,20,100,120,180]
tipo_variedad = ['vegetal', 'vegetal', 'animal', 'mezcla','animal','mezcla','vegetal','vegetal','vegetal','vegetal','mezcla','animal','animal']

def precio_bruto(precios, kilos, long):
    precio_bruto = 0
    i = 0
    while i < long:
        precio_bruto += precios[i]*kilos[i]
        i+=1
    return precio_bruto

def descuento(kilos, precio_bruto):
    precio_descuento = 0
    if kilos > 300:
        precio_descuento = precio_bruto - (precio_bruto*0.25)
    elif kilos > 100:
        precio_descuento = precio_bruto - (precio_bruto*0.15)

    return precio_descuento

def ingreso_producto():
        Ingrediente = input("Ingrese el ingrediente: ")
        while True:
            try:
                peso = int(input("Debe estar entre 10 y 100: "))
                if peso >= 10 and peso <= 100:
                    break
                else:
                    print("Peso no permitido")
            except ValueError:
                print("Trataste de convertir algo diferente a un numero")
        while True:
            try:
                precio = float(input("Ingrese el precio: "))
                if precio > 0:
                    break
                else:
                    print("Precio no permitido")
            except ValueError:
                print("Trataste de convertir algo diferente a un numero")

        variedad = input("Ingrese la variedad del producto (vegetal, mezcla y animal): ")
        #Agregar los datos ingresados a la lista
        ingredientes.append(Ingrediente)
        pesos.append(peso)
        precio_x_kilo.append(precio)
        tipo_variedad.append(variedad)




while True:
    print("# A. El importe total a pagar, BRUTO sin descuento.")
    print("# B. El importe total a pagar con descuento (Solo si corresponde).")
    print("# C. Informar el tipo de alimento más caro.")
    print("# D. El promedio de precio por kilo en total.")
    print("# E Ingresar alimentos")
    print("# S. salir")
    opcion = input("Ingrese una opcion:  ")
    if opcion == 'A':
        print(precio_bruto(precio_x_kilo,pesos,len(ingredientes)))
    elif opcion == 'B':
        peso_total = 0
        for peso in pesos:
            peso_total += peso
        precio_descuento = descuento(peso_total,precio_bruto(precio_x_kilo,pesos,len(ingredientes)))
        print(f"El precio con descuento es {precio_descuento}")
    elif opcion == 'C':
        max = 0
        producto = ''
        i = 0
        while i < len(precio_x_kilo):
            if i == 0 or max < precio_x_kilo[i]:
                max = precio_x_kilo[i]
                producto = ingredientes[i]
            i += 1
        print(f"El alimento mas caro es: {producto} con un precio de {max} x Kg.")

    elif opcion == 'D':
        precio_total = precio_bruto(precio_x_kilo,pesos,len(ingredientes))
        kilos_total = 0
        for i in pesos:
            kilos_total += i
        promedio = precio_total / kilos_total
        print(f"El promedio de pesos x kg es {promedio}")
    elif opcion == 'E':
        ingreso_producto()
    elif opcion == 'S':
        print("Saliendo del programa")
        break

