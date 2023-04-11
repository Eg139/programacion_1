# 2-
# La real academia española nos pide desarrollar un pequeño programa que contenta el
# diccionario de la lengua española y su traducción al inglés. Para esto necesitamos un
# algoritmo que nos permita el ingreso de una palabra en español y su traducción al
# ingles y guardarlo en una lista. Si la palabra no existe, debemos agregarla, y si la
# palabra existe debemos informar que la palabra ya existe y su índice dentro del listado,
# esta carga debe ser hasta que el usuario se canse de ingresar palabras. Al finalizar se
# debe mostrar todo el listado de palabras ingresadas con su palabra equivalente en
# inglés. Recordar validar los datos de forma correcta.
from googletrans import Translator
translator = Translator()
palabras_español = []
traducciones_ingles = []
seguir = 's'


while seguir == 's':
    palabra_traducida = ''
    
    while True:
        palabra = input("Ingrese lo que desea traducir: ")
        if palabra.isalpha():
            break
        else:
            print("Eror, no se puede ingresar numeros o caracteres especiales")

    if not palabra in palabras_español:
        palabra_traducida = translator.translate(palabra,src='es', dest= 'en').text
        palabras_español.append(palabra)
        traducciones_ingles.append(palabra_traducida)
        
    else:
        indice = palabras_español.index(palabra)
        print(f"La palabra ya existe se encuentra en el indice {indice}")
        
    seguir = input("Desea seguir traduciendo palabras? s/n: ")
    while seguir != 's' and seguir != 'n':
        print("Ingrese una opcion valida.")
        seguir = input("Desea seguir traduciendo palabras? s/n: ")
print(palabras_español)
print(traducciones_ingles)
