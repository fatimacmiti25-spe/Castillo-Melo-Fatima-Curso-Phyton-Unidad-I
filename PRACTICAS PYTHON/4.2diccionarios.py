# CREACIÓN Y ACCESO

persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])


# MÉTODO GET()

print(persona.get("nombre"))
print(persona.get("profesion"))


# MÉTODOS DE DICCIONARIOS

# Mostrar todas las claves
print(persona.keys())

# Mostrar todos los valores
print(persona.values())

# Mostrar los pares clave-valor
print(persona.items())


# UPDATE()

persona.update({"profesion": "Ingeniero"})

print(persona)