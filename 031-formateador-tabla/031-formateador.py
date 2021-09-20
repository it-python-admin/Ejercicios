ventas = {"Lunes":(2083,38) , "Martes":(10,183) ,"Miércoles":(-283,19) , "Jueves":(2023,11) ,"Viernes":(10,18)}
linea1 = "Ventas".center(50)
linea2 = ""
for k,v in ventas.items():
    linea2 = linea2+k.ljust(10)
print(linea1)
print(linea2)