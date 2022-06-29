
#from ast import dump
import json
#from ntpath import join
#from this import d
#from xml.etree.ElementTree import register_namespace


datos_triki= input("Ingrese diccionario: ")

datos_triki=json.loads(datos_triki)



#dump guarda la información en el archivo
with open("base.json", "w") as archivo:
    json.dump(datos_triki, archivo)

#Para cargar la información y visualizarlos
with open("base.json", "r") as archivo:
    datos_triki = json.load(archivo)
    #print(datos_triki)


matriz=[]

filas=3
columnas=3

for f in range(filas):
    matriz.append([])
    for c in range(columnas):
        matriz[f].append("*")

''''''''''
for f in range(filas):
    for c in range(columnas):
        print (matriz[f][c], end=" ")
    print()

'''''''''   

lista_Triki=list(datos_triki.keys())
lista_Triki1=list(datos_triki.values())


#print(lista_Triki)
#print(lista_Triki1)




Lista1="123456789"
Lista2="000111222"
Lista3="012012012"

for l1 in range(len("".join(lista_Triki))):
    for l2 in range(len("".join(Lista1))):
        if int("".join(lista_Triki[l1])) == int(Lista1[l2]):
            matriz[int(Lista2[l2])][int(Lista3[l2])]=str(lista_Triki1[l1])
            

for f in range(filas):
    for c in range(columnas):
        print (matriz[f][c], end=" ")
    print()

bandera=0
for f in range(3):
    
    if matriz[f][0]== matriz[f][1] and matriz[f][1] ==matriz[f][2]:
            print("El Ganador es ["+  matriz[f][0] + "]")
            bandera=1
            break
    if matriz[0][f]==matriz[1][f] and matriz[1][f]==matriz[2][f]:
            print("El Ganador es ["+  matriz[0][f] + "]")
            bandera=1
            break



if matriz[0][0]==matriz[1][1] and matriz[1][1]==matriz[2][2] and bandera !=1:
    print("El Ganador es ["+  matriz[0][0] + "]")
    bandera=1
    

if matriz[0][2]==matriz[1][1] and matriz[1][1]==matriz[2][0] and bandera !=1:
    print("El Ganador es ["+  matriz[0][2] + "]")
    bandera=1
        
            
if bandera==0:
    print("Sin Ganador [EMPATE]")



 