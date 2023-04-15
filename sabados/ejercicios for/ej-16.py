#Dada una lista de palabras, imprimir las palabras que tienen una letra específica.

palabras = ["ala","Ozaru", "Vegeta", "Namekusein", "Milk","oso"]
letra_especifica = 'a'

for palabra in palabras:
    if letra_especifica in palabra:
        print(palabra)
