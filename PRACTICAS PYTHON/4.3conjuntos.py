# CREACIÓN DE CONJUNTOS

frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])

print(frutas)
print(numeros)


# OPERACIONES CON CONJUNTOS

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

# Unión
union = conjunto1 | conjunto2
print(union)

# Intersección
interseccion = conjunto1 & conjunto2
print(interseccion)

# Diferencia
diferencia = conjunto1 - conjunto2
print(diferencia)

# Diferencia simétrica
diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)


# MÉTODOS DE CONJUNTOS

frutas = {"manzana", "banana", "naranja"}

# Agregar un elemento
frutas.add("pera")
print(frutas)

# Eliminar un elemento
frutas.remove("banana")
print(frutas)

# Eliminar un elemento si existe
frutas.discard("uva")
print(frutas)

# Eliminar todos los elementos
frutas.clear()
print(frutas)