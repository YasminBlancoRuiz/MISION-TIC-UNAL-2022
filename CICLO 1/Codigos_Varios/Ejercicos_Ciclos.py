

#Escribir un programa que muetre la sumatoria de todos los números entre el 0 y 100

from math import factorial


suma=0

for i in range(101):
    suma=suma+i

print("La sumatoria de todos los números entreo el cero y 100 es: " + str(suma) )

print()

#¿Qué modificación habría que hacer si ahora sólo se deben sumar los números que sean múltiplos de 3?

suma=0

for i in range(101):
    if i%3==0:
        suma=suma+i

print("La suma de los múltiplos de 3 son : " + str(suma) )

print()

#Dado un número entero positivo, mostrar su factorial.
#El factorial de un número se obtiene multiplicando todos los números entre positivos que hay entre el 1 y ese número.
#El factorial de 0 es 1


#num= int( input("Ingrese número del factorial: ") )
num=5
fact=1

if num>0:
    for i in range(1, num+1):
        fact=fact*i

else:
    print("El factorial es " + str (fact) )        


print("El factorial de " + str (num) + " es " + str(fact))

print()

#Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión 
#comineza con los números 0 y 1 y, a partir de éstos cada elemento es la suma de los dos números anteriores en la secuencia.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 .....


print("Serie de Fibonacci")
n1=0
n2=1
print(n1)
print(n2)

for i in range(8):
    f= n1+n2
    print(f)
    n1=n2
    n2=f


#Escribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos. 
# Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos.
#No olvides que no es posible dividir por cero, por lo que es necesario evitar que el programa arroje un 
# error sino se ingresaron números positivos


cont=0
promedio=0
suma=0
for i in range(6):
    n= int (input (" Ingrese 6 números enteros entre positivos y negativos # " ))

    if n==0:
        input("Número invalido, ingrese otro número")
    
    else:
        if n>0:
            cont=cont+1
            promedio=(promedio+n)/cont
        else:
            suma=suma+n

if cont !=0:

    print( "El promedio de los números enteros positivos es: " + str(promedio) )
else:
    print("No se ingresaron números positivos: ")


print("La sumatria de los números negatvos es: " + str(suma) )



#Otros ejercicios
#https://www.youtube.com/watch?v=wv1VFXgZbV0
