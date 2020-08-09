#def nos define que algo es una funcion
def hello(name="World"): #se define la variable que se va a usar
    print("Hello " + name)

hello("Mario") #obviamente las funciones no se ejecutan hasta que se llamen
#lo que metas aqui se agrega a la variable del parametro de la funcion
hello() #si no le paso parametros, en la funcion se puede definir uno por defecto de la misma forma en la que declaras una variable
def add(number_one, number_two):
    return number_one + number_two

print(add(10, 30))
print(add(100, 500))

print(len("Hello"))

#funciones anonimas o lambda que toman un numero de argumentos escritos con una sola expresion
add2 = lambda number_one, number_two: number_one + number_two
print(add2(10, 30))

