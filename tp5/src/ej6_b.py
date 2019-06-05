def solo_vocales(frase):
    """
    Función que recibe una frase, es decir un conjunto de palabras separadas
    por espacio y devuelve una copia de la frase pero con solo vocales.

    Recibe por parámetro la frase que debe ser de tipo string, de lo contrario
    devuelve TypeError.

    La función devuelve un string.
    """
    # Validaciones
    if not isinstance(frase, str):
        return TypeError
    # Todo ok
    frase_final = ""
    vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U",
               "á", "é", "í", "ó", "ú", "Á", "É", "Í", "Ó", "Ú", " "]
    for letra in frase:
        if letra in vocales:
            frase_final += letra
    return frase_final