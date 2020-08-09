#los loops nos permiten recorrer toda una lista automaticamente con nuestros parametros

foods = ['Aplles', 'Bread', 'Cheese', 'Milk', 'Bananas']
 
#ciclo for
for food in foods:#declaracion de variable temporal contenedora
    if food == "Cheese":
        print("Yo have to buy this:")
        #break #break rompe la ejecucion
        continue #continue continua la ejecucion
    #break y continue no se llevan bien
    print(food) #de los elementos de la lista

for number in range(1, 8):
    print(number); #iteracion de numeros

for letter in "Hello":
    print(letter) #iteracion de caracteres

count = 4

while count <= 10: #mientras count sea menor o igual a 10 entonces:
    print(count)
    count = count + 1 #se suma una valor para que llegue a 10 y no se 
                      #ejecute eternamente
