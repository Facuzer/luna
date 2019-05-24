def evaluar_examenes(cantidad_ejs, porcentaje_aprobacion):
    """
    Función que sirve para calificar una lista de evaluaciones dada su
    cantidad de ejercicios y el porcentaje necesario para aprobar, suponiendo
    que todos los ejercicios valen lo mismo. La función evaluará la cantidad
    necesaria de alumnos hasta que el profesor ingrese un valor centinela que
    es: '*'.

    La función recibe dos parámetros, deben ser, el primero la cantidad de
    ejercicios totales de la evaluación, que debe ser de tipo int. Y el
    segundo el porcentaje de aprobación que debe ser un número de tipo int o
    float. En caso de que se ingresen datos no numéricos, devolerá None.

    La función no devuelve parámetros. Al llamar a la función entra en un
    bucle, preguntándole al profesor cuántos ejercicios resolvio bien el alumno
    específico, hasta que el profesor ingrese el valor centinela que en este
    caso es *, al ingresar este valor el programa entenderá que no hay más
    alumnos para evaluar, imprimirá un string avisando esto y se irá de la
    función. Si el valor no es '*', lo que hará la función es imprimir en
    pantalla cuánto porcentaje de la evaluación completó correctamente
    el alumno, y especificando si aprobó o no. Y pasará automaticamente
    al próximo alumno, así sucesivamente hasta que se ingrese el valor
    centinela."""
    # Valido los datos.
    if not isinstance(cantidad_ejs, int):
        return None
    if not isinstance(porcentaje_aprobacion, (int, float)):
        return None
    # Creo una variable para guardar la cantidad de ejercicios bien que hizo el
    # alumno.
    cantidad_ejs_bien = ""
    # Creo una variable iterador para guardar el paso del bucle en el que me
    # encuentro, esto me sirve para poder saber que número de alumno estoy
    # evaluando(la seteo en 1 para que el primer alumno salga como "alumno 1"
    # y no como alumno 0).
    i = 1
    # Hago un bucle indefinido hasta que el profesor ingrese en el input el
    # valor '*'
    while(cantidad_ejs_bien != "*"):
        # Me fijo si me dio el valor centinela
        if cantidad_ejs_bien == "*":
            break  # Si es asi, salgo del while.
        # Creo una variable para saber si tengo que seguir en el bucle o no
        sigo = True
        while sigo:  # Hago un bucle para saber si me dio bien el valor  
            # Seteo la variable centinela en false, para que ya este asi.
            sigo = False
            # Hago un input para pedir la cantidad de ejercicios bien que resolvió
            # este alumno y lo guardo en la variable.
            cantidad_ejs_bien = input(
                "Indique cuántos ejercicios resolvio bien el alumno {}: ".format
                (i))
            try:  # Intento pasarlo a int
                if cantidad_ejs_bien == "*":
                    break
                cantidad_ejs_bien = int(cantidad_ejs_bien)
            except ValueError:
                # Si hay error, significa que ingreso un tipo de dato no int.
                # Entonces seteo la variable sigo en True.
                print("Ingreso un tipo de dato no admitido, intente de nuevo")
                sigo = True
            # Ahora me quiero fijar si me dijo que hay mas ejercicios de los
            # ejercicios totales de la prueba.
            if cantidad_ejs_bien > cantidad_ejs:
                print("Ingreso un numero mayor a los ejercicios totales.", end="")
                print(" Intente de nuevo.")
                sigo = True
        # Aca en adelante pasa si el valor ingresado no es '*' y
        # no es string

        # Calculo el porcentaje de la prueba llamando a la función.
        porcentaje_alumno = calcular_porcentaje(cantidad_ejs_bien, 
                                                cantidad_ejs)
        if porcentaje_alumno == "*":
            break
        # Me fijo si aprobó o no y lo guardo en una variable para poder luego
        # imprimirlo.
        aprobo = calcular_si_aprobo(porcentaje_aprobacion, porcentaje_alumno)
        # Imprimo en pantalla diciendo el porcentaje de aprobación y si aprobó
        # o no.
        print(
            "El alumno {} resolvió bien el {}% de la evaluación. {}".format(
            i, porcentaje_alumno, aprobo))
        # Le sumo a la variable iterador 1 para luego poder tener el número de
        # alumno en el que se encuentra el bucle.
        i = i + 1
    # Si se termino el while, indico que termino la lista de alumnos.
    print("Fin de la lista de alumnos.")


def calcular_porcentaje(cantidad_ejs_bien, cantidad_ejs):
    """
    Función que sirve para calcular el porcentaje de una evaluación dado su
    cantidad de ejs totales y la cantidad de ejs bien hechos.

    Los parámetros deben ser de tipo int. De lo contrario devuelve None. Existe
    una excepcion a esto y es que si se ingreso el valor centinela "*", devuelve
    el mismo valor para que pueda salir del while

    Devuelve valores de tipo int o float.
    """
    if cantidad_ejs_bien == "*":
        return "*"
    if not isinstance(cantidad_ejs, int):
        return None
    if not isinstance(cantidad_ejs_bien, int):
        return None
    return (int(cantidad_ejs_bien) * 100) / cantidad_ejs


def calcular_si_aprobo(porcentaje_aprobacion, porcentaje_alumno):
        """
        Función que sirve para determinar si una evaluación está aprobada
        o no dada su porcentaje necesario de aprobación y el porcentaje
        del alumno correspondiente.

        Se deben ingresar datos de tipo int o float, de lo contrario devuelve
        None.
        """
        if porcentaje_alumno >= porcentaje_aprobacion:
            return "Aprobó."
        else:
            return "No aprobó."