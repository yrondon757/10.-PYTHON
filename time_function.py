# ---------------- FUNCIONES DE TIEMPO
# Vamos a importar el modulo "time"
import time

# El modulo time en Python proporciona funciones para manejar tareas relacionadas con el tiempo.
# Las tareas relacionadas con el tiempo incluyen lo siguiente:

# - Leer la hora actual.
# - Tiempo de formateo.
# - Convertir un numero especifico en segundos y asi sucesivamente.

# En Python, el time() funcion devuelve el numero de segundos transcurridos desde la epoca (El punto donde comienza el tiempo 1970 UTC).
segundos = time.time()
print(segundos) # Imprime por consola <---- 1732820374.2957785 Estos numeros varian en cada ejecucion.

# time ---> .ctim() Funcion en Python que toma los segundos transcurridos desde la epoca como argumento y podemos convertir los segundos a una fecha legible para los humanos.
local_time = time.ctime(segundos)
print(local_time)

# time ---> .sleep() Nos permite susoender (retrasar) la ejecucion del hilo actual durante el numero de segundos que nosotros le iniquemos.
print("Iniciando programa...")
time.sleep(0)
print("Programa finalizado")

# time ---> .localtime() Toma un numero de segundos transcurridos desde la epoca como argumento y devuelve una tupla de 9 elementos.
# struct_time()
resultado = time.localtime(segundos)
print(resultado)
print(f"El mes es = {resultado.tm_mon}")
print(f"El dia es = {resultado.tm_mday}")

# time ---> .gmtime() Toma el numero de segundos transcurridos desde la epoca como argumento y devuelve una tupla de 9 elementos.
resultado2 = time.gmtime(segundos)
print(resultado2)

# time ---> .mktime() Toma una struct_time() como argumento y devuelve el numero de segundos transcurridos desde la epoca.
# El struct_time contiene lo siguiente:
# (year, month, day, hour, minute, second, weekday, day of the year, daylight saving)
format_seconds = time.mktime(resultado2)
print(format_seconds)

# time ---> .asctime() Toma una struct_time() como argumento y devuelve una cadena legible para los humanos.
resultado3 = time.asctime(resultado2)
print(resultado3)

# time ---> strftime() Toma una cadena como argumento y devuelve una cadane con el formato deseado.
resultado4 = time.strftime("%d/%m/%Y, %H:%M:%S", resultado2)
print(resultado4)

# El year = %Y
# El month = %m
# El day = %d
# El hour = %H
# El minute = %M
# El second = %S
# El weekday = %w
# El day of the year =%j
# El daylight saving = %I
# La fecha en formato cadena = %c