#En las tuplas no se pueden reasignar datos (Son inmutables) y son mas rapidas que las listas
x = (1, 2, 3, 4, 5) #para definir tuplas se hace entre parentesis
print(x)
print(type(x)) #recuerda que es para ver el tipo de dato
print(x[4]) #imprime el indice dado
del x #del elimina la tupla dada
#print(x) #comprobamos

y = tuple((1, 2, 3)) #se pueden definir igual que las listas con el constructur y dentro escribes la tupla entre parentesis
print(y)

print(dir(x)) #ver los metodos de las tuplas

c = (1)
print(c)
print(type(c))  #nos imprime que es un entero porque solo tenemos un dato
#una tupla debe contener mas de un elemento, si solo tiene uno lo topa como entero
c2 = (1,) #para que nos imprima como tupla podemos poner una "," para definirlo como tal (como un conjunto de elementos)
print(c2)
print(type(c2))

#podemos tambien tener tuplas dentro de diccionarios
locations = {
    (32.12343, 39.000): "Tokyo",
    (35.345453, 30.089): "New York"
}
