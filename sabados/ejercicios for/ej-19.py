#Dada una lista de palabras, imprimir las palabras que tienen una letra mayúscula.
import string
palabras = ["ala","Ozaru", "Vegeta", "Namekusein", "Milk","oso"]
mayusculas = string.ascii_uppercase

for palabra in palabras:
    for letra in palabra:
        if letra in mayusculas:
            print(palabra)
            break