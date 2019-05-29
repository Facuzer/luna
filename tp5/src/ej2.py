def contar_vocales(palabra):
    """

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