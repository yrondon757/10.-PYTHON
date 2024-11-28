# Expresiones Regulares
# Para usar expresiones regulares en Python es necesario importar el modulo re

# Importamos el modulo re
import re

texto = "The rain in Spain"
ex = re.search("^The.*Spain$", texto)
print(ex)

# El modulo re ofrece un conjunto de funciones que nos permite buscar una cadena para una coincidencia

# findall : Devuelve una lista que contiene todas las coincidencias.
# search : Devuelve un objeto Match que contiene la primera coincidencia.
# split : Divide la cadena en una lista de cadenas.
# sub : Reemplaza las coincidencias con la cadena especifica

# findall
texto = "The rain in Spain"
ex = re.findall("\s", texto)
print(ex)

# search
texto = "The rain in Spain"
ex = re.search("\s", texto)
print(ex)

# split
texto = "The-rain-in-Spain"
ex = re.split("\-", texto, 2) # Podemos tambien controlar cuantas veces queremos que se realice el split
print(ex)

texto = "The rain in Spain"
ex = re.sub("\s", "-", texto, 3) # Podemos tambien controlar cuantas veces se reemplaza
print (ex)

# El objeto match tiene propiedades y metodos utiles para recuperar informacion sobre la busqueda y el resultado

# .span() Devuelve una tupla que contiene las posiciones inicial y final de la coincidencia.
# .string Devuelve la cadena en la que se realizo la busqueda.
# .group() Devuelve la cadena que coincide con la expresion regular.

# span()
texto = "The rain in Spain"
ex = re.search("rain", texto)
print(ex.span()) # (4, 8)

# string
print(ex.string)

# group()
print(ex.group()) # rain