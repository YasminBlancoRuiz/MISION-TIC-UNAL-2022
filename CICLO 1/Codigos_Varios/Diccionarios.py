


import json

from turtle import end_fill

''''''''''
triki={
   "1":"O" " " , 
   "2":"O" " ",
   "3":"O" " ",
   "4":"O" " ",
   "5":"O" " ",
   "6":"X" " ",
   "7":"X" " ",
   "8":"X" " ",
   "9":"X" " ",

}

#Me imprime el diccionario
print(triki)

#Convierto el diccionario a lista
print(list(triki.values()))

#lo imprimo en cadena por espacios
print(("".join(triki.values())))

for i in triki:
   print(i)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


#Diccionario creado
datos_triki={
   "1":"O" " " , 
   "2":"O" " ",
   "3":"O" " ",
   "4":"O" " ",
   "5":"O" " ",
   "6":"X" " ",
   "7":"X" " ",
   "8":"X" " ",
   "9":"X" " ",

}


# Este método dumps recibe como argumento una expresion de diccionario y crea como resultado 
# una cadena con la representación de formato JSON
cadena_json= json.dumps(datos_triki)
print(cadena_json)

print()

#Escritura:

with open("base.json", "w") as archivo:
    json.dump(datos_triki, archivo)

print()

#Lectura

with open("base.json", "r") as archivo:
    cadena_json=json.loads(archivo)

print(cadena_json) 

