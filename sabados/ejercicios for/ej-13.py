#Dada una lista de palabras, imprimir las palabras que tienen una longitud impar.

palabras = ["ala","Ozaru", "Vegeta", "Namekusein", "Milk","oso"]


for palabra in palabras:
    if len(palabra) % 2 != 0:
        print(palabra)
