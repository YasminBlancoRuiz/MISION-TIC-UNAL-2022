#RETO #1
#Hackathon Lplay Innovation

#La Universidad Nacional de Colombia realizará como parte de su festival Linux la hackathon LPlay Innovation, enfocada 
#en el desarrollo de video juegos en dicha plataforma. En vista del gran interés de las comunidades de desarrolladores, 
#se ha decidido practicar pruebas de clasificación que permitan presentar a los interesados retos acordes a sus conocimientos y capacidades.

#Las pruebas de clasificación tienen una puntuación máxima de 70, y el resultado que se obtenga permitirá clasificar a los interesados en los siguientes niveles:

#- Participantes que obtengan 20 puntos o menos estarán al nivel 'Básico'.

#- Participantes con puntajes entre 21 y 30 estarán en el nivel 'Intermedio'.

#- Participantes con puntajes entre 31 y 50 corresponden al nivel 'Avanzado'.

#- Participantes con más de 50 puntos corresponden al nivel 'Experto'.


#Los hermanos Hugo, Paco y Luis, apasionados por el sistema operativo Linux, la programación y los video juegos, se estuvieron preparado para 
#las pruebas de clasificación; no obstante las habilidades de cada uno de ellos son bien diferentes y los puntajes obtenidos se relacionan de la siguiente manera:

#Al quitarle cuatro (4) puntos al puntaje de Luis, se obtiene dos (2) veces el puntaje de Paco, y al sumar los puntajes de Luis y de Paco, 
#da como resultado cinco (5) veces el puntaje Hugo (los puntajes se contabilizan utilizando números enteros).



#Objetivo: Escribir un programa en el lenguaje de programación Python, el cual a partir de del puntaje obtenido por Paco (ingresado por el usuario),
#imprime en la consola de ejecución los puntajes de Hugo, Paco y Luis, separados por un solo espacio (' '). En una segunda línea, se debe indicar a que 
#qué nivel corresponde Luis a partir de su puntaje ('Básico', 'Intermedio', 'Avanzado', o 'Experto').


#Variables PP = Puntaje Paco //  PH= Puntaje Hugo //  PL= Puntaje Luis 

PP= (int(input("Ingrese por favor el puntaje de Paco: ")))

PL=int(2*PP)+4
PH=int((PL+PP)/5)

if PP >70 or PL>70 or PH>70:
  print("Supera la puntuación máxima")
else:
  print(str(PH) + " " +str(PP) + " " + str(PL) )
  if PL<=20:
    print("Básico")
  if PL>=21 and PL<=30:
    print("Intermedio")
  if PL>=31 and PL<=50:
    print("Avanzado")
  if PL >50:
    print("Experto")