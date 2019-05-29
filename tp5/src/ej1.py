def verificar_contraseña(contraseña_dada):
    """
    Función que recibe un valor de tipo string y comprueba si el valor es
    igual a la contraseña correcta.

    La función recibe un solo parámetro de tipo string, en caso de que se
    de un tipo de variable distinta de string, devolverá TypeError.

    La función devuelve True si ingreso la contraseña correcta y False en caso
    contrario.
    """
    # Valido los datos.
    if not isinstance(contraseña_dada, str):
        return TypeError
    contraseña = "fMoon"
    if contraseña_dada == contraseña:
        return True
    else:
        return False

if __name__ == "__main__":
    # Hago una variable para poder saber cuando salgo del while.
    sigo = True
    while sigo:
        sigo = False
        contraseña_pedida = input("Ingrese la contraseña: ")
        # Llamo a la función que hice, le pongo not porque si la contraseña
        # está bien devuelvo True, y si devuelve True sigue el bucle, lo cual
        # no tendria sentido.
        sigo = not verificar_contraseña(contraseña_pedida)
        if sigo == False:
            print("\nContraseña correcta.")
        else:
            print("\nContraseña incorrecta. Intente de nuevo.\n")