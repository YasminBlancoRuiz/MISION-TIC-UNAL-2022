
#Tuplas con tuplas como elementos (anidadas). Para el programa
tuple1=(0,1,2,3)
tuple2=("A","B","C")
tuple3=(tuple1,tuple2)

print(tuple3)
print(tuple3[0])
print(tuple3[1])
print(tuple3[1][0])

#Concatena dos tuplas. Para el programa
tup1 = ("A", "B", "C", "E")
tup2 = (1, 2, 3, 4, 5)
tup3 = tup1 + tup2
print(tup3)

#Concatena dos tuplas. Para el programa

tup1=("A","B","C","E")
tup2=(1,2,3,4,5)
tup3=tup1+tup2
print(tup3)

#Crea una tupla con m ́ultiples copias de una tupla, tantas como se defina.
#Para el programa

tup2 = (1, 2, 3, 4, 5)
tup3 = tup2 * 3
print(tup3)

tup4 = ("Abc", "Bcd")
tup5 = tup4 * 2
print(tup5)

text = ("cien", "a~nos", "de", "soledad")
if "a~nos" in text:
    print("Si est ́a en la tupla")
else:
    print("No est ́a en la tupla")

''''''''''
#LETRAS PLACA, NUMEROS, PLACA, TIPO, ID, NUMERO ID, FECHA
"XSD",234,"CC",213123,"2022-01-23"
"XDD",343,"CC",324234,"2022-02-14"
'''''''''''
