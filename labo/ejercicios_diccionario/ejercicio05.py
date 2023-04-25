# 5. Crear un diccionario que contenga los nombres de 20 estudiantes y sus respectivas
# notas en un examen. Luego imprimir el nombre del estudiante con la nota más alta.
from data05 import alumnos

maximo = 0
aux_nombre = ""
flag = False
for alumno in alumnos:
    if flag == False or maximo < alumno["nota"]:
        maximo = alumno["nota"]
        aux_nombre = alumno["nombre"]
        flag = True

print(f"La nota maxima: {maximo} pertenece al alumno {aux_nombre}")