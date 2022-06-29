''''''''''''''''
El juego de la Gulupa (Ligeramente Inspirado en “Guayabita”)

La Gulupa es un fruto de amplia siembra, comercialización y consumo en Colombia en virtud de sus 
grandes propiedades nutricionales y medicinales, y de sus bondades comerciales 
(https://es.wikipedia.org/wiki/Passiflora_pinnatistipula).

Los agricultores de la región, en su honor, y para pasar ratos amenos de libre esparcimiento, han 
inventado un juego llamado “El Juego de la Gulupa”, “Gulupita”, como cariñosamente lo llaman.

En “El Juego de la Gulupa” se utiliza un dado de seis caras (https://es.wikipedia.org/wiki/Dado), 
se juega por rondas y participan dos competidores y la “Casa”.

En cada ronda hay una apuesta inicial base que es la misma para los dos competidores 
(solo los competidores aportan esta apuesta inicial, es decir la “Casa” no apuesta), 
y que constituye el premio otorgado a quien gane la ronda.

Después de que los competidores hayan aportado la apuesta inicial, la “Casa” lanza el dado, 
obteniendo un valor base (entre 1 y 6).  Posteriormente, los competidores lanzan el dado 
obteniendo cada uno su valor de apuesta.  El competidor que saque el mayor valor de apuesta 
que sea superior al valor base es el ganador de dicha ronda.

La “Casa” es una entidad que va acumulando los premios de las rondas en las que no hay ganadores 
( Es decir cuando no hay un competidor  ganador, la “Casa” gana).  Dichos casos son:

Caso 1: Cuando el valor base                                                    

Caso 2: Cuando ninguno de los competidores superen con su valor de apuesta el valor base obtenido 
por la “Casa”

Caso 3: Cuando los dos competidores sacan el mismo valor de apuesta que supera el valor base 
obtenido por la “Casa”.

Adicionalmente, existen una serie de eventos especiales:

Evento 1: Cuando ambos competidores sacan como valor de apuesta el número 6, se hace una Amnistía, 
y todo lo que ha ganado la “Casa” se distribuye entre los competidores en partes iguales.

Evento 2: Cuando ambos competidores sacan como valor de apuesta el número 1, y el valor base es 
diferente de 1 y de 6 (ver Caso 1, Gana la “Casa”), se genera una Penalización, reflejada en tener 
que duplicar el valor base de la apuesta, que es entregado inmediatamente a la “Casa”.

Rondas de Ejemplo
Ronda	Valor base
("Casa")	Valor de apuesta
(Competidor 1)
Valor de apuesta
(Competidor 2)	Resultado
1	⚂	⚃	⚄	Gana Competidor 2
2	⚃	⚄	⚂	Gana Competidor 1
3	⚄	⚄	⚃	Gana la Casa
4	⚂	⚄	⚄	Gana la Casa
5	⚅	-	-	Gana la Casa
6	⚁	⚅	⚅	Amnistía
7	⚃	⚀	⚀	Penalización
Objetivo:  

Escribir un programa en el lenguaje de programación Python, que escenifique 10 rondas de 
“El Juego de la Gulupa”, simulando los lanzamientos de la “Casa”, el “Competidor 1” y el 
“Competidor 2” con secuencias de caracteres en el cual cada carácter es el símbolo correspondiente 
a un lanzamiento de un dado.

(Puede ser de utilidad)

La siguiente tabla presenta los valores decimales asociados a los códigos Unicode 
(https://en.wikipedia.org/wiki/List_of_Unicode_characters) que representan los lanzamientos 
de los dados: 



Caracteres Unicode
Valor Decimal	Caracter Unicode
9856	⚀
9857	⚁
9858	⚂
9859	⚃
9860	⚄
9861	⚅
El programa debe presentar una secuencia de caracteres en la que cada caracter representa el 
resultado de la ronda correspondiente, usando las siguientes convenciones:

Convenciones
Signficado	Caracter Unicode a Utilizar	Valor Decimal
Gana Competidor 1	👸	128120
Gana Competidor 2	🤴	129332
Gana la Casa	🏰	127984
Amnistía	🤑	129297
Penalización	🤕	129301
A continuación se presentan algunos ejemplos de las salidas esperadas (10 evaluaciones) 
del programa construido a partir de las tres entradas (10 rondas de "Casa", 10 rondas de 
Competidor 1 y 10 rondas de Competididor 2):

Ejemplo 1
Entradas	Salida
⚃⚅⚂⚄⚅⚀⚁⚃⚁⚃
⚃⚁⚀⚄⚁⚁⚂⚀⚂⚅
⚄⚂⚀⚂⚃⚅⚀⚄⚁⚃	🤴🏰🤕🏰🏰🤴👸🤴👸👸
Ejemplo 2
Entradas	Salida
⚂⚅⚀⚅⚅⚀⚃⚁⚂⚃
⚃⚀⚂⚂⚃⚁⚄⚅⚀⚀
⚄⚅⚄⚀⚀⚀⚅⚁⚁⚃	🤴🏰🤴🏰🏰👸🤴👸🏰🏰
Ejemplo 3
Entradas	Salida
⚃⚃⚅⚃⚃⚀⚀⚀⚁⚅
⚀⚅⚅⚀⚄⚄⚀⚁⚀⚂
⚃⚅⚁⚀⚁⚃⚃⚁⚃⚁	🏰🤑🏰🤕👸👸🤴🏰🤴🏰

Ejemplo 4
Entradas	Salida
⚀⚁⚁⚁⚄⚁⚀⚁⚂⚁
⚂⚃⚃⚁⚄⚁⚃⚀⚅⚀
⚀⚅⚅⚅⚁⚂⚃⚀⚅⚂	👸🤴🤴🤴🏰🤴🏰🤕🤑🤴

Ejemplo 5
Entradas	Salida
⚁⚀⚄⚃⚂⚃⚃⚁⚃⚄
⚅⚁⚅⚀⚄⚄⚄⚅⚄⚄
⚀⚄⚁⚄⚅⚄⚃⚁⚀⚄	👸🤴👸🤴🤴🏰👸👸👸🏰
'''''''''



def comparaciones(casa, Compet1, Compet2):  
  resultado = ""
  for i in range(10):       
    if casa[i]!="⚅":
      if Compet1[i] == "⚀" and Compet2[i] == "⚀" and casa[i] != "⚀" and casa[i] != "⚅":
        resultado +='🤕'
      elif ((Compet1[i] == Compet2[i]) and (Compet1[i] > casa[i]) and (Compet1[i] != "⚅") ) or (Compet1[i] <= casa[i] and Compet2[i] <= casa[i]):
        resultado +='🏰'
      elif Compet1[i] == "⚅" and Compet2[i] == "⚅":
        resultado +='🤑'
      elif casa[i] <Compet2[i] and Compet1[i] < Compet2[i]:
        resultado +='🤴'
      elif casa[i] < Compet1[i] and Compet1[i] > Compet2[i]:
        resultado +='👸'
    else:
      resultado += "🏰"      
  return   resultado

casa=input("Ingrese rondas de la casa: ")
Compet1=input("Ingrese las rondas del competidor N°1: ")
Compet2=input("Ingrese las rondas del competidor N°2: ")

print(comparaciones (casa, Compet1, Compet2))

