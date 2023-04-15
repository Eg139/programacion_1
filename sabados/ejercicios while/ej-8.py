# Dada una cadena de texto, imprimir la cantidad de vocales en la cadena.
palabra = "Siames"
vocales = ['a','e','i','o','u','A','E','I','O','U']
i = 0;
contador = 0
while i < len(palabra):
    if palabra[i] in vocales:
        contador += 1
    i += 1
print(contador)
