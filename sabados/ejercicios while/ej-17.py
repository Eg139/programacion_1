# Dada una cadena de texto, imprimir la cadena al revés.
cadena = "Esto es una cadena"
cadena_invertida = ""
i = 0
while i < len(cadena):
    cadena_invertida = cadena[i] + cadena_invertida
    i+=1
print(cadena_invertida)
