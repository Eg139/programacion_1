# 1. Crear un diccionario que contenga los nombres y edades de 5 personas. Luego
# imprimir por pantalla el nombre y la edad de cada persona.

personas = [{"nombre":"pepe","edad":50},{"nombre":"dardo","edad":50},{"nombre":"coki","edad":17},{"nombre":"paola","edad":18},{"nombre":"moni","edad":49}]


print("Listado de personas")
print("Nombre\t Edad\t")
for persona in personas:
     print(f"{persona['nombre']}\t {persona['edad']:2d}\t")