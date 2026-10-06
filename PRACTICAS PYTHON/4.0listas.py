# CREACIÓN Y ACCESO A UNA LISTA

frutas = ["manzana", "banana", "naranja"]

print(frutas[0])
print(frutas[1])
print(frutas[2])

# Acceso utilizando índices negativos
print(frutas[-1])
print(frutas[-2])
print(frutas[-3])


# MÉTODOS DE LISTAS

frutas = ["manzana", "banana", "naranja"]

# Agregar un elemento
frutas.append("pera")
print(frutas)

# Insertar un elemento
frutas.insert(1, "uva")
print(frutas)

# Eliminar un elemento
frutas.remove("banana")
print(frutas)

# Eliminar un elemento por su posición
fruta_eliminada = frutas.pop(2)
print(frutas)
print(fruta_eliminada)

# Ordenar la lista
frutas.sort()
print(frutas)

# Invertir la lista
frutas.reverse()
print(frutas)


# LISTAS DE COMPRENSIÓN

numeros = [1, 2, 3, 4, 5]

cuadrados = [x ** 2 for x in numeros if x % 2 == 0]

print(cuadrados)