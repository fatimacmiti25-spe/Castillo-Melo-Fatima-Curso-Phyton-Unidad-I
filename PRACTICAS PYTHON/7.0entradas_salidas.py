# 1. ENTRADA DE DATOS DEL USUARIO

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")

print("Hola, " + nombre + "!")
print("Tienes " + edad + " años.")


# 2. ENTRADA DE DATOS CON CONVERSIÓN A ENTERO

edad = int(input("Ingresa nuevamente tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


# 3. SALIDA DE DATOS CON F-STRING

nombre = "Juan"
edad = 25

print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")