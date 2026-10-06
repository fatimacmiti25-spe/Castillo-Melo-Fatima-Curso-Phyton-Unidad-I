# CREACIÓN Y ACCESO

punto = (3, 4)

print(punto[0])
print(punto[1])


# MÉTODOS DE TUPLAS

mi_tupla = (1, 2, 3, 2, 4, 2)

# count() cuenta cuántas veces aparece un elemento
print(mi_tupla.count(2))

# index() obtiene la posición de la primera aparición
print(mi_tupla.index(2))

# Buscar a partir de una posición
print(mi_tupla.index(2, 2))

# Buscar indicando inicio y fin
print(mi_tupla.index(2, 2, 4))

# len() obtiene la cantidad de elementos
print(len(mi_tupla))