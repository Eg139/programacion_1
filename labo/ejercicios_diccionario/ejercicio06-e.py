# 5. Crear un diccionario que contenga los nombres de 20 estudiantes y sus respectivas
# notas en un examen. Luego imprimir el nombre del estudiante con la nota más alta.
alumnos = []
tam = 4
maximo = 0
aux_nombre = ""
flag = False

for x in range(tam):
    diccionario_aux = {}
    
    while True: 
            aux_alumno = input("Ingrese el nombre: ")
            if aux_alumno.isalpha():
                diccionario_aux['nombre'] = aux_alumno
                break
            else:
                 print("Ingreso un elemento invalido.\n")
    
    while True:
        try:   
            aux_notas = float(input("Ingrese la nota del examen: "))
            if aux_notas >= 0:
                diccionario_aux["nota"] = aux_notas
                break
            else:
                print("Debe ser un numero mayor o igual a 0")
        except ValueError:
            print("Trato de convertir algo diferente a un numero")

    alumnos.append(diccionario_aux)



for alumno in alumnos:
    if flag == False or maximo < alumno["nota"]:
        maximo = alumno["nota"]
        aux_nombre = alumno["nombre"]
        flag = True

print(f"La nota maxima: {maximo} pertenece al alumno {aux_nombre}")