

import json


datos={"1":"X", "4":"X", "7":"X", "10":"🚗", "2":"X", "5":"X", "8":"🚗", "11":"X", "3":"X", "6":"🚗", "9":"x", "12":"X"}


#creo Json para crear el archivo y guardar información
with open("parque.json", "w") as archivo:
    json.dump(datos, archivo)


#me carga el archivo
with open("parque.json", "r") as archivo:
    json.load(archivo)



print(datos)


print()

#🚗
#Crear matriz

filas=3
columnas=4

matriz=[]

#me ayuda a llenar la matriz

for f in range (filas):
    matriz.append([])
    for c in range (columnas):
        matriz[f].append("L")



# imprimiendo la matriz
for f in range(filas):
    for c in range(columnas):
        print(matriz[f][c], end=" ") # end=" " me sirve para pasar de renglon sin dejar espacio
    print() # este print me ayuda a dar un espacio

print()

listaDatoskeys=list(datos.keys())
listaDatosvalues=list(datos.values())
print(listaDatoskeys)
print(listaDatosvalues)


#listaDatoskeys.sort()
print(listaDatoskeys)


posicionesnumeros="1,2,3,4,5,6,7,8,9,10,11,12"
posiciones=posicionesnumeros.split(",")
print(posiciones)

cadenafila="012012012012"
cadenacolumna="000111222333"

print(cadenafila[9])
print(cadenacolumna[9])

print(posiciones)
print(posiciones[5])





for f in range(len(posiciones)):
    for c in range(len(listaDatoskeys)):

        if posiciones[f]== listaDatoskeys[c]:
            matriz[int(cadenafila[f])][int(cadenacolumna[f])]=listaDatosvalues[c]



#Imprimir matriz
for f in range (filas):
    for c in range (columnas):
        print(matriz[f][c], end=" ")
    print()



