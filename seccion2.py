#--------------- SECCION 2 Python

# --------- Funciones sin parametros
def miFuncion():
    print("Hola desde mi funcion sin parametros")

miFuncion() # LLamar a la funcion

# --------- Funciones con parametros
def sumar(a, b):
    resultado = a + b
    print(f"El resultado es : {resultado}")

sumar(10,20)

# ---------- Funcion con parametros con valores
def miFuncion2(nombre, saludo = "Buenas noches"):
    print(f"{saludo} {nombre}")

miFuncion2("Yenetson", "Buenas tardes")
miFuncion2("Jose")

# ---------- Funciones con retorno
def saludar(nombre = ""):
    return f"Hola {nombre}"

print(saludar("Jose"))

# ---------- Funciones recursivas
# Es una funcion que se llama a si misma durante su ejecucion
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))

# --------- LOS METODOS (STRING, LISTAS, DICCIONARIOS, TUPLAS)

# --------- Metodos de Strings
# --- Len() ---> Nos dice la longitud de un string
mensaje = "Aprendiendo Python :D"
print(len(mensaje))

# --- Upper() ---> Convierte un string a mayusculas
print(mensaje.upper())

# --- Lower() ---> Convierte un string a minusculas
print(mensaje.lower())

# --- Capitalize() ---> Convierte la primera letra en mayuscula
print(mensaje.capitalize())

# --- Title() ---> Convierte la primera letra de cada palabra en mayuscula
print(mensaje.title())

# --- Replace() ---> Nos permite reemplazar caracteres/palabras
print(mensaje.replace("Python", "Javascript"))

# --- Split() ---> Nos permite cortar cadenas y agregarlas a una lista
mensaje2 = "Hola, como estas, bien"
print(mensaje2.split(","))
print(mensaje2.split(" "))

# --- Find ---> Buscar una palabra/caracter dentro de una cadena (Devuelve la posicion)
print(mensaje2.find("estas"))

# --- Count() ---> Cuenta las veces que aparece una palabra/caracter
print(mensaje2.count("o"))

# --- startwith() ---> Comprueba si una cadena empieza con una palabra/cadena
print(mensaje2.startswith("Hola"))

# --- endswith() ---> Comprueba si una cadena termina con una palabra/cadena
print(mensaje2.endswith("bien"))



# -------------- Metodos de Listas
# --- len() ---> Nos dice la longitud de una lista
lista = [1,2,3,4,5,6,7,8]
print(len(lista))

# --- append() ---> Nos permite agregar elementos a una lista (al final de la lista)
lista.append(9)
print(lista)

# --- insert() ---> Nos permite agregar elementos a una lista en una posicion especifica
lista.insert(9, 0) # (posicion, valor)
print(lista)

# --- extend() ---> Agrega elementos a una lista (en una lista existente)
lista.extend([10,11,12,13,14,15])
print(lista)

# --- remover() ---> Elimina un elemento de una lista
lista.remove(0) # Valor del elemento a eliminar 
print(lista)

# --- pop() ---> Elimina un elemento de una lista (el ultimo)
print(lista.pop()) # Me devuelve el valor que se elimino
print(lista)



# ------------------ Metodos de las Tuplas
# --- index() ---> Devuelve la posicion de un elemento
tupla = (1,2,3,4,5,6,7,3)
print(tupla.index(2))

# --- count() ---> Contar las veces que se repite un elemento
print(tupla.count(3))

# --- Convertir una tupla a una lista
miLista = list(tupla)
print(miLista)
print(tupla)



# ----------------- Metodos de Diccionarios
diccionario = {
    "nombre": "Yenetson",
    "apellido": "Rondon",
    "edad": 33
}

# --- keys() ---> Devuelve las claves de un diccionario
print(diccionario.keys())

# --- Values() ---> Devuelve los valores de un diccionario
print(diccionario.values())

# --- Items() ---> Nos permite obtener las claves y valores del diccionario
print(diccionario.items())

# --- Get() ---> Nos permite obtener el valor de una clave
print(diccionario.get("edad"))

# --- Agregar un item al diccionario
diccionario["calificacion"] = 18.5
print(diccionario)

# --- Eliminar un item del diccionario
del diccionario["calificacion"]
print(diccionario)



# ------------------ Loops (for, while) CICLOS
#--- for
frutas = ["manzana", "pera", "naranja", "platano"]
for fruta in frutas:
    print(fruta)
    
# --- while
contador = 1
while contador <= 10:
    print(contador)
    contador += 1

# --- for con range (rango)
for i in range(1,10):
    print(i)
    
# --- for con zip
nombres = ["Jose", "Maria", "Yenetson", "Pedro", "Rossibell"]
edades = [20, 25, 33, 30, 25]

for nombre, edad in zip(nombres, edades):
    print(f"Nombre: {nombre} - Edad: {edad}")
    
# --- for con break y continue
for i in range(1,15):
    if i == 10:
        break
    elif i % 2 == 0:
        continue
    print(i)



# -------------------- CLASES EN PYTHON
# Para crear una clase en python debemos usar la palabra class y el nombre de esta clase debe ser la primera letra en mayuscula
class Persona:
    #Para definir un constructor de esta clase, se utiliza __init__
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Vamos a crear un metodo de clase para imprimir algo por consola
    def imprimir(self):
        print(f"Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad}")
    
# Vamos a crear instancias de la clase
persona1 = Persona("Jose","Perez",28)
persona2 = Persona("Maria","Gonzalez",30)
print(persona1)
# Se puede utilizar el metodo imprimir
persona1.imprimir()



# ---------------- CONCEPTOS

# Que es el metodo __init__ : Es un metodo especial en python que se llama automaticamente cuando se crea una instancia de una clase.

# Que es el parametro self : Es el primer parametro de los metodos de una clase, se llama self por convencion, pero se puede llamar como uno quiera, pero no es lo recomendable.

# Que es el metodo __str__ : Es un metodo especial en Python que se llama automaticamente cuando se imprime una instancia de una clase.

class Persona:
    #Para definir un constructor de esta clase, se utiliza __init__
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad}"
    
persona3 = Persona("Luis","Ramirez",20)

print(persona3)



# ---------------- SUB CLASE

class Categoria:
    def __init__(self, nivel):
        self.nivel = nivel
        
class Heroe(Categoria):
    def __init__(self, nombre, nivel):
        super().__init__(nivel) # Heredamos el atributo "nivel" de la clase padre Categoria
        self.nombre = nombre
    def __str__(self):
        return f"Nombre: {self.nombre} - Nivel: {self.nivel}"
    
heroe = Heroe("Spiderman", 9)
print(heroe)