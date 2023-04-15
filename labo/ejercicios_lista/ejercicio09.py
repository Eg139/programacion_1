# 9-
# Realizar un programa que pida una cadena de texto al usuario y le pida una cadena de
# texto y determine que la cadena ingresada es un palíndromo o no. De serlo deberá
# imprimir la palabra por consola.
palabra = ""
palabra_invertida = ""
while True:
    palabra = input("Ingrese una palabra: ")
    if palabra.isalpha():
        # palabra_invertida = ''.join(reversed(palabra))
        break
    else:
        print("Eror, no se puede ingresar numeros o caracteres especiales")
for letra in palabra:
    palabra_invertida = letra + palabra_invertida

if palabra == palabra_invertida:
    print(f"La cadena de texto {palabra} es un palindromo.")
else:
    print("La cadena de texto no es un palindromo")