# Dada una cadena de texto, imprimir la cantidad de veces que aparece una letra específica en la cadena.
palabra = "Siames macho"
longitud = len(palabra)
i = 0;
contador = 0
letra = 'm'
while i < longitud:
    if palabra[i] == letra:
        contador+=1
    i += 1
print(contador)
