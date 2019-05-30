def contar_vocales(palabra):
    """
    Función que recibe una palabra y decide si tiene mas letras "e" o mas
    letras "a".

    Recibe como parámetro un solo dato de tipo string, en caso contrario
    devuelve TypeError.

    La función devuelve una letra, que hace referencia a la mayor cantidad de
    vocales que hay, es decir devuelve "a" si hay mas a's y "e" si hay mas e's
    En caso de que haya iguales e's que a's, devuelve None.
    """
    # Validaciones
    if not isinstance(palabra, str):
        return TypeError
    # Todo ok
    cantidad_a = 0
    cantidad_e = 0
    # Recorro la palabra.
    for letra in palabra:
        if letra == "a":
            cantidad_a += 1
        elif letra == "e":
            cantidad_e += 1
    # Me fijo cual es el numero más grande.
    if cantidad_a == cantidad_e:
        return None
    else:
        if cantidad_a > cantidad_e:
            return "a"
        else:
            return "e"

if __name__ == "__main__":
    palabra_pedida = input("Porfavor, ingrese una palabra: ")
    result = contar_vocales(palabra_pedida)
    if result is None:
        print("Hay la misma cantidad de a's que de e's.")
    elif result == "a":
        print("Hay más a's que e's.")
    elif result == "e":
        print("Hay más e's que a's.")
