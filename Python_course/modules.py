#Existen modulos escritos por nosotros mismos
#Existen modulos ya escritos que puedes encontrar por internet
#Existen modulos de python

#import datetime
from datetime import timedelta, date
#de esta segunda forma importamos solo ciertos metodos

print(date.today()) #siempre hay que leer la documentacion para
#entender los modulos
#sin los modulos especificos seria print(datetime.date.today())

print(timedelta(minutes=100))
#sin los modulos especificos seria print(datetime.timedelta(minutes=100))

import fmath #importas tus modulos con import y el nombre del archivo como cualquier otro modulo
#para importar solo algunas funciones de tu modulo lo haces con:
#from fmath import add, substract. from archivo import funciones

fmath.add(1, 2)
fmath.substract(3,2)

from colorama import Fore, Style
#si usas windows descomenta la linea de abajo para activar los colores
#init(convert=True)
print(Fore.RED + "Hello World")
