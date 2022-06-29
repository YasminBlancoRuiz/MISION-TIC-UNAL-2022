
'''''''''''''''''''''''''''''''''''''''
Reto 3: Grupo P13
 Número máximo de ficheros: 1
Tipo de trabajo:  Individual
El Juego del Ahorcado

"El Ahorcado" o simplemente "Ahorcado" es un popular juego de adivinanza (https://es.wikipedia.org/wiki/Ahorcado_(juego) que nos es familiar a la mayoría.

Este juego consiste en adivinar frases (secuencias de palabras separadas por espacio) o palabras, con un sentido contextual (título de películas, refranes, obras de literatura, piezas musicales, etc) a partir de las letras que las componen y de ayudas visuales que van indicando su ubicación dentro de las frases.

P R ? G R ? M ? C ? ? N ? N P ? T H ? N

Objetivo:

Escribir un programa en Python que reciba en una primera entrada la frase a adivinar y una segunda entrada correspondiente a las letras (separadas por coma ',') que utiliza un contrincante a la hora de adivinar (sus intentos).  Veámos:

1) Frase a Adivinar: Programación en Python

2) Intentos: p,o,Y,I,h,G,N,r,M,C,é,U,t,A

Por simplicidad, tanto la frase como los intentos serán convertidos a mayúsculas y si aparecen caracteres con tilde, serán reemplazados por sus versiones sin tilde. Es decir que las dos anteriores entradas serán tratadas como si hubieran sido escritas así:

1) PROGRAMACION EN PYTHON

2) P,O,Y,I,H,G,N,R,M,C,E,U,T,A

En cada intento, el programa debe imprimir la salida "[1] - [2] - [3]" en donde:

1. La letra del intento

2. Como se vé la frase con sus incógnitas (las incógnitas deben ser reemplazadas por el signo de interrogación '?') y las letras que ya se conocen legibles.

3. El listado de letras que constituyen los intentos fallidos.

Siguiendo con el ejemplo:

[P] - [P??????????? ?? P?????] - []
[O] - [P?O???????O? ?? P???O?] - []
[Y] - [P?O???????O? ?? PY??O?] - []
[I] - [P?O??????IO? ?? PY??O?] - []
[H] - [P?O??????IO? ?? PY?HO?] - []
[G] - [P?OG?????IO? ?? PY?HO?] - []
[N] - [P?OG?????ION ?N PY?HON] - []
[R] - [PROGR????ION ?N PY?HON] - []
[M] - [PROGR?M??ION ?N PY?HON] - []
[C] - [PROGR?M?CION ?N PY?HON] - []
[E] - [PROGR?M?CION EN PY?HON] - []
[U] - [PROGR?M?CION EN PY?HON] - [U]
[T] - [PROGR?M?CION EN PYTHON] - [U]
[A] - [PROGRAMACION EN PYTHON] – [U]

En el transcurrir del juego se pueden dar dos situaciones:

1. El Contrincante Pierde: Se debe tener en cuanta que cada vez que el contrincante indica letras que no hacen parte de la frase, se consideran intentos fallidos, que se van contabilizando; si ese número de intentos fallidos llega a la mitad (división entera) de la longitud de toda la frase, sin haber adivinado, el contrincante habrá perdido. En este caso se deberá imprimir adicionalmente la siguiente frase "{AHORCADO DESPUÉS DE [N] INTENTOS}", en donde N corresponde a los intentos que se tuvieron:

{AHORCADO DESPUÉS DE [12] INTENTOS}

2. El Contrincante Gana: Si el contrincante completa las letras de la frase sin exceder los intentos fallidos permitidos, habrá ganado y en este caso se deberá imprimir adicionalmente la siguiente frase "{FELICITACIONES, GANA DESPUÉS DE [N] INTENTOS}", en donde N corresponde a los intentos que se tuvieron:

{FELICITACIONES, GANA DESPUÉS DE [14] INTENTOS}

Ejemplos de la Ejecución

Ejemplo 1
Entradas	Salidas
Tiempos Violentos
p,L,a,S,h,U,T,v,M,o,I,e,n
[P] - [????P?? ?????????] - []
[L] - [????P?? ???L?????] - []
[A] - [????P?? ???L?????] - [A]
[S] - [????P?S ???L????S] - [A]
[H] - [????P?S ???L????S] - [AH]
[U] - [????P?S ???L????S] - [AHU]
[T] - [T???P?S ???L??T?S] - [AHU]
[V] - [T???P?S V??L??T?S] - [AHU]
[M] - [T??MP?S V??L??T?S] - [AHU]
[O] - [T??MPOS V?OL??TOS] - [AHU]
[I] - [TI?MPOS VIOL??TOS] - [AHU]
[E] - [TIEMPOS VIOLE?TOS] - [AHU]
[N] - [TIEMPOS VIOLENTOS] - [AHU]
{FELICITACIONES, GANA DESPUÉS DE [13] INTENTOS}

Ejemplo 2
Entradas	Salidas
El Padrino
v,g,s,B,C
[V] - [?? ???????] - [V]
[G] - [?? ???????] - [VG]
[S] - [?? ???????] - [VGS]
[B] - [?? ???????] - [VGSB]
[C] - [?? ???????] - [VGSBC]
{AHORCADO DESPUÉS DE [5] INTENTOS}

Ejemplo 3
Entradas	Salidas
El Caballero de la Noche
t,s,l,h,i,d,ñ,E,u,R,M,p,a,F,V,C,b,N,o,G
[T] - [?? ????????? ?? ?? ?????] - [T]
[S] - [?? ????????? ?? ?? ?????] - [TS]
[L] - [?L ????LL??? ?? L? ?????] - [TS]
[H] - [?L ????LL??? ?? L? ???H?] - [TS]
[I] - [?L ????LL??? ?? L? ???H?] - [TSI]
[D] - [?L ????LL??? D? L? ???H?] - [TSI]
[Ñ] - [?L ????LL??? D? L? ???H?] - [TSIÑ]
[E] - [EL ????LLE?? DE L? ???HE] - [TSIÑ]
[U] - [EL ????LLE?? DE L? ???HE] - [TSIÑU]
[R] - [EL ????LLER? DE L? ???HE] - [TSIÑU]
[M] - [EL ????LLER? DE L? ???HE] - [TSIÑUM]
[P] - [EL ????LLER? DE L? ???HE] - [TSIÑUMP]
[A] - [EL ?A?ALLER? DE LA ???HE] - [TSIÑUMP]
[F] - [EL ?A?ALLER? DE LA ???HE] - [TSIÑUMPF]
[V] - [EL ?A?ALLER? DE LA ???HE] - [TSIÑUMPFV]
[C] - [EL CA?ALLER? DE LA ??CHE] - [TSIÑUMPFV]
[B] - [EL CABALLER? DE LA ??CHE] - [TSIÑUMPFV]
[N] - [EL CABALLER? DE LA N?CHE] - [TSIÑUMPFV]
[O] - [EL CABALLERO DE LA NOCHE] - [TSIÑUMPFV]
[G] - [EL CABALLERO DE LA NOCHE] - [TSIÑUMPFVG]
{FELICITACIONES, GANA DESPUÉS DE [20] INTENTOS}

Ejemplo 4
Entradas	Salidas
El Gladiador
t,H,O,i,E,L,r,U,D,G,Á
[T] - [?? ?????????] - [T]
[H] - [?? ?????????] - [TH]
[O] - [?? ???????O?] - [TH]
[I] - [?? ????I??O?] - [TH]
[E] - [E? ????I??O?] - [TH]
[L] - [EL ?L??I??O?] - [TH]
[R] - [EL ?L??I??OR] - [TH]
[U] - [EL ?L??I??OR] - [THU]
[D] - [EL ?L?DI?DOR] - [THU]
[G] - [EL GL?DI?DOR] - [THU]
[A] - [EL GLADIADOR] - [THU]
{FELICITACIONES, GANA DESPUÉS DE [11] INTENTOS}

Ejemplo 5
Entradas	Salidas
La Vida es Bella
n,Ú,F,í,H,G,m,C,t
[N] - [?? ???? ?? ?????] - [N]
[U] - [?? ???? ?? ?????] - [NU]
[F] - [?? ???? ?? ?????] - [NUF]
[I] - [?? ?I?? ?? ?????] - [NUF]
[H] - [?? ?I?? ?? ?????] - [NUFH]
[G] - [?? ?I?? ?? ?????] - [NUFHG]
[M] - [?? ?I?? ?? ?????] - [NUFHGM]
[C] - [?? ?I?? ?? ?????] - [NUFHGMC]
[T] - [?? ?I?? ?? ?????] - [NUFHGMCT]
{AHORCADO DESPUÉS DE [9] INTENTOS}

'''''''''''''''''''''''''''''''''''''''''''''''''''


