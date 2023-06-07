import os
def sacar_max(listado:list,param:str)-> float:
    """obtiene el valor maximo dentro de una lista de diccionarios

    Args:
        listado (list): lista para recorrer
        param (str): nombre de la key a evaluar

    Returns:
        float: retorna el valor maximo encontrado
    """
    maximo = 0
    flag = False
    for individuo in listado:
        if flag == False or maximo < float(individuo[param]):
            maximo = float(individuo[param])
            flag = True
    return maximo

def sacar_min(listado:list,param:str)-> float:
    """obtiene el valor minimo dentro de una lista de diccionarios

    Args:
        listado (list): lista para recorrer
        param (str): nombre de la key a evaluar

    Returns:
        float: retorna el valor minimo encontrado
    """
    minimo = 0
    flag = False
    for individuo in listado:
        if flag == False or minimo > float(individuo[param]):
            minimo = float(individuo[param])
            flag = True
    return minimo

def buscar_float(listado:list,param:str,item_comparar:float)->list:
    """Busca los valores de una key especifica comparando con el parametro dado, de cumplirse las condiciones lo agrega en una nueva lista

    Args:
        listado (list): lista para recorrer
        param (str): nombre de la key a evaluar
        item_comparar (float): elemento a comparar con el valor de la key

    Returns:
        list: lista con los elemento que cumplen las condiciones
    """
    aux_list = []
    for individuo in listado:
        if float(individuo[param]) == item_comparar:
            aux_list.append(individuo)
    return aux_list

def buscar_string(listado:list,param:str,item_comparar:str)->list:
    """Busca los valores de una key especifica comparando con el parametro dado, de cumplirse las condiciones lo agrega en una nueva lista

    Args:
        listado (list): lista para recorrer
        param (str): nombre de la key a evaluar
        item_comparar (str): elemento a comparar con el valor de la key

    Returns:
        list: lista con los elemento que cumplen las condiciones
    """
    aux_list = []
    for individuo in listado:
        if individuo[param] == item_comparar:
            aux_list.append(individuo)
    return aux_list

def sacar_promedio(listado:list,param:str)->float:
    """_summary_

    Args:
        listado (list): lista a evaluar
        param (str): nombre de la key que se va a usar

    Returns:
        float: promedio de los elementos seleccionados
    """
    acumulador = 0
    for heroe in listado:
        acumulador += float(heroe[param])
    return acumulador/len(listado)

def mostrar_varios(listado:list,item_buscado:str,message:str):
    """imprime en consola varios individuos con mensajes

    Args:
        listado (list): lista a recorrer
        item_buscado (str): nombre de la key a evaluar
        message (str): mensaje predefinido que se mostrara
    """
    for individuo in listado:
        mostrar(individuo[item_buscado],message)

def mostrar(param:any,message:str):
    """imprime por consola un individuo con un mensaje

    Args:
        param (any): parametro que se muestra con el mensaje
        message (str): mensaje que se mostrara
    """
    print(message.format(param) )


def mostrar_menu():
    """Imprime el menu de opciones del programa
    """
    print("          ********************    MENU DE OPCIONES    **************************         ")
    print("# A. Analizar detenidamente el set de datos.")
    print("# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe.")
    print("# C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo.")
    print("# D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO).")
    print("# E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO).")
    print("# F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)")
    print("# G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)")
    print("# H. Calcular e informar cual es el superhéroe más y menos pesado.")
    print("# I. menú que permita elegir qué dato obtener.")
    print("# J. menu stark 01")
    print("# Z. salir")

def filtrar_elemento(listado:list,key:str,value:any)->dict:
    aux_dict = {}
    for individuo in listado:
        if float(individuo[key]) == value:
            aux_dict.append(individuo)
    return aux_dict

def mostrar_menu_stark_01():
    """Imprime el menu de opciones del programa
    """
    print("          ********************    MENU DE OPCIONES    **************************         ")
    print("# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M.")
    print("# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F")
    print("# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M")
    print("# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F")
    print("# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M")
    print("# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F")
    print("# G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M")
    print("# H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F")
    print("# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)")
    print("# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
    print("# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    print("# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con No Tiene).")
    print("# M. Listar todos los superhéroes agrupados por color de ojos.")
    print("# N. Listar todos los superhéroes agrupados por color de pelo.")
    print("# O. Listar todos los superhéroes agrupados por tipo de inteligencia")
    print("# Z. salir")
def elegir_menu_stark_01(lista:list):
    aux_informes = []
    while True:
        os.system('cls')
        mostrar_menu_stark_01()
        opcion = input("Ingrese una opcion:  ")
        
        match opcion:       
            case "A":
                aux = buscar_string(lista,"genero","M")
                mostrar_lista_parcial(aux,"Listado de heroes Masculinos","nombre","genero")
            case "B":
                aux = buscar_string(lista,"genero","F")
                mostrar_lista_parcial(aux,"Listado de heroes Femeninos","nombre","genero") 
            case "C":
                aux = buscar_string(lista,"genero","M")
                max_altura = sacar_max(aux,"altura")
                aux = buscar_float(aux,"altura",max_altura)
                aux_informes.append(aux[0]['nombre'])

                
            case "D":
                aux = buscar_string(lista,"genero","F")
                max_altura = sacar_max(aux,"altura")
                aux = buscar_float(aux,"altura",max_altura)
                aux_informes.append(aux[0]['nombre'])

            case "E":
                aux = buscar_string(lista,"genero","M")
                max_altura = sacar_min(aux,"altura")
                aux = buscar_float(aux,"altura",max_altura)
                aux_informes.append(aux[0]['nombre'])

            case "F":
                aux = buscar_string(lista,"genero","F")
                max_altura = sacar_min(aux,"altura")
                aux = buscar_float(aux,"altura",max_altura)

                aux_informes.append(aux[0]['nombre'])

            case "G":
                aux = buscar_string(lista,"genero","M")
                promedio = sacar_promedio(aux,"altura")
                print(f"El promedio de altura de los superheroes M es: {promedio}")
            case "H":
                aux = buscar_string(lista,"genero","F")
                promedio = sacar_promedio(aux,"altura")
                print(f"El promedio de altura de los superheroes F es: {promedio}")
            case "I":
                for heroe in aux_informes:
                    print(heroe)
            case "J":
                aux = crear_lista_srepetidos(lista,"color_ojos")
                contar_x_categoria(aux,lista,"color_ojos")
            case "K":
                aux = crear_lista_srepetidos(lista,"color_pelo")
                contar_x_categoria(aux,lista,"color_pelo")
            case "L":
                aux = inicializar_vacio(lista,"inteligencia","No Tiene")
                aux = crear_lista_srepetidos(lista,"inteligencia")
                contar_x_categoria(aux,lista,"inteligencia")                
            case "M":
                aux = crear_lista_srepetidos(lista,"color_ojos")
                mostrar_x_categoria(aux,lista,"color_ojos")
            case "N":
                aux = crear_lista_srepetidos(lista,"color_pelo")
                mostrar_x_categoria(aux,lista,"color_pelo")
            case "O":
                aux = crear_lista_srepetidos(lista,"inteligencia")
                mostrar_x_categoria(aux,lista,"inteligencia")                
            case "Z":
                print("Saliendo del programa")    
                break
            case _:
                print("Opcion invalida.")
        os.system("pause")

def crear_lista_srepetidos(listado:list,item:str)->list:
    aux = []
    for heroe in listado:
        if not filtrar_repetidos(aux,heroe[item]):
            aux.append(heroe[item])
    return aux

def filtrar_repetidos(lista:list, item:str)->bool:
    esta = False
    for elemento in lista:
        if (elemento == item):
            esta = True
            break
    return esta

def mostrar_x_categoria(categorias:list,lista:list,item:str):
    for categoria in categorias:
        print(f"Lista de {categoria}")
        for heroe in lista:
            if heroe[item] == categoria:
                print(f"{heroe['nombre']}  {heroe['color_pelo']}")
        print("\n------------------------------------\n")

def contar_x_categoria(categorias:list,lista:list,item:str):
    for categoria in categorias:
        print(f"Lista de {categoria}")
        contador = 0
        for heroe in lista:
            if heroe[item] == categoria:
                contador+=1
        print(f"Los heroes contados son: {contador}")    
        print("\n------------------------------------\n")

def inicializar_vacio(lista:list,key:str,message:str):
    for heroe in lista:
        if heroe[key] == "":
            heroe[key] = message

def submenu():
    """Imprime por consola un sub menu
    """
    print("          ********************    MENU DE OPCIONES    **************************         ")
    print("# A. nombre.")
    print("# B. identidad.")
    print("# C. empresa.")
    print("# D. altura.")
    print("# E. peso.")
    print("# F. genero")
    print("# G. color de ojos")
    print("# H. color de pelo.")
    print("# I. fuerza.")
    print("# J. inteligencia.")
    print("# Z. salir")

def elegir_submenu(listado:list, titulo:str):
    """Elije una opcion del menu y ejecuta lo solicitado de la opcion

    Args:
        listado (list): lista a recorrer
        titulo (str): titulo de las listas que se generan en las opciones
    """
    while True:
        os.system('cls')
        
        submenu()
        opcion = input("Ingrese una opcion: ")

        if opcion == "A":
            param_buscado = "nombre"
            print(titulo.format(param_buscado))
            mostrar_varios(listado,param_buscado,"{}")
        elif opcion == "B":
            param_buscado = "identidad"
            print(titulo.format(param_buscado))
            mostrar_varios(listado,param_buscado,"{}")
        elif opcion == "C":
            param_buscado = "empresa"
            print(titulo.format(param_buscado))
            mostrar_varios(listado,param_buscado,"{}")

        elif opcion == "D":
            param_buscado = "altura"
            print(titulo.format(param_buscado))
            mostrar_varios(listado,param_buscado,"{}")

        elif opcion == "E":
            param_buscado = "peso"
            print(titulo.format(param_buscado))
            mostrar_varios(listado,param_buscado,"{}")

        elif opcion == "F":
            param_buscado = "genero"
            print(titulo.format(param_buscado))
            mostrar_varios(listado,param_buscado,"{}")

        elif opcion == "G":
            param_buscado = "color_ojos"
            print(titulo.format(param_buscado))
            mostrar_varios(listado,param_buscado,"{}")

        elif opcion == "H":
            param_buscado = "color_pelo"
            print(titulo.format(param_buscado))
            mostrar_varios(listado,param_buscado,"{}")
    
        elif opcion == "I":
            param_buscado = "fuerza"
            print(titulo.format(param_buscado))
            mostrar_varios(listado,param_buscado,"{}")
        elif opcion == "J":
            param_buscado = "inteligencia"
            print(titulo.format(param_buscado))
            mostrar_varios(listado,param_buscado,"{}")
            
        elif opcion == "Z":
            print("Saliendo del submenu")    
            break
        else:
            print("Opcion invalida.")
        os.system('pause')


def mostrar_lista_parcial(listado:list,titulo:str,param1:str,param2:str=""):
    """se muestra por consola solo los parametros dados por el usuario de una lista

    Args:
        listado (list): lista a recorrer
        titulo (str): encabezado de la lista
        param1 (str): nombre de la key a mostrar
        param2 (str, optional): nombre de la key a mostrar. Defaults to "".
    """
    print(titulo)
    print(f"{param1}\t {param2}\t")
    for individuo in listado:
        if param2 == "":
            print(f"{individuo[param1]}\t")
        else:
            print(f"{individuo[param1]}\t {individuo[param2]}\t")
