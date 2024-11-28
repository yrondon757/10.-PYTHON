# Debemos importar el modulo "random"
import random

#.randint(1,10) Nos permite colocar un rango de numero "random"
numero_random = random.randint(1,11)
print(numero_random)

#.choice(lista) Nos permite seleccionar un elemento aleatorio de una lista
lista = ["Telefono","Computadora","Televisor"]
elemento_aleatorio = random.choice(lista)
print(elemento_aleatorio)

# .random() Genera un numero aleatorio del 0 al 1
# Si multiplicamos ese numero por 100, nos da un numero del 0 al 100
# Si envolvemos el codigo de un int() lo que hace es que nos devuelve un numero aleatorio entero

random_numero = int(random.random() * 100)
print(random_numero)

