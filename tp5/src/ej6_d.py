def check_palindromo(frase):
    """
    Función que recibe una frase, es decir un conjunto de palabras separadas
    por espacio y devuelve True si es un palíndromo y False en caso contrario.

    Recibe por parámetro la frase que debe ser de tipo string, de lo contrario
    devuelve TypeError.

    La función devuelve un string.
    nota = una frase vacía o una sola letra es un palíndromo, por lo menos
           para mi consideración.
    nota2 = no importan la capitalización, los acentos sí.
    """
    # Validaciones
    if not isinstance(frase, str):
        return TypeError
    # Todo ok
    frase = frase.replace(" ", "").upper()
    if frase == frase[::-1]:
        return True
    else:
        return False
    return frase_final
