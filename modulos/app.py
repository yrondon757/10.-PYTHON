# Podemos importar funciones/variables de otros archivos.
from funciones import sumar, restar
from variables import nombre, clave

print(sumar(30,5))
print(restar(10,2))
print(f"{nombre} {clave}")