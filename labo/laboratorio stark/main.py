import os
from data_stark import lista_personajes
from funciones import *

while True:
    lista_heroes = []
    for heroe in lista_personajes:
        lista_heroes.append(heroe.copy())
    print(lista_heroes)
    os.system('cls')
    mostrar_menu()
    tam = len(lista_heroes)
    opcion = input("Ingrese una opcion:  ")
    
    match opcion:       
        case "A":
            print("Listado de superheroes")
            print("Nombre\t Identidad\t Empresa\t Altura\t Peso\t")
            for superheroe in lista_heroes:
                print(f"{superheroe['nombre']}\t {superheroe['identidad']}\t {superheroe['empresa']}\t {superheroe['altura']}\t {superheroe['peso']}\t")
        case "B":
            param_mostrar_1 = "nombre"
            mostrar_lista_parcial(lista_heroes,"Lista de superheroes",param_mostrar_1)
        case "C":
            param_mostrar_1 = "nombre"
            param_mostrar_2 = "altura"
            mostrar_lista_parcial(lista_heroes,"Lista de superheroes",param_mostrar_1,param_mostrar_2)
        case "D":
            param_buscar = "altura"
            maximo = sacar_max(lista_heroes,param_buscar)
            aux_maximo = buscar_float(lista_heroes,param_buscar,maximo)
            mostrar_varios(aux_maximo,param_buscar,"La altura maxima es de : {}")
        case "E":
            param_buscar = "altura"
            minimo = sacar_min(lista_heroes,param_buscar)
            aux_minimo = buscar_float(lista_heroes,param_buscar,minimo)
            mostrar_varios(aux_minimo,param_buscar,"La altura minima es de :")

        case "F":
            param_buscar = "altura"
            promedio = sacar_promedio(lista_heroes,param_buscar)
            mostrar(promedio,"El Promedio de altura de los superheroes es de: ")
        case "G":
            maximo = sacar_max(lista_heroes,"altura")
            minimo = sacar_min(lista_heroes,"altura")

            list_max = buscar_float(lista_heroes,"altura",maximo)
            list_min = buscar_float(lista_heroes,"altura",minimo)

            mostrar_varios(list_max,"nombre","La altura maxima pertenece al superheroe: ")
            mostrar_varios(list_min,"nombre","La altura minima pertenece al superheroe: ")
    
        case "H":
            param_buscar = "peso"
            maximo = sacar_max(lista_heroes,param_buscar)
            minimo = sacar_min(lista_heroes,param_buscar)
            list_max = buscar_float(lista_heroes,param_buscar,maximo)
            list_min = buscar_float(lista_heroes,param_buscar,minimo)

            mostrar_varios(list_max,"nombre","El peso mas alto pertenece al superheroe: ")
            mostrar_varios(list_min,"nombre","El peso mas bajo pertenece al superheroe: ")
        case "I":
            elegir_submenu(lista_heroes,"Listado de Superheroes - {}")
        case "J":
            elegir_menu_stark_01(lista_heroes)
        case "Z":
            print("Saliendo del programa")    
            break
        case _:
            print("Opcion invalida.")

    os.system('pause')