from calendar import c
from re import L
from sre_constants import RANGE_UNI_IGNORE
import unicodedata
import sys
import math


fraseAdivina=""
letras=""

#####Convertir a mayúsculas y quitando tildes

fraseAdivinar= input("Ingrese frase a adivinar:")
letras1= input("Ingrese las letras (separadas por coma ',':")


def validarMayus_Tildes(palabras):


   palabras=palabras.replace("á","a").replace("Á","A")
   palabras=palabras.replace("é","e").replace("Ë","E")
   palabras=(palabras.replace("í","i").replace("Í","I"))
   palabras=(palabras.replace("ó","o").replace("Ó","O"))
   palabras=(palabras.replace("ú","u").replace("Ú","U"))

   palabras=palabras.upper()

   return palabras

R1=[]
R2=[]
R1=validarMayus_Tildes(fraseAdivinar)
R2=validarMayus_Tildes(letras1)

print("".join(R1))
print("".join(R2))

##### El nuevo vector contertirlo en "?" 
# P R ? G R ? M ? C ? ? N ? N P ? T H ? N
#El join convierte la lista a un string // Podríamos usar el método str.join() para 
# convertir una lista que tiene elementos de tipo datos str a una cadena.

R3=[]

for r in "".join(R1):
   if r!= " ":
      R3.append("?")   
   else:
      R3.append(" ")    

#print("[" + "".join(R3) + "]" )



#verificando las letras iguales ingresadas

temp=0

R4=[]
for c2 in range(0,len(letras1),2):
   temp=0  
   for c1 in range(len(fraseAdivinar)):
      if ("".join(R2)[c2]) == ("".join(R1)[c1]):
         R3[c1]=("".join(R1)[c1])
         temp=1
   
   if temp==0:
      R4.append("".join(R2)[c2])
   
   
   print("["+ "".join(R2)[c2] +"]" + " - " + "[" +"".join(R3) +"]"   + " - "+ "[" + "".join(R4) + "]")

   

#divisionfraseR1=int((len(fraseAdivinar)/2))
#print(divisionfraseR1)


# math.ceil este metodo me ayuda a traer despues de la coma para redondear. 
# Esta función devuelve el valor máximo del número o el entero más pequeño mayor o igual que el número pasado como argumento.
#fraseAdivinar=fraseAdivinar.replace(" " , "")
letras1=letras1.replace("," , "")
intentos=(len(letras1))
fraseDivididos=int((len(fraseAdivinar))/2) 

if (len(R4)>=fraseDivididos):
   print("{AHORCADO DESPUÉS DE [" + str(intentos) + "] INTENTOS}")
   
else:
   print("{FELICITACIONES, GANA DESPUÉS DE [" + str(intentos) + "] INTENTOS}")




