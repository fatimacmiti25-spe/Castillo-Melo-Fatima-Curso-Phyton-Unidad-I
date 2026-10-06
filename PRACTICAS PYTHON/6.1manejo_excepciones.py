# 1. TRY Y EXCEPT

try:
    resultado = 10 / 0
    print(resultado)

except ZeroDivisionError:
    print("Error: División por cero")


# 2. MÚLTIPLES EXCEPT

try:
    resultado = 10 / 0
    print(resultado)

except ZeroDivisionError:
    print("Error: División por cero")

except ValueError:
    print("Error: Valor inválido")


# 3. FINALLY

archivo = None

try:
    archivo = open("archivo.txt", "r")

except FileNotFoundError:
    print("Error: Archivo no encontrado")

finally:
    if archivo is not None:
        archivo.close()

    print("Bloque finally ejecutado")