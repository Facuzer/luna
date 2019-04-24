def queDiaEs(diaDelAnio):
    """ Función que, suponiendo que el primer día del año es lunes, imprime el día
    de la semana que es, dado el día del año.

    La función recibe un solo parámetro y debe ser el dia del año, un número
    de tipo entero entre 1 y 366.

    La función imprime un string y en caso de que no se hayan respetado las
    cotas o se haya dado un tipo de dato incorrecto, imprimirá en pantalla
    avisando el error y especificando cuál fue."""
    # Me fijo si hay algun error al llamar a la función
    # Si me dieron un diaDelAnio de tipo distinto a int entonces que devuelva
    # error
    if not isinstance(diaDelAnio, int):
        print("Error. Se ingreso un tipo de dato no admitido.")
    # Si me dieron un diaDelAnio que no esta entre 1 y 366 entonces que me
    # devuelva error
    if not(diaDelAnio > 0 or diaDelAnio <= 366):
        print("Error. Se ingreso un valor que no está entre 1 y 366.")
    # Está todo ok entonces empiezo

    # Creo una tupla para que cuando sepa que día de la semana toca, luego lo
    # pueda imprimir en letras(Esto lo hice para no tener que hacer un montón
    # de ifs anidados).

    diasEnLetras = (
        "Domingo",
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Sábado",
        "Domingo"
    )
    # Me fijo qué dia del año es con una simple ecuación.
    diaDelAnio = diaDelAnio - (diaDelAnio // 7) * 7
    # Paso el día del año que me quedó en números a letras, gracias a la
    # tupla.
    diaDelAnio = diasEnLetras[diaDelAnio]
    # Imprimo el día del año en pantalla.
    print(diaDelAnio)

# Esto es para probar si funciona todo xd
# for i in range (1,367):
#  queDiaEs(i)
