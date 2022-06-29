
from ast import dump
import json
from ntpath import join
from this import d
from xml.etree.ElementTree import register_namespace


#Diccionario creado
datos_triki={
   "3":"O", 
   "6":"X",
   "2":"O",
   "7":"X",
   "5":"O",
   "9":"X",
   "4":"O",
   "8":"X",
   "9":"X",

}

datos_triki2={
   "1":"[0][0]", 
   "2":"[0][1]",
   "3":"[0][2]",
   "4":"[1][0]",
   "5":"[1][1]",
   "6":"[1][2]",
   "7":"[2][0]",
   "8":"[2][1]",
   "9":"[2][2]",

}

#Me trae la longitud total del diccionario item
#print(len(datos_triki2))
print(len(datos_triki2["7"]))
#Me trae lo que hay dentro de la posición
print(datos_triki2["6"])
print(datos_triki2.get("6"))






#dump guarda la información en el archivo
with open("base.json", "w") as archivo:
    json.dump(datos_triki, archivo)

#Para cargar la información y visualizarlos
with open("base.json", "r") as archivo:
    print(json.load(archivo))


matriz=[]

filas=3
columnas=3

for f in range(filas):
    matriz.append([])
    for c in range(columnas):
        matriz[f].append("*")

for f in range(filas):
    for c in range(columnas):
        print (matriz[f][c], end=" ")
    print()
   

print()


lista_Triki=list(datos_triki.keys())
lista_Triki1=list(datos_triki.values())

lista_Triki.sort()
lista_Triki1.sort()
print(lista_Triki)
print(lista_Triki1)

print()

lista_Triki2=list(datos_triki2.keys())
lista_Triki3=list(datos_triki2.values())


lista_Triki2.sort()
lista_Triki3.sort()
print(lista_Triki2)
print(lista_Triki3)



for l1 in range(len("".join(lista_Triki))):
    for l2 in range(len("".join(lista_Triki2))):
        if "".join(lista_Triki[l1])== "".join(lista_Triki2[l2]):
            print(lista_Triki3[l2])
            #matriz[l2][l2]="".join(lista_Triki1[l1])
            print(matriz)

    print(matriz)