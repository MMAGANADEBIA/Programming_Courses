#Recordar que los diccionarios son parecidos a los objetos en js
#definidos por el nombre de la variable seguido de un "=" y entre corchetes
#el contenido distribuido por value key pairs por linea separados por comas (,)

product = {
    "name": "book",
    "quantity": 3,
    "price": 4.99
}

person = {
    "first_name": "Ryan",
    "last_name": "ray"
}

print(type(product)) #tipo
print(type(person))
print(product) #impresion
print(person)

print(dir(product)) #ver metodos

print(person.keys()) #imprime solo los vales de las llaves
print(person.items())

#del person#elimina  el diccionario
person.clear() #limpia el diccionario
print(person)#comprobacion

#Una lista puede estar compuesta de diccionarios
products = [
    {"name": "book", "price": 10.99}, #estoy escribiendo el diccionario en una sola linea
    {"name": "laptop", "price": 1000}
]

print(products)
