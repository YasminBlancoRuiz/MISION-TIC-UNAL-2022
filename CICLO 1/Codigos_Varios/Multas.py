

#ebido a la alta accidentalidad presentada en el último año en las carreteras del territorio nacional, 
#el Gobierno Colombiano ha decidido implementar controles que permitan sancionara a los 
#conductores que no respeten los límites de velocidad establecidos por los organismos de control. 
#Con este fin, el Ministerio de Transporte ha decidido implementar radares de tramo en las carreteras 
#con mayores índices de accidentalidad en el país.
#Los radares de tramo funcionan colocando dos cámaras en dos puntos alejados de una carretera
#con el fin de comprobar cuánto tiempo tarda un conductor recorrer dicho tramo. Estos radares no 
#miden la velocidad de paso, sino el tiempo de paso representado como la velocidad media de un 
#conductor en un trayecto con una longitud determinada. 
#La interpretación del funcionamiento de los radares es simple: si colocamos las cámaras separadas 
#10 Km en un tramo cuya velocidad máxima es de 110 Km/h y un conductor tarda 5 minutos en ser 
#visto por la segunda cámara, sabremos que su velocidad media ha sido de 120 Km/h, y por tanto,
#en algún sitio ha superado la velocidad permitida.
#Usted hace parte del equipo de desarrollo encargado de construir el software que procesará los 
#datos registrados por las cámaras. Su misión es crear un programa en Python que permita saber si 
#un conductor debe ser multado o no.


#Entrada El programa recibirá 3 parámetros:
# La distancia en metros que separa dos cámaras
#La velocidad máxima permitida en ese tramo en (Km/h)
# El tiempo en segundos que tarda el conductor en recorrer el trayecto

#Salida El programa imprimirá una línea indicando si el conductor debe 
#ser multado o no. Se debe considerar lo siguiente:

# Imprimirá “OK” si el conductor no superó la velocidad máxima

# Imprimirá “MULTA” si se superó la velocidad máxima en 
#menos de un 20% de la velocidad permitida

# Imprimirá “CURSO SENSIBILIZACION” si la velocidad 
#fue superada en un 20% o más de la velocidad permitida. 
#En este caso además de la multa deberá realizar un curso 
#de sensibilización.

# Debido a que los sistemas pueden fallar y registrar valores 
#errados (por ejemplo, indicando que el tiempo que ha 
#tardado el conductor es negativo). En esos casos, se deberá 
#imprimir “ERROR”

#Entradas de ejemplo=     9165 110 300
                        # 9165 110 299
                        # 1000 -50 -100
                        # 12000 100 359



#Salidas de ejemplo=     OK
                        # MULTA
                        # ERROR
                        # CURSO SENSIBILIZACION



            

DistanciaMetros= int(input("Ingrese distancia en metro: "))
VelocidadMaxima=int(input("Ingrese velocidad máxima: "))
Tiempo=int(input("Ingrese tiempo en segundos: "))

VelocidadMedia=(DistanciaMetros/1000)/(Tiempo/3600)
print(VelocidadMedia)






if( DistanciaMetros<0 or VelocidadMaxima<0 or Tiempo<0):
    print("ERROR") 

else:

    if ( VelocidadMedia < VelocidadMaxima ):
        print("OK")
        

    else:
        porcentaje=0
        porcentaje= VelocidadMaxima+(VelocidadMaxima*0.2)
        if ( VelocidadMedia > porcentaje ):
            print(" CUSO DE SENSIBILIZACIÓN")
        else:
            print("MULTA")  


 



