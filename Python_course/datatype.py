#para ver el tipo de dato se usa type() y print lo imprime()
print(type("Hello World!"))
#los strings se pueden declarar con comillas simples y triples comillas

#la concatenacion funciona igual que en javascript
print("Bye " + "World")

#Los numeros son muy importantes
print(30)
print(type(30)) #los numeros enterenos son int
print(30.5)
print(type(30.5)) #los numeros con decimal son float

#booleanos o logico
False
True

#tipo de dato list
[10, 20, 30, 55] #se declaran con corchetes
["hello", "Bye", "Adios"]#tambien se pueden usar con strings
[10, "Hello", True, 10.5]#Pueden ser usados tambien en conjunto con los otros datos
[]#se pueden declarar vacias
#en escencia son arrays (vectores)

#las tuplas son datos que no cambian
(10, 20, 30, 55) #son inmutables y se declaran como listas pero con parentesis
#se pueden declarar vacias

#Diccionarios
print(type({
    "name": "Ryan",
    "lastname": "Ray",
    "nickname": "Fazt"
}))
#Se declaran dentro de llaves como si fuera un objeto
#sirve para agrupar distintos tipos de datos con un nombre clave
#al igual que los objetos json son key-value

#si declaras algo con None se declara sin un tipo de dato aun
None
