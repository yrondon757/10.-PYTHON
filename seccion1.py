# Esto es un comentario en Python.

"""
Esto es un comentario
de varias lineas
de codigo.
"""

# -------------- VARIABLES
# ------> Sintaxis de variable, nombreVariable = valor
nombre = "Yenetson"
apellido = "Rondon"
edad = 33
calificacion = 17
pais = "Venezuela"
mayor_de_edad = True # Las iniciales de un booleano deben ser en mayusculas.

# ----------- Imprimir por pantalla/consola
print(nombre)
print(apellido)
print(edad, calificacion, pais)

# --------------> Tipos de Datos

# --- ENTERO (int)
x = 10

#--- FLOTANTE (float)
y = 10.5

#--- CADENA DE TEXTO (str) = string
msg = "Hola mundo desde Python"

# --- BOOLEANO (bool)
verdadero = True
falso = False

# --- LISTA (list)
miLista = [1,2,3,4,5,"Texto",10.5,True]
# Acceder
print(miLista[5])

# --- TUPLAS (tuple) Las tuplas son inmutables (No se pueden modificar, ni añadir elementos)

miTupla = (1,2,3,4,5,"Texto",10.5,True)
# Algo en cuenta que hay que tomar es lo siguiente:
miTupla2 = (10,) # Colocar coma si solomente tiene un elemento.
# Vamos a intentar modificar un elemento de la tupla (Saldra error porque son inmutables).
# miTupla[0] = 7
print(miTupla)
# Vamos a intentar añadir un elemento (Saldra error porque las tuplas son inmutables).
# miTupla.append(20)
print(miTupla)

# --- Diccionarios (dict)
# --> Sintaxis nombreVariable = {clave:valor, clave2:valor2, clave3:valor3, ...}

miDiccionario = {
    "nombre" : "Yenetson",
    "edad" : 33,
    "calificacion" : 17.5
}

# Acceder
print(miDiccionario["edad"])
# Reasignar
miDiccionario["nombre"] = "Jose"
print(miDiccionario["nombre"])
# Crear una nueva clave
miDiccionario["apellido"] = "Rondon"
print(miDiccionario)
# Tambien podemos eliminar una clave
del miDiccionario["calificacion"]
print(miDiccionario)

# --- None (NoneType)
nulo = None

# ----------------- Python es CASE SENSITIVE
# Se refiere al hecho de que un Lenguaje de programacion distingue entre mayusculas y minusculas.
miVariable = 100
mivariable = 99

a = True
A = False

print(A)

# -------------- Algunas diferencias con Javascript
# 1 No hay punto y coma.
# 2 No hay llaves.
# 3 No podemos concatenar o sumar variables de diferentes tipos de datos.
# 4 No hay incremento ni decremento (++) (--)
# 5 No hay operardor ternario explicito (?:)

# -------------- Operadores aritmeticos
# + ---> Suma
resultado = 10 + 3 # 13

# - ---> Resta
resultado2 = 10 - 3 # 7

# * ---> Multiplicacion
resultado3 = 10 * 3 # 30

# / ---> Division
resultado4 = 10 / 3 # 3.33333333333333

# % Modulo
resultado5 = 10 % 3 # 1

# // ---> Division entera
resultado6 = 10 // 3 # 3

# ** ---Z Exponente
resultado7 = 10 ** 3 # 1000

# ------------------- Operadores de asignacion

# = ---> Asignacion
m = 500

# += ---> Incremento
m += 150

# -= ---> Decremento
m -= 200

# *= ---> Multiplicacion
m *= 2

# /= ---> Division
m /= 2

# %= ---> Modulo
m %= 2

# //= ---> Division entera
m //= 2

# **= ---> Exponente
m **= 2
print(m)

# ------------------ Operadores comparativos

# == ---> Igual
print(20 == 20) # True
# != ---> Diferente
print (20 != 20) # False
# > ---> Mayor que
print(20 > 20) # False
# < ---> Menor que
print (20 < 20) # False
# >= ---> Mayor o igual que
print (20 >= 20) # True
# <= Menor o igual que
print (20 <= 20) # True

# --------------- Operadores Logicos
# && ---> and (y)
print(True and True) # True
# || ---> or (o)
print(True or False) # True
# ! ---> not (no)
print (not True) # false

# --------------- Input y Print
# --- Input (Entrada de datos)
msg2 = input("Ingresa tu nombre: ")

# --- Print (Imprimir por consola)
print(msg2)

# ---------------- Concatenacion y F-strings

# --- Concatenacion
print("Hola " + "buenas noches, " + msg2)
print("Hola", "buenas noches,", msg2)

# --- F-strings (Esto seria en javascript ---> `Hola ${msg2}`)
# Facilita la incorporacion de variables y expresiones dentro de cadenas de texto, se puede colocar la letra F
print(f"Hola {msg2}")
# \n ---> Nos permite hacer un salto de linea
print("Hola \n Esto es una prueba")


# ------------------- Condicionales (if, else, elif, ternario, match-case)
# En javascript if y else serian igual... Pero elif en python seria la otra condicion adicional por si if llegase a ser falso

if 5 > 4:
    print("5 es mayor que 4")
elif 7 > 8:
    print("7 es mayor que 8")
elif 8 > 7:
    print("8 es mayor que 7")
else:
    print("No se cumple ninguna condicion")
    
tiempo = True
dinero = True
ganas = False
if tiempo and dinero and ganas:
    print("Yujuuuuuu hoy se sale :D")
elif tiempo and dinero and not ganas:
    print("Hoy se sale pero no se disfruta")
elif tiempo and not dinero and ganas:
    print("Hoy me quedo en casa :C")
elif not tiempo and dinero or not ganas:
    print("Hay que trabajar :'C")
else:
    print("Hoy me quedare en casa porque no tengo nada :C")
    

# ------------ Operador Ternario
edad2 = 17
respuesta = "Es mayor de edad" if edad2 >= 18 else "Es menor de edad"
print(respuesta)

# ---- MATCH - CASE
match edad2: 
    case 18:
        print ("Tienes 18 años")
    case 19:
        print ("Tienes 19 años")
    case 20:
        print ("Tienes 20 años")
    case _:
        print("Edad desconocida")
        
# -------------- Algo adicional
# int convierte un string a un entero
# float convertir un string a un float
# str convertir un entero o un float a un string
# bool convertir un string a un booleano
numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el primer numero: "))

print(numero1 + numero2)

# -------------- Ejercicios correspondientes a la Seccion 1 de python

#1 Verificar si un numero es par o impar (usar input).
#2 Clasificar una persona en una categoria de edad. Por ejemplo si es un niño, si es un adolescente, si es un adulto (Utilizar input).
#3 Evaluar la nota e imprimir el resultado: Por ejemplo, se recibe una nota con un input (20), y le decimos que su clasificacion (A,B,C,D,E,F)
#4 Calcular el descuento en una tienda, si el monto supera los 100$ aplicar un 10% de descuento. Por ejemplo, se recibe un numero (el monto de la compra), utilizar input.
#5 Dterminar el tipo de triangulo en base a sus lados (Equilatero, isoceles o escaleno) (Usar 3 inputs).
#6 Convertir un cantidad de dolares o bolivares o viceversa (Usar inputs).