# Vamos a importar el modulo del SISTEMA OPERATIVO
import os

# --------- MANEJO DE ARCHIVOS
# La funcion para trabajar con archivos en Python, es la funcion open()
# La funcion open() toma dos argumentos: NombreDeArchivo y el Modo.
# Hay cuatro metodos (modos) diferentes para abrir un archivo.

#1) r ---> Leer: Es un valor predeterminado. Abre un archivo para leer, y da error si el archivo no existe.
#2) w ---> Escribir: Abre un archivo para escribir, creando el archivo si no existe.
#3) a ---> Agregar: Abre un archivo para agregar, creando el archivo si no existe.
#4) x ---> Crea un archivo, devuelve un error si el archivo ya existe.

# Estos dos metodos a continuacion nos permiten como debe manejarse el archivo. Si en modo binario o modo texto.
#5) t ---> Texto: Es un valor predeterminado. Abre el archivo en modo texto.
#6) b ---> Binario: Abre el archivo en modo binario.

# open abre el archivo .txt
f = open("demofile.txt", "r")

# La funcion .read() es un metodo para leer el contenido del archivo.
print(f.read())

# Si el archivo se encuentra en otra ubicacion distinta, debemos especificar la ruta del archivo.
# f = open("C:\\Users\User\Desktop\demofile.txt", "r")

# De forma predeterminada, el read() el cual es un metodo, devuelve el texto completo. Tambien podemos espicificar cuantos caracteres queremos leer.
f = open("demofile.txt", "r")
print(f.read(5))

# Podemos leer el archivo linea por linea.
f = open("demofile.txt", "r")
for row in f:
    print(f"Linea: {row}")
    
# La funcion .close() es un metodo que permite cerrar el archivo abierto.
# Es BUENA PRACTICA CERRAR EL ARCHIVO ABIErTO UNA VEZ SE UTILICE.
# Siempre se deben cerrar los archivos, debido al almacenamiento bufer, es posible que los cambios realizados en unos archivos no se muestren hasta que los cierres.

f.close()

# Para crear y escribir en un archivo.
# Para escribir en un archivo existente, debe agregar un parametro a la funcion open()
# a ---> Agregar: Se agrega al final del archivo.
# w ---> Escribir: Sobrescribe el contenido del archivo.

f = open("demofile2.txt", "a")
f.write("Hola desde Python xD")
f.close()

# Escribir / Sobrescribir un archivo
f = open("demofile2.txt", "w")
f.write("Sobrescritura.")
f.close()

# Crear un archivo en Python, usando el metodo open().
# x ---> Crear: Crear un archivo, y da error si el archivo existe.

# Crear un archivo
"""f = open("demofile3.txt", "x")
f.close()"""

# Eliminar archivos
# Para eliminar un archivo en Python, debemos importar el modulo del sistema operativo.
# Para eliminar una vez importado el modulo del sistema, usamos os.remove().

if os.path.exists("demofile3.txt"):
    os.remove("demofile3.txt")
    print("Se elimino correctamente.")
else:
    print("El archivo no existe.")