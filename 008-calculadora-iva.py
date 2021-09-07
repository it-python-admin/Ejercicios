i1 = input("Introduce el importe 1:")
i2 = float(input("Introduce el importe 2:"))
impuesto = float(input("Introduce el porcentaje de IVA:"))/100
i1 = float(i1)
print("IMPORTE FACTURA=",i1+i2+(i1+i2)*impuesto)