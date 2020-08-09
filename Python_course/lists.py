demo_list = [1, "hello", 1.34, True, [1, 2, 3]] #las listas pueden albergar cualqquier dato o tipo de dato
colors = ["red", "green", "blue"]

#tambien se puede usar el constructor
number_list = list((1, 2, 3, 4)) # se crea una variable igual a constructor list y entre parentesis los objetos
print(number_list) 
print(type(number_list))

r = list(range(1, 101))#rangos de donde a donde para crear determinado elemento
print(r)

print(type(colors))
print(dir(colors)) #dir nos permite ver los metodos del elemento
print(len(colors)) #recuerda que len ve el tamaño de un objeto o en este caso lista
print(colors[1]) #para buscar el indice
print(colors[-2]) #para buscar indice al reves

print('green' in colors) #esta funcion es para imprimir true o false si el string que meti existe in variable

print('verde' in colors)

print(colors) #imprime la lista

colors[1] = 'yellow' #sustituye el indice 1 de la lista colors por yellow
print(colors)

colors.append('violet') #agrega nuevos elementos a la lista
print(colors)

#colors.append(('green', 'black')) #append solo agrega uno, puedo agregar mas con una tupla
#print(colors) 
#Comentado por efectos practicos

colors.extend(['blue', 'dirt']) #para agregarlos como elementos separados se usa extend y se manda una lista
print(colors)

colors.insert(1, 'pink') #agrega un elemento en un indice dado
print(colors)

colors.insert(len(colors), 'second_pink') #inserta en el indice igual al tamaño de la lista, en este caso al final
print(colors)

colors.pop() #elimina el ultimo elemento
print(colors)

colors.remove('pink') #elimina el elemento dado 
print(colors)

#colors.clear() #limpia completamente la lista colors
#comentado por efectos practicos
colors.sort() #sort al igual que en javascript ordena alfabeticamente los elementos de una lista
print(colors)

colors.sort(reverse=True) #para ordenar de manera inversa se debe de escribir dentro de los parentesis del metodo "reverse" que es lo que se busca y =True para decirle que queremos "activarlo"
print(colors)

print(colors.index('red')) #.index sirve para encontrar cual es el indice del elemento dado de una lista

print(colors.count('blue')) #recordar que nos ayuda a contar cuantas veces se repite un elemento en una lista
