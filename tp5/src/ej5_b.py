def capitalizar_primera_letra(frase):
    """
    Función que recibe una frase, es decir un conjunto de palabras separadas
    por espacio y devuelve la misma frase pero con la primera letra de cada
    palabra en mayúsculas, sin importar las demás letras de la palabra.

    Recibe por parámetro la frase que debe ser de tipo string, de lo contrario
    devuelve TypeError.

    La función devuelve un string con la frase, pero con la primera letra de
    cada palabra en mayúsculas.
    """
    # Validaciones
    if not isinstance(frase, str):
        return TypeError
    # Todo ok
    resultado_final = []
    # Pongo todas las palabras en una lista
    palabras = frase.split(" ")
    # Las recorro y cambio la primera letra de cada palabra
    for palabra in palabras:
        # Cambio la primera letra de la palabra
        palabra = palabra[0].upper() + palabra[1:]
        resultado_final.append(palabra)
    # Lo cambio de lista a string
    resultado_final = " ".join(resultado_final)
    return resultado_final

if __name__ == "__main__":
    frase = input("Ingrese su frase: ")
    print(capitalizar_primera_letra(frase))
