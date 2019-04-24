import ej9  # Importo la función que cree anteriormente en otro archivo.

# Hago variable para saber si tengo que seguir pidiendo el numero.
sigo = True
while sigo:  # hago un while para pedirlo hasta que me de un int.
    # Seteo el false para que este asi desde el principio
    sigo = False
    # Pido el numero
    cantidadTotal = (input(
        "Indique la cantidad de ejercicios totales del examen que \
            desea corregir: "))
    try:  # Intento pasarlo a int.
        cantidadTotal = int(cantidadTotal)
    except ValueError:
        # Si hay error de tipo de dato, lo aviso y hago q el bucle siga
        print("Error, ingreso un tipo de dato no admitido, ingrese de nuevo")
        sigo = True

# Seteo variable para saber si tengo que seguir pidiendo el numero.
sigo = True
while sigo:  # hago un while para pedirlo hasta que me de un int.
    sigo = False  # Seteo el false para que este asi desde el principio
    porcentajeAprobacion = (input(  # Pido el numero
        "Indique el porcentaje de aprobacion necesario para aprobar: "))
    try:  # Intento pasarlo a int.
        porcentajeAprobacion = int(porcentajeAprobacion)
    except ValueError:
        # Si hay error de tipo de dato, lo aviso y hago q el bucle siga
        print("Error, ingreso un tipo de dato no admitido, ingrese de nuevo")
        sigo = True
# Llamo a la función que cree en el otro archivo. Le paso los parámetros
# que anteriormente le pedí al profesor.
ej9.evaluarExamenes(cantidadTotal, porcentajeAprobacion)
