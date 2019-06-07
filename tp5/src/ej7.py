def consulta(dicc, nombre):
    """
    Función que recibe una agenda(diccionario) y un nombre(string)
    y devuelve el número correspondiente al nombre. 
    En caso de que se ingrese un nombre no existente, entonces devuelve None.

    En caso de que se ingresen valores de tipo erróneo se devolvera TypeError.

    La función devuelve un string.
    """
    # Validaciones
    if not isinstance(dicc, dict):
        return TypeError
    if not isinstance(nombre, str):
        return TypeError
    # Todo ok
    try:
        numero = dicc[nombre]
    except KeyError: # Si pasa este error significa que no existe ese registro
        return None
    return numero

def alta(dicc, nombre, telefono):
    """
    Función que recibe una agenda(dicc), un nombre(string),
    un telefono(string) y devuelve el mismo diccionario pero con un registro
    más, usando los valores dados.

    Si se ingresan tipos de datos distintos a los pedidos se devuelve
    TypeError

    Si el registro ya existe devuelve None.
    """
    # Validaciones
    if not isinstance(dicc, dict):
        return TypeError
    if not isinstance(nombre, str):
        return TypeError
    if not isinstance(telefono, str):
        return TypeError
    # Todo ok
    # Me fijo si existe ya el registro, intentando poner el nombre en la key,
    # si tira error significa que no existe el registro.
    try:
        aux = dicc[nombre]
    except KeyError:
        # No existe el registro, entonces lo creo
        dicc[nombre] = telefono
        return dicc
    # Si no se fue de la función todavía significa que no hubo error, entonces
    # devuelvo None porque el registro ya existía.
    return None




def modificacion(dicc, nombre, telefono_nuevo):
    """
    Función que recibe una agenda(dicc), un nombre(string),
    un telefono(string) y devuelve el mismo diccionario pero con un registro
    modificado, usando los valores dados.

    Si se ingresan tipos de datos distintos a los pedidos se devuelve
    TypeError

    Si el registro no existe devuelve None.
    """
    # Validaciones
    if not isinstance(dicc, dict):
        return TypeError
    if not isinstance(nombre, str):
        return TypeError
    if not isinstance(telefono_nuevo, str):
        return TypeError
    # Todo ok
    # Me fijo si existe ya el registro, intentando poner el nombre en la key,
    # si tira error significa que no existe el registro.
    try:
        aux = dicc[nombre]
    except KeyError:
        # No existe el registro, entonces devuelvo None
        return None
    # Si no se fue de la función todavía significa que no hubo error, entonces
    # cambio el registro porque el registro ya existía.
    dicc[nombre] = telefono_nuevo
    return dicc  

if __name__ == "__main__":
    dicc = {"fede" : "1187656789",
            "valen" : "1131334144",
            "pacio" : "1157645012",
            "heras" : "1168485566"}
    cadena = ""
    while cadena != "*":
        cadena = input("Ingrese un nombre('*' para salir): ")
        if cadena == "*":
            # Hice este break feo para que no me haga todo con el valor = *
            break
        aux = consulta(dicc, cadena)
        if aux != None:  # Si existe ese registro
            print("El teléfono de {} es {}".format(cadena, aux))
            decision = input("Si desea cambiar el registro ingrese (s) de lo " +
                             "contrario ingrese cualquier valor y volverá a " +
                             "la consulta: ")
            if decision == "s":
                # Modificación
                telefono = input("Ingrese el nuevo teléfono de {}.".format(cadena))
                dicc_aux = modificacion(dicc, cadena, telefono)
                if dicc_aux == None:
                    print("Error, ese registro no existe.")
                else:
                    dicc = dicc_aux
                    print("Registro cambiado correctamente")
        else:  # Si no existe el registro
            decision = input("El registro no existe, si desea crearlo " +
                             "ingrese (s), de lo contrario ingrese " +
                             "cualquier otra cosa y volverá a la consulta.")
            if decision == "s":
                # Alta
                telefono = input("Ingrese el teléfono del nuevo registro con " +
                                 "nombre " + cadena + ": ")
                dicc = alta(dicc, cadena, telefono)
                print("Registro creado correctamente.")
    
    print("Fin del programa.")
