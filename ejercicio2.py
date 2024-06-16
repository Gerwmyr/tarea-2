factura=int(input("ingrese el total de la factura \n"))

if factura > 10000:
    comision=factura*0.05
    print("su comision es de: ", comision)
else:
    print("no se le cobra comision")