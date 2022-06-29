
# -*- coding: utf-8 -*-

def estadisticasDirector(db):
   """
   Retorna un diccionario con los nombres de los directores de cine como llave y
   para cada uno la cantidad de películas correspondientes (valor entero)
   """
   resultado = {}
   #implementar lógica

   for pelicula in db:
      if pelicula ["director"] in resultado:
         resultado [pelicula["director"]]+=1
      else:
         resultado [pelicula["director"]]=1

   return resultado


#for i in DicConteo:
    #frecuencia= DicConteo[pelicula["director"]]
    #print("El director: " + str(i)+ " tiene " + str(frecuencia) + " pelicul@s" )

def estadisticasFecha(db):
   """
   Retorna un diccionario que tienen como llaves los años en que se hicieron las película (valor
   entero) y para cada año la cantidad de películas correspondientes (valor entero)
   """
   resultado = {}
   #implementar lógica
   for ano in db:
      if int (ano["year"]) in resultado:
            resultado [ int (ano["year"])]+=1
      else:
         resultado [int (ano["year"]) ]=1

   return resultado


def estadisticasGenero(db):
   """
   Retorna un diccionario con los géneros como llave y para cada género la
   cantidad de películas correspondientes (valor entero)
   """
   resultado = {}
   #implementar lógica
   for generos in db:
      for g in generos["genres"]:
         if g in resultado:
               resultado[g]+=1
         else:
               resultado[g]=1

   return resultado

