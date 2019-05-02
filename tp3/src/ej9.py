def evaluarExamenes(cantidadEjs, porcentajeAprobacion):
    """Función que sirve para calificar una lista de evaluaciones dada su
    cantidad de ejercicios y el porcentaje necesario para aprobar, suponiendo
    que todos los ejercicios valen lo mismo. La función evaluará la cantidad
    necesaria de alumnos hasta que el profesor ingrese un valor centinela que
    es: '*'.

    La función recibe dos parámetros, deben ser, el primero la cantidad de
    ejercicios totales de la evaluación, que debe ser de tipo int. Y el
    segundo el porcentaje de aprobación que debe ser un número de tipo int o
    float.

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
    # Creo una variable para guardar la cantidad de ejercicios bien que hizo el
    # alumno.
    cantidadEjsBien = ""
    # Creo una variable iterador para guardar el paso del bucle en el que me
    # encuentro, esto me sirve para poder saber que número de alumno estoy
    # evaluando(la seteo en 1 para que el primer alumno salga como "alumno 1"
    # y no como alumno 0).
    i = 1
    # Hago un bucle indefinido hasta que el profesor ingrese en el input el
    # valor '*'
    while(cantidadEjsBien != "*"):
        # Me fijo si me dio el valor centinela
        if cantidadEjsBien == "*":
            break  # Si es asi, salgo del while.
        # Creo una variable para saber si tengo que seguir en el bucle o no
        sigo = True
        while sigo:  # Hago un bucle para saber si me dio bien el valor  
            # Seteo la variable centinela en false, para que ya este asi.
            sigo = False
            # Hago un input para pedir la cantidad de ejercicios bien que resolvió
            # este alumno y lo guardo en la variable.
            cantidadEjsBien = input(
                "Indique cuántos ejercicios resolvio bien el alumno {}: ".format
                (i))
            try:  # Intento pasarlo a int
                cantidadEjsBien = int(cantidadEjsBien)
            except ValueError:
                # Si hay error, significa que ingreso un tipo de dato no int.
                # Entonces seteo la variable sigo en True.
                print("Ingreso un tipo de dato no admitido, intente de nuevo")
                sigo = True
            # Ahora me quiero fijar si me dijo que hay mas ejercicios de los
            # ejercicios totales de la prueba.
            if cantidadEjsBien > cantidadEjs:
                print("Ingreso un numero mayor a los ejercicios totales.", end="")
                print(" Intente de nuevo.")
                sigo = True
        # Aca en adelante pasa si el valor ingresado no es '*' y
        # no es string

        # Calculo el porcentaje de la prueba del alumno con una simple
        # ecuación.
        porcentajeAlumno = (int(cantidadEjsBien) * 100) / cantidadEjs
        # Me fijo si aprobó o no y lo guardo en una variable para poder luego
        # imprimirlo.
        if porcentajeAlumno >= porcentajeAprobacion:
            aprobo = "Aprobó."
        else:
            aprobo = "No aprobó."
        # Imprimo en pantalla diciendo el porcentaje de aprobación y si aprobó
        # o no.
        print(
            "El alumno {} resolvió bien el {}% de la evaluación. {}".format(
            i, porcentajeAlumno, aprobo))
        # Le sumo a la variable iterador 1 para luego poder tener el número de
        # alumno en el que se encuentra el bucle.
        i = i + 1
    # Si se termino el while, indico que termino la lista de alumnos.
    print("Fin de la lista de alumnos.")
