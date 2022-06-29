

#Entradas en una sóla linea separados por espacio
entrada=(input ("") )



#split= organiza la cadena de entrada en posiciones
entrada=entrada.split()

salariobase= float(entrada[0])
CantidadHorasExtras= int(entrada[1])
Bonificaciones1= int(entrada[2])

ValorHora=salariobase/192
HorasExtras=0
Bonificaciones=0

if CantidadHorasExtras>0:
    HorasExtras = ( ValorHora + ( ValorHora*0.25 ) ) * ( CantidadHorasExtras )

if Bonificaciones1==1:
    Bonificaciones=  ( salariobase*0.05 ) 


salarioTotalAD= salariobase + HorasExtras + Bonificaciones  #salarioTotalAD = Salario total antes de descuento

valor_Pagar_Empleado= salarioTotalAD - ( salarioTotalAD *0.035) - ( salarioTotalAD *0.04 ) - ( salarioTotalAD *0.01)

print( str(round(valor_Pagar_Empleado,1)))