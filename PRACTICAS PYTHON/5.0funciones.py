# 1. DEFINICIÓN Y LLAMADA DE FUNCIONES

def saludo():
    print("¡Hola, mundo!")

saludo()


# 2. PARÁMETROS Y ARGUMENTOS

def saludo_nombre(nombre):
    print(f"¡Hola, {nombre}!")

saludo_nombre("Juan")
saludo_nombre("María")


# 3. VALORES DE RETORNO

def suma(a, b):
    return a + b

resultado = suma(3, 4)
print(resultado)


# 4. FUNCIONES ANÓNIMAS (LAMBDA)

cuadrado = lambda x: x ** 2

print(cuadrado(5))


# 5. ALCANCE DE VARIABLES: LOCAL Y GLOBAL

def funcion():
    variable_local = 10
    print(variable_local)

variable_global = 20

def funcion2():
    print(variable_global)

funcion()
funcion2()
print(variable_global)

# Esta línea generaría un error porque variable_local
# solamente existe dentro de la función:
# print(variable_local)


# 6. DOCUMENTACIÓN DE FUNCIONES (DOCSTRINGS)

def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.

    Returns:
        float: El área del rectángulo.
    """
    return base * altura

print(area_rectangulo(5, 3))


# 7. FUNCIONES CON NÚMERO VARIABLE DE ARGUMENTOS

def suma_variable(*numeros):
    total = 0

    for numero in numeros:
        total += numero

    return total

print(suma_variable(1, 2, 3))
print(suma_variable(4, 5, 6, 7))