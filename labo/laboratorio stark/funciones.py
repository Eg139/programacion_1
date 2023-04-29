import os
def sacar_max(listado:list,param:str):
    maximo = 0
    flag = False
    for individuo in listado:
        if flag == False or maximo < float(individuo[param]):
            maximo = float(individuo[param])
            flag = True
    return maximo

def sacar_min(listado:list,param:str):
    minimo = 0
    flag = False
    for individuo in listado:
        if flag == False or minimo > float(individuo[param]):
            minimo = float(individuo[param])
            flag = True
    return minimo

def buscar_float(listado:list,param:str,item_comparar:float):
    aux_list = []
    for individuo in listado:
        if float(individuo[param]) == item_comparar:
            aux_list.append(individuo)
    return aux_list

def buscar_string(listado:list,param:str,item_comparar:str,message:str):
    for individuo in listado:
        if individuo[param] == item_comparar:
            print(message+ individuo[param])

def sacar_promedio(listado:list,param:str):
    acumulador = 0
    for heroe in listado:
        acumulador += float(heroe[param])
    return acumulador/len(listado)

def mostrar_varios(listado:list,item_buscado:str,message:str):
    for individuo in listado:
        mostrar(individuo[item_buscado],message)

def mostrar(param:any,message:str):
    print(message.format(param) )


def mostrar_menu():
    print("          ********************    MENU DE OPCIONES    **************************         ")
    print("# A. Analizar detenidamente el set de datos.")
    print("# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe.")
    print("# C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo.")
    print("# D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO).")
    print("# E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO).")
    print("# F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)")
    print("# G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)")
    print("# H. Calcular e informar cual es el superhéroe más y menos pesado.")
    print("# I. Ordenar el código implementando una función para cada uno de los valores informados.")
    print("# J. Construir un menú que permita elegir qué dato obtener.")
    print("# Z. salir")

def submenu():
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
    print(titulo)
    print(f"{param1}\t {param2}\t")
    for individuo in listado:
        if param2 == "":
            print(f"{individuo[param1]}\t")
        else:
            print(f"{individuo[param1]}\t {individuo[param2]}\t")
