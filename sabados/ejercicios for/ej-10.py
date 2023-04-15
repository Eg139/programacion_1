#Dada una lista de palabras, imprimir las palabras que comienzan y terminan con la misma letra.

palabras = ["ala","Ozaru", "Vegeta", "Namekusein", "Milk","oso"]


for palabra in palabras:
    flag = 0
    contador = 0
    primer_letra = ""
    ultima_letra = ""
    longitud = len(palabra)
    for letra in palabra:
        
        contador += 1
        if flag == 0:
            primer_letra = letra
            flag = 1
        if contador == longitud:
            ultima_letra = letra
            if ultima_letra == primer_letra:
                print(palabra)
