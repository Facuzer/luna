def primera_letra_palabra(frase):
    """
    Función que recibe una frase, es decir un conjunto de palabras separadas
    por espacio y devuelve la primera letra de cada palabra en mayúsculas.

    Recibe por parámetro la frase que debe ser de tipo string, de lo contrario
    devuelve TypeError.

    La función devuelve un string con la primera letra de cada palabra en
    mayúsculas.
    """
    # Validaciones
    if not isinstance(frase, str):
        return TypeError
    # Todo ok
    resultado_final = ""
    # Pongo todas las palabras en una lista
    palabras = frase.split(" ")
    # Las recorro y le pido la primera letra de cada palabra.
    for palabra in palabras:
        resultado_final += palabra[0].upper()
    return resultado_final
