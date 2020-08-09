#Las condicionales nos ayudan a mantener un control y un flujo dentro de nuestro programanar

x = 20

#if es un nombre reservado que sirve para comparar dos elementos
#y correr un codigo dependiendo del resultado
#dentro del estas comparaciones, las mas usada son menor que <, mayor que >
# o comparar si son iguales con == 
#para comparar si son iguales se usa el doble igual(==)y el igual sencillo(=) se usa para asignar datos
#Ejemplos
#if x < 30:
#    print("x is less than 30")

#if x > 10:
#    print("x is greater than 10")

#if x == 20:
#    print("x is equal than 20")
#en python no se necesitan corchetes para marcar el bloque de codigo, solo dospuntos(:) y un tabulador para marcar el codigo a correr(o espacios)
#tampoco necesita los parentesis para enjaular la evaluacion como en js

#para evaluar dos opciones usamos else

if x < 20: #evalua si x es menor que 20
    print("x less than 20") #si es así, corre esto
else: #si no es asi
    print("x greater than 20") #corre esto


color = "red"
if color == "blue":
    print("The color is blue")
else:
    print("any color")

if color == "blue":
    print("the color is blue")
elif color == "red":            #elif funciona como un else if de js
    print("the color is red")
else:
    print("any color")

#el elif al usarse despues del if es como un: if(si...) elif(pero si...)
#para evaluar una segunda opcion en caso de que la primera no se cumpla
#tener en cuenta que se pueden anidar

name = "John"
lastname = "Carter"

if name == "John":
    if lastname == "Carter":
        print("You are John Carter")
    else:
        print("You are not John Carter")
else:
    print("You are not John")


if x > 2 and x <= 10: #a diferencia de js, aqui se sustituye el && por "and"
    print("x is greater than 2 and less or equal than 10")
elif x > 2 or x <= 20 :
    print("x is greater than 2 or less or equal than 20")
y = 20
if not(x == y): #si x es diferente de y. es una forma de verlo
    print("x is not equal y")
else:
    print("x is equal y")


#exiten otros operadores logicos como or y not
#not permite dar un resultado contrario al que valida
