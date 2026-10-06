# PRÁCTICA 6.2 - EXCEPCIONES PERSONALIZADAS

def funcion():
    # Condición que genera una excepción personalizada
    condicion = True

    if condicion:
        raise Exception("Descripción del error")


try:
    funcion()

except Exception as e:
    print(f"Error: {str(e)}")