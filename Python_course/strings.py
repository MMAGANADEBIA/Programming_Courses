myStr = "Hello World!"
#en python se pueden hacer operaciones directas con strings
#print(dir(myStr)) #dir nos ayuda a saber las propiedades y metodos

print(myStr.upper()) #para usar propiedades y metodos se usa la variable y lel metodo
#imprimimos la variable de myStr con el metodo upper que escribe en mayusculas
print(myStr.lower()) #minisculas
print(myStr.swapcase()) #primear minusculas y las siguientes mayusculas
print(myStr.capitalize()) #primera mayuscula y siguientes minisculas

print(myStr.replace("Hello", "Bye")) #Para remplazar se usa remplace y dentro de las comillas el texto a remplazar, coma y el texto por el que se remplaza
print(myStr.replace("Bye", "hello").upper()) #podemos usar mas metodos agregandolos con notacion de punto

print(myStr.count("l")) #count se usa para contar cuantas veces se un caracter

print(myStr.startswith("H")) #metodo para ver si la cadena inicia con una palabra o caracteres

print(myStr.endswith("D")) #Para para saber si termina con una palabra o algunos caracteres
# Para verificar los ultimos dos metodos nos regresa true o false

print(myStr.split('o')) #si entre los parentesis ponemos algun caracter, separa por ese caracter

print(myStr.find('o')) #busca el indice de el caracter que le ingrese entre parentesis

print(len(myStr)) #mide la longitud de la cadena

print(myStr.index('e')) #nos encuentra el indice del caracter a encontrar

#print(myStr.isnumeric()) #verifica si la variable es numerica por alguna razon no funciona jaja :(
print(myStr.isalpha()) #verifica si la variable es alfanumerica

print(myStr[4]) #si escribimos directamente entre corchetes un indice nos manda el caracter de ese indice
print(myStr[-2]) #con un numero en negativo nos devuelve el indice pero en orden inverso

print("Oh, " + myStr) #concatena cadenas y variables
#print(f "Oh, {myStr}") #con f deberia de imprimir la variable pero no funciona

print("Oh, {0}".format(myStr)) #de esta forma puedes concatenar variables y cadenas tambien, en los corchetes es indice o solo 0 y .format con la variable que quieres que imprima
