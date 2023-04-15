#Dada una lista de palabras, imprimir la cantidad total de vocales en la lista.
palabras = ["Ozaru", "Vegeta", "Namekusein", "Milk"]
vocales = ['a','A','e','E','i','I','o','O','u','U']

cantidad_vocales = 0

for palabra in palabras:
    for letra in palabra:
        if letra in vocales:
            cantidad_vocales += 1        

print("Las vocales son: ", cantidad_vocales)
