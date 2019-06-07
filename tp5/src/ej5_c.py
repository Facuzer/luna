def solo_palabras_con_a(frase):
    """
    Función que recibe una frase, es decir un conjunto de palabras separadas
    por espacio y devuelve la anterior frase solo con las palabras que
    empiecen con A, a, á o Á

    Recibe por parámetro la frase que debe ser de tipo string, de lo contrario
    devuelve TypeError.

    La función devuelve un string.
    """
    # Validacion
    if not isinstance(frase, str):
        return TypeError
    # Todo ok
    frase_final = []
    palabras = frase.split(" ")
    for palabra in palabras:
        if palabra[0] == "a" or palabra[0] == "A" or \
           palabra[0] == "á" or palabra[0] == "Á":
            frase_final.append(palabra)
    return " ".join(frase_final)
