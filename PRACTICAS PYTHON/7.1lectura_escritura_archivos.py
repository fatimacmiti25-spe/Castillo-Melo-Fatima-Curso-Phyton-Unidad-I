# 1. ESCRITURA DE ARCHIVOS

archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()

print("El archivo se creó correctamente.")


# 2. LECTURA DE ARCHIVOS

archivo = open("datos.txt", "r")
contenido = archivo.read()

print(contenido)

archivo.close()


# 3. LECTURA UTILIZANDO WITH

with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)