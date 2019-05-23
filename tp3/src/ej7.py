def que_dia_es(dia_del_anio):
    """ Función que, suponiendo que el primer día del año es lunes, imprime el día
    de la semana que es, dado el día del año.

    La función recibe un solo parámetro y debe ser el dia del año, un número
    de tipo entero entre 1 y 366.

    La función imprime un string y en caso de que no se hayan respetado las
    cotas o se haya dado un tipo de dato incorrecto, devolverá None."""
    # Me fijo si hay algun error al llamar a la función
    # Si me dieron un diaDelAnio de tipo distinto a int entonces que devuelva
    # error
    if not isinstance(dia_del_anio, int):
        if __name__ == "__main__":
            print("Error. Se ingreso un tipo de dato no admitido.")
        else:
            return None
    # Si me dieron un diaDelAnio que no esta entre 1 y 366 entonces que me
    # devuelva error
    if not(dia_del_anio > 0 or dia_del_anio <= 366):
        if __name__ == "__main__":
            print("Error. Se ingreso un valor que no está entre 1 y 366.")
        else:
            return None
    # Está todo ok entonces empiezo

    # Creo una tupla para que cuando sepa que día de la semana toca, luego lo
    # pueda imprimir en letras(Esto lo hice para no tener que hacer un montón
    # de ifs anidados).
    dias_en_letras = (
        "Domingo",
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado",
        "Domingo"
    )
    # Me fijo qué dia del año es con una simple ecuación.
    # dia_del_anio = dia_del_anio - (dia_del_anio // 7) * 7
    dia_del_anio = dia_del_anio % 7
    # Paso el día del año que me quedó en números a letras, gracias a la
    # tupla.
    dia_del_anio = dias_en_letras[dia_del_anio]
    # Imprimo el día del año en pantalla.
    print(dia_del_anio)


for i in range (1,367):
    que_dia_es(i)
