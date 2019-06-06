def cambiar_vocales(frase):
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
    vocales = ("a", "e", "i", "o", "u",
               "A", "E", "I", "O", "U",
               "á", "é", "í", "ó", "ú",
               "Á", "É", "Í", "Ó", "Ú")
    cambiar_vocales = {"a" : "e", "e" : "i", "i" : "o", "o" : "u", "u" : "a",
                       "A" : "E", "E" : "I", "I" : "O", "O" : "U", "U" : "A",
                       "á" : "é", "é" : "í", "í" : "ó", "ó" : "ú", "ú" : "á",
                       "Á" : "É", "É" : "Í", "Í" : "Ó", "Ó" : "Ú", "Ú" : "Á"}
    frase_final = ""
    for letra in frase:
        if letra in vocales:
            frase_final += cambiar_vocales[letra]
        else:
            frase_final+= letra
    return frase_final