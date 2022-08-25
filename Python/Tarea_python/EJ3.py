from time import time
from datetime import *
from dateutil.relativedelta import relativedelta
dia = int(input("Dígame su dia: "))
mes = int(input("Dígame su mes: "))
año = int(input("Dígame su año: "))
fecha_deseada = datetime(año, mes, dia)


edad = relativedelta(datetime(2022, 8, 31), fecha_deseada)
print(f"{edad.years} años, {edad.months} meses y {edad.days} días")
