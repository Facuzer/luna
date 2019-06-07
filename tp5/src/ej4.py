def comprobar_capitalizacion(palabra_no_cap, palabra_cap):
    """
    Función que recibe dos palabras y comprueba si la segunda es la versión
    capitalizada de la primera.

    Recibe 2 parámetros, ambos de tipo string. El primero debe ser la versión
    no capitalizada y la segunda debe ser la versión capitalizada. En caso de
    que se den valores de tipo no string, devolverá TypeError.

    La función devuelve True si la segunda palabra es la versión capitalizada
    de la primera palabra. Devuelve False en caso contrario.
    """
    # Valido datos
    palabras = (palabra_cap, palabra_no_cap)
    for palabra in palabras:
        if not isinstance(palabra, str):
            return TypeError
    # Todo ok
    if(palabra_cap == palabra_no_cap.upper()):
        return True
    else:
        return False


if __name__ == "__main__":
    p_no_cap = input("Ingrese la palabra no capitalizada: ")
    p_cap = input("Ingrese la palabra capitalizada: ")
    if comprobar_capitalizacion(p_no_cap, p_cap):
        print("La segunda palabra es la versión capitalizada de la primera.")
    else:
        print("La segunda palabra no es la versión capitalizada de la primera")
