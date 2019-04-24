

def anioEnNumerosRomanos(anio):
    """Función que convierte números de tipo enteros a números romanos.

    La función recibe un solo parámetro, debe ser el número a convertir en
    romanos es un número de tipo entero, en el rango de 0 a 1 000 000.

    La función devuelve un dato de tipo string con el valor en números romanos
    del numero dado.

    Si se ingresa un dato que no sea de tipo entero, o se ingresa un número
    que no cumpla con las cotas especificadas, se devolverá una cadena de
    texto informando el error que se cometió."""
    # Empiezo checkeando si hay algun error en el año dado.
    # Si no es int lo informo y salgo de la función.
    if not(isinstance(anio, int)):
        return "Error. Se ingresó un tipo de dato no soportado."
    # Si no está en el rango 0 a 1 000 000 entonces lo informo y salgo de la
    # función
    if not(anio >= 0 and anio <= 1000000):
        return "Error. Se ingresó un valor fuera de las cotas(0-1 000 000)."
    # Ta todo ok entonces sigo

    # Bueno, acá estoy creando muchas tuplas, para poder reemplazar los valores
    # numéricos del año en números romanos. Es una tupla por cada cifra,
    # ya que los valores de la unidad, son distintos que los de la decena y
    # así sucesivamente.
    unidad = ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX")
    decena = ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC")
    centena = ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM")
    unidadDeMil = (
        "",
        "M",
        "MM",
        "MMM",
        u"I\u0305V\u0305",
        u"V\u0305",
        u"V\u0305I\u0305",
        u"V\u0305I\u0305I\u0305",
        u"V\u0305I\u0305I\u0305I\u0305",
        u"I\u0305X\u0305")
    decenaDeMil = (
        "",
        u"X\u0305",
        u"X\u0305X\u0305",
        u"X\u0305X\u0305X\u0305",
        u"X\u0305L\u0305",
        u"L\u0305",
        u"L\u0305X\u0305",
        u"L\u0305X\u0305X\u0305",
        u"L\u0305X\u0305X\u0305X\u0305",
        u"X\u0305C\u0305")
    centenaDeMil = (
        "",
        "C\u0305",
        "C\u0305C\u0305",
        "C\u0305C\u0305C\u0305",
        "C\u0305D\u0305",
        "D\u0305",
        "D\u0305C\u0305",
        "D\u0305C\u0305C\u0305",
        "D\u0305C\u0305C\u0305C\u0305",
        "C\u0305M\u0305")
    unidadDeMillon = ("", u"M\u0305")
    # Creo una tupla con las tuplas para poder recorrerlas más fácil cuando
    # use el for.
    lista = (
        unidad,
        decena,
        centena,
        unidadDeMil,
        decenaDeMil,
        centenaDeMil,
        unidadDeMillon)
    # Creo una variable para guardar el número final
    final = ""
    # Paso el año a string para poder operar bien con él.
    anio = str(anio)
    # Creo una variable len con la lengitud del año, ya que lo uso varias
    # veces.
    Len = len(anio)
    # Seteo una variable para saber en qué ciclo del bucle estoy, ya que el
    # bucle for se va a recorrer al revés, entonces no me sirve la variable i
    # del bucle.
    j = 0
    # Hago un bucle for, que vaya desde la longitud del año hasta 0, lo
    # recorro al revés porque me sirve recorrer el string año al reves.
    for i in range(Len, -1, -1):
        # Creo una variable para guardar la tupla que voy a usar en este bucle
        # y la igualo a la tupla correspondiente.
        tipoDeCaracter = lista[j]

        ch = int(anio[i - 1])
        final = tipoDeCaracter[ch] + final
        if j == Len - 1:
            break
        j += 1

    return final


print(anioEnNumerosRomanos(1015))
