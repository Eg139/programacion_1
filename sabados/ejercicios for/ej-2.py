#Dada una lista de palabras, imprimir la palabra más larga de la lista.

palabras = ["Ozaru", "Vegeta", "Namekusein", "Milk"]
flag = 0

for i in palabras:
    if flag == 0 or len(i) > len(maximo) :
        maximo = i
        flag = 1
        
print("El numero mas grande es: ",maximo)