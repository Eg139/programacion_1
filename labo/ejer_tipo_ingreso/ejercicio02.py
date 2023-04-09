# Debemos hacer un programa para que el usuario recuerde las reglas de estilo de
# python, entonces debemos pedirle al usuario un número entre el 1 y el 8,
# al ingresar el número debemos mostrarle que regla de estilo representa y su
# descripción (Sacar la información de las diapositivas de las reglas de estilo).
# En caso de que ingrese un numero fuera del rango deberá mostrarle al usuario “Error,
# regla de estilo inexistente”
seguir = 's'

while seguir == 's':

    while True:
        try:
            opcion = int(input("Ingrese una opcion del 1 al 8 para ver una regla de estilo:  "))
            if opcion <=8 and opcion >= 1:
                break
            else:
                print("Opcion invalida")
        except ValueError:
            print("Trataste de convertir algo diferente a un numero")
    if opcion == 1:
        print(" Diseño del código Usa 4 (cuatro) espacios por indentación.")
    elif opcion == 2:
        print("Nunca mezcles tabulaciones y espacios.")
    elif opcion == 3:
        print("Limita todas las líneas a un máximo de 79 caracteres")
    elif opcion == 4:
        print("Líneas en blanco Separa funciones de alto nivel y definiciones de clase con dos líneas en blanco. Definiciones de métodos dentro de una clase son separadas por una línea en blanco.")
    elif opcion == 5:
        print("Las importaciones deben estar en líneas separadas. Las importaciones siempre se colocan al comienzo del archivo, simplemente luego de cualquier comentario o documentación del módulo, y antes de globales y constantes") 
    elif opcion == 6:
        print("Los módulos deben tener un nombre corto y en minúscula. Guiones bajos pueden utilizarse si mejora la legiblidad. Los paquetes en Python también deberían tener un nombre corto y en minúscula, aunque el uso de guiones bajos es desalentado") 
    elif opcion == 7:  
        print("Casi sin excepción, los nombres de clases deben utilizar la convención “CapWords” (palabras que comienzan con mayúsculas). Clases para uso interno tienen un guión bajo como prefijo.")  
    elif opcion == 8:
        print("Las funciones deben ser en minúscula, con las palabras separadas por un guión bajo, aplicándose éstos tanto como sea necesario para mejorar la legibilidad.")
    seguir = input("Desea seguir eligiendo opciones s/n:  ")

