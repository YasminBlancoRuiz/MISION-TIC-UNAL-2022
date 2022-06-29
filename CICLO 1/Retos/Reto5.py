
# -*- coding: utf-8 -*-


import json


import requests






contenido=requests.get("https://raw.githubusercontent.com/erik-sytnyk/movies-list/master/db.json").text


db= json.loads(contenido)

with open("reto5.json", "w") as archivo:
    json.dump(db, archivo, indent=4)





#estadisticasDirector:
DicConteo={}


for pelicula in db ["movies"]:
    if pelicula ["director"] in DicConteo:
        DicConteo [pelicula["director"]]+=1
    else:
        DicConteo [pelicula["director"]]=1

#print(DicConteo)

for i in DicConteo:
    frecuencia= DicConteo[pelicula["director"]]
    #print("El director: " + str(i)+ " tiene " + str(frecuencia) + " pelicul@s" )




#estadisticasFecha:

dicFecha={}

for ano in db ["movies"]:
    if int (ano["year"]) in dicFecha:
         dicFecha [ int (ano["year"])]+=1
    else:
        dicFecha [int (ano["year"]) ]=1

#print(dicFecha)


#estadisticasGenero

dicGeneros={}
for generos in db ["movies"]:
    for g in generos["genres"]:
        if g in dicGeneros:
            dicGeneros[g]+=1
        else:
            dicGeneros[g]=1


    #print(generos["genres"])
print(dicGeneros)




