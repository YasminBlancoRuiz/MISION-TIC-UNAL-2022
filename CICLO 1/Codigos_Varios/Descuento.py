

#Una tienda tiene las siguientes promociones
#Si un cliente lleva m ́as de 5 productos del mismo tipo le realizan
#un descuento del 5%. Si lleva m ́as de 10 productos del mismo tipo
#le realizan un descuento del 10%. Si lleva m ́as de 20 productos
#del mismo tipo le realizan un descuento del 20%. Construya un
#programa que dado el n ́umero de productos y el precio de cada
#producto determine el valor a pagar por el cliente.

Cantidadproductos= int ( input ("Ingrese la cantidad de productos: ") )
precio= int( input ("Ingrese el precio del producto: " ) )

valorTotal=0
if ( Cantidadproductos > 5 and Cantidadproductos<=10):
    
    valorTotal= (precio * Cantidadproductos) 
    valorPagar= valorTotal - (valorTotal * 0.05)
elif ( Cantidadproductos > 10 and  Cantidadproductos<=20):
    valorTotal= (precio * Cantidadproductos) 
    valorPagar= valorTotal - (valorTotal * 0.10)
elif ( Cantidadproductos > 20 ):
    valorTotal= (precio * Cantidadproductos) 
    valorPagar= valorTotal - (valorTotal * 0.20)

else:
    valorPagar= (precio * Cantidadproductos)



print("El valor a pagar es: " + str(valorPagar) )  