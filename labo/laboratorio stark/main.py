import os
from data_stark import lista_personajes
from funciones import *

while True:
    os.system('cls')
    mostrar_menu()
    tam = len(lista_personajes)
    opcion = input("Ingrese una opcion:  ")
    
            
    if opcion == "A":
        print("Listado de superheroes")
        print("Nombre\t Identidad\t Empresa\t Altura\t Peso\t")
        for superheroe in lista_personajes:
            print(f"{superheroe['nombre']}\t {superheroe['identidad']}\t {superheroe['empresa']}\t {superheroe['altura']}\t {superheroe['peso']}\t")
    elif opcion == "B":
        param_mostrar_1 = "nombre"
        mostrar_lista_parcial(lista_personajes,"Lista de superheroes",param_mostrar_1)
    elif opcion == "C":
        param_mostrar_1 = "nombre"
        param_mostrar_2 = "altura"
        mostrar_lista_parcial(lista_personajes,"Lista de superheroes",param_mostrar_1,param_mostrar_2)
    elif opcion == "D":
        param_buscar = "altura"
        maximo = sacar_max(lista_personajes,param_buscar)
        aux_maximo = buscar_float(lista_personajes,param_buscar,maximo)
        mostrar_varios(aux_maximo,param_buscar,"La altura maxima es de : {}")
    elif opcion == "E":
        param_buscar = "altura"
        minimo = sacar_min(lista_personajes,param_buscar)
        aux_minimo = buscar_float(lista_personajes,param_buscar,minimo)
        mostrar_varios(aux_minimo,param_buscar,"La altura minima es de :")

    elif opcion == "F":
        param_buscar = "altura"
        promedio = sacar_promedio(lista_personajes,param_buscar)
        mostrar(promedio,"El Promedio de altura de los superheroes es de: ")
    elif opcion == "G":
        maximo = sacar_max(lista_personajes,"altura")
        minimo = sacar_min(lista_personajes,"altura")

        list_max = buscar_float(lista_personajes,"altura",maximo)
        list_min = buscar_float(lista_personajes,"altura",minimo)

        mostrar_varios(list_max,"nombre","La altura maxima pertenece al superheroe: ")
        mostrar_varios(list_min,"nombre","La altura minima pertenece al superheroe: ")
 
    elif opcion == "H":
        param_buscar = "peso"
        maximo = sacar_max(lista_personajes,param_buscar)
        minimo = sacar_min(lista_personajes,param_buscar)
        list_max = buscar_float(lista_personajes,param_buscar,maximo)
        list_min = buscar_float(lista_personajes,param_buscar,minimo)

        mostrar_varios(list_max,"nombre","El peso mas alto pertenece al superheroe: ")
        mostrar_varios(list_min,"nombre","El peso mas bajo pertenece al superheroe: ")

 
    elif opcion == "J":
        elegir_submenu(lista_personajes,"Listado de Superheroes - {}")

    elif opcion == "Z":
        print("Saliendo del programa")    
        break
    else:
        print("Opcion invalida.")

    os.system('pause')

