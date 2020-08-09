#Set es una coleccion de datos desordenada y sin indices
colors = {'Red', 'Green', 'Blue'}
print(type(colors))
print(colors)

print('Red' in colors) #no tiene indice, pero se puedem buscar elementos

colors.add('Violet') #con add nos agrega un elemento nuevo en una posicion aleatoria
print(colors)

colors.remove('Red') #al igual que listas, se pueden eliminar con remove un elemento dado
print(colors)

colors.clear() #clear() limpia los elementos
print(colors) #nos regresa set() limpio

del colors#al igual que las tuplas se puede eliminar con del
#print(colors) #comprobar
