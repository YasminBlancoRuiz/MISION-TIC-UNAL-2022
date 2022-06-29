
numcliente= float(input('Ingrese el número del cliente: '))
Totalfactura=float(input('Ingrese el valor total de la factura: '))
pago=int(input('Ingrese día de pago: '))


if pago<=10:
  Descuento1=200
  Descuento2=Totalfactura*0.2
  if Descuento2>Descuento1:
      ValorApagar=Totalfactura-Descuento2
  else: 
    ValorApagar=Totalfactura-Descuento1
print("Si el cliente paga dentro de los 10 días, tiene un descuento de, valor a pagar es:"+ str(ValorApagar) +" ")
if pago>10 and pago<=20:                    
  Totalfactura
print("Cliente no aplica con descuento, superó los 10 días, el valor a pagar es: "+ str(Totalfactura) + " ")
if pago>20:
  Multa=350
  DescuentoMulta=Totalfactura*0.10
  if Multa>DescuentoMulta or DescuentoMulta<Multa :
    ValorM=Totalfactura+Multa
  else:
    ValorM=Totalfactura+DescuentoMulta
    print("Cliente supera los 20 días de pago, debe pagar multa: "+ str(ValorM)+ " ")