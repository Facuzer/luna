import math


def obtenerVertice(a, b, c):
    """Función que se utiliza para obtener el vértice(es decir, el máximo o mínimo)
    de una función cuadrática.

    Los parámetros a,b,c hacen referencia a los valores
    de a,b,c en la siguiente ecuacion de una función cuadrática: ax**2 + bx + c
    los tres valores deben ser números de tipo int o float.

    Devuelve un string diciendo en qué valores se encuentra el vértice y
    diciendo si es un máximo o mínimo.

    Si a es igual a 0 va a devolver una cadena informando que se ha cometido
    un error, ya que si a es 0 no sería una función cuadrática.
    Si se ingresan datos de tipos no admitidos devolverá un string informando
    el error.

    ejemplo de uso = obtenerVertice(1,1,2) siendo 1 = a,1 = b,2 = c
    en este ejemplo la función devolvería = "Hay un minimo en (-0.5,1.75)"  """
    # Me fijo si a es 0
    if a == 0:
        # Si a es 0 entonces que devuelva error.
        return("Error. La función ingresada no es una función cuadrática.")
    # Recorro los numeros para saber si son de tipo numérico.
    for numeros in [a, b, c]:
        if not(isinstance(numeros, int) or isinstance(numeros, float)):
            # Si hay alguno que no es de tipo numérico, entonces devuelvo
            # un error.
            return("Error. Ha ingresado tipos de datos no admitidos.")

    # Calculo el valor de x y de y del vértice. El nombre xV y yV hacen
    # referencia a vértice en x y vértice en y.
    # Para calcular xV uso la fórmula matemática.
    xV = (-b) / (2 * a)
    # Para calcular yV solo reemplazo el valor de xV en la función.
    yV = (a * xV)**2 + b * xV + c
    # Me fijo si puedo pasar estos números a int sin cambiar el valor.
    if xV % 1 == 0:
        xV = int(xV)
    if yV % 1 == 0:
        yV = int(yV)
    # Hago una variable para guardar si la función tiene un mínimo o un
    # máximo, me doy cuenta de esto sabiendo si el valor de a en la función es
    # negativo o positivo.
    queEs = ""
    if a > 0:
        queEs = "mínimo"
    else:
        queEs = "máximo"
    # Devuelvo un string diciendo los valores del máximo/mínimo y
    # especificando qué es.
    return ("Hay un {} en ({},{})".format(queEs, xV, yV))


def raiz(a, b, c):
    """Función que se utiliza para obtener una raíz de una función cuadrática.


    La función recibe tres parámetros, que es a,b,c (los valores deben ser
    numéricos) y cada uno hace referencia a los valores a,b,c en la siguiente
    ecuacion de una función cuadratica: ax**2 + bx + c

    Si existen dos raíces, la función devuelve los dos valores de la raíz
    en x, en caso contrario devuelve solo un valor en x. Si la raíz es una
    raiz compleja, también lo resuelve.

    El parámetro a debe ser si o si distinto a 0, porque sinó no sería una
    función cuadrática. En caso de que se de un valor de a que sea 0, o
    que se den valores de tipo no numérico se devolverá un string informando
    el error.
    """

    # Me fijo si a es 0
    if a == 0:
        # Si a es 0 entonces que devuelva error.
        return("Error. La función ingresada no es una función cuadrática.")
    # Recorro los numeros para saber si son de tipo numérico.
    for numeros in [a, b, c]:
        if not(isinstance(numeros, int) or isinstance(numeros, float)):
            # Si hay alguno que no es de tipo numérico, entonces devuelvo
            # un error.
            return("Error. Ha ingresado tipos de datos no admitidos.")
    # Creo una variable im para guardar si tengo que agregarle la i de
    # los complejos o no
    imaginario = ""
    # Me fijo si se pueden hacer las operaciones y si se puede lo hago
    try:
        loQueVaEnLaRaiz = b**2 - 4 * a * c
        x1 = (-b + math.sqrt(loQueVaEnLaRaiz)) / (2 * a)
        x2 = (-b - math.sqrt(loQueVaEnLaRaiz)) / (2 * a)
    except BaseException:
        # Si no se pueden hacer las operaciones, esto quiere decir que no hay
        # raíces reales, entonces en tal caso empiezo a calcular la raiz
        # compleja.
        x1 = (-b + math.sqrt(-loQueVaEnLaRaiz)) / (2 * a)
        x2 = (-b - math.sqrt(-loQueVaEnLaRaiz)) / (2 * a)
        # Seteo la variable de los complejos con una i para saber que
        # tengo que agregarle la i al final ya que el resultado es
        # complejo.
        imaginario = "i"
    # Paso a int los resultados si se puede
    if x1 % 1 == 0:
        x1 = int(x1)
    if x2 % 1 == 0:
        x2 = int(x2)
    if imaginario == "i":  # Si tengo que agregar la i la agrego.
        x1 = str(x1) + imaginario
        x2 = str(x2) + imaginario
    # Me fijo si hay un resultado o dos para dar
    if x1 != x2:
        # Si hay dos devuelvo 2
        return x1, x2
    else:
        # Si hay uno devuelvo 1
        return x1


def interseccionEntreRectas(pendiente1, ordenadaOrigen1, 
                            pendiente2, ordenadaOrigen2):
    """Función que se utiliza para obtener la intersección entre dos rectas dadas
    sus pendientes y sus ordenadas de origen.

    Los parámetros que pide la función son:
    pendiente1 = hace referencia a la pendiente de la primer recta.
    ordenadaOrigen1 = hace referencia a la ordenada de origen de la primer recta.
    pendiente2 = hace referencia a la pendiente de la segunda recta.
    ordenadaOrigen2 = hace referencia a la ordenada de origen de la segunda recta.
    Todos los parámetros deben de tipo entero o float.

    La función devuelve el resultado en x de la intersección entre las dos
    rectas, el tipo de dato que devuelve puede ser int o float, dependiendo
    cuanto valga el valor en x de la intersección.

    Si se dan dos pendientes iguales, no existíria nunca una intersección
    o(si las ordenadas de origen tambien son iguales) serían la misma función
    y tendrían una intersección indefinida.
    En ambos casos se devolvería un string informando lo ocurrido.
    Si se ingresan datos no admitidos devolvería un error informando lo
    ocurrido."""
    # Recorro los numeros para saber si son de tipo numérico.
    for numeros in [pendiente1, ordenadaOrigen1, pendiente2, ordenadaOrigen2]:
        if not(isinstance(numeros, int) or isinstance(numeros, float)):
            # Si hay alguno que no es de tipo numérico, entonces devuelvo
            # un error.
            return("Error. Ha ingresado tipos de datos no admitidos.")
    # Me fijo si los valores de las pendientes son iguales para ver si se
    # puede obtener la intersección o no.
    if pendiente1 == pendiente2:
        # Me fijo si las ordenadas de origen son iguales para saber si es la
        # misma función.
        if ordenadaOrigen1 == ordenadaOrigen2:
            # Devuelvo el error especificando cuál fue.
            return "Las funciones que se ingresaron son iguales, es decir que \
                hay una interseccion indefinida."
        else:
            # Devuelvo el error especificando cuál fue.
            return "Las funciones ingresadas son paralelas, esto quiere decir\
                que no existe intersección."
    # Creo una variable intersección y le asigno el valor de la
    # intersección, este valor queda definido igualando las dos funciones y
    # pasando un valor para el otro lado.
    interseccion = -(ordenadaOrigen2 - ordenadaOrigen1) / (pendiente2 - pendiente1)
    if interseccion % 1 == 0:  # Intento ver si puedo pasar el resultado a int.
        interseccion = int(interseccion)  # Si se puede lo paso.
    
    return interseccion  # Devuelvo el valor.


# print(obtenerVertice(1,0,4))
