import math


def obtener_vertice(a, b, c):
    """Función que se utiliza para obtener el vértice(es decir, el máximo o mínimo)
    de una función cuadrática.

    Los parámetros a,b,c hacen referencia a los valores
    de a,b,c en la siguiente ecuacion de una función cuadrática: ax**2 + bx + c
    los tres valores deben ser números de tipo int o float.

    Devuelve un string diciendo en qué valores se encuentra el vértice y
    diciendo si es un máximo o mínimo.

    Si a es igual a 0 va a devolver uNone, ya que si a es 0, no sería una función
    cuadrática.

    Si se ingresan datos de tipos no admitidos devolverá None.

    ejemplo de uso = obtenerVertice(1,1,2) siendo 1 = a,1 = b,2 = c
    en este ejemplo la función devolvería = "Hay un minimo en (-0.5,1.75)"  """
    # Me fijo si a es 0
    if a == 0:
        # Si a es 0 entonces que devuelva error.
        return None
    # Recorro los numeros para saber si son de tipo numérico.
    for numeros in [a, b, c]:
        if not(isinstance(numeros, int) or isinstance(numeros, float)):
            # Si hay alguno que no es de tipo numérico, entonces devuelvo
            # un error.
            return None

    # Calculo el valor de x y de y del vértice. El nombre xV y yV hacen
    # referencia a vértice en x y vértice en y.
    # Para calcular xV uso la fórmula matemática.
    x_v = (-b) / (2 * a)
    # Para calcular yV solo reemplazo el valor de xV en la función.
    y_v = (a * x_v)**2 + b * x_v + c
    # Me fijo si puedo pasar estos números a int sin cambiar el valor.
    if x_v % 1 == 0:
        x_v = int(x_v)
    if y_v % 1 == 0:
        y_v = int(y_v)
    # Hago una variable para guardar si la función tiene un mínimo o un
    # máximo, me doy cuenta de esto sabiendo si el valor de a en la función es
    # negativo o positivo.
    que_es = ""
    if a > 0:
        que_es = "mínimo"
    else:
        que_es = "máximo"
    # Devuelvo un string diciendo los valores del máximo/mínimo y
    # especificando qué es.
    if __name__ == "__main__":
        return ("Hay un {} en ({},{})".format(que_es, x_v, y_v))
    else:
        return(que_es, (x_v, y_v))

def raiz(a, b, c):
    """Función que se utiliza para obtener una raíz de una función cuadrática.

    La función recibe tres parámetros, que es a, b, c (los valores deben ser
    numéricos) y cada uno hace referencia a los valores a, b, c en la siguiente
    ecuación de una función cuadrática: ax**2 + bx + c

    Si existen dos raíces, la función devuelve los dos valores de la raíz
    en x, en caso contrario devuelve solo un valor en x. Si la raíz es una
    raiz compleja, también lo resuelve.

    El parámetro a debe ser si o si distinto a 0, porque sinó no sería una
    función cuadrática. En caso de que se de un valor de a que sea 0, o
    que se den valores de tipo no numérico se devolverá None.
    """

    # Me fijo si a es 0
    if a == 0:
        # Si a es 0 entonces que devuelva error.
        return None
    # Recorro los numeros para saber si son de tipo numérico.
    for numeros in [a, b, c]:
        if not(isinstance(numeros, int) or isinstance(numeros, float)):
            # Si hay alguno que no es de tipo numérico, entonces devuelvo
            # un error.
            return None
    # Creo una variable imaginario para guardar si tengo que agregarle la i de
    # los complejos o no
    imaginario = ""
    # Me fijo si se pueden hacer las operaciones y si se puede lo hago
    try:
        lo_que_va_en_la_raiz = b**2 - 4 * a * c
        x1 = (-b + math.sqrt(lo_que_va_en_la_raiz)) / (2 * a)
        x2 = (-b - math.sqrt(lo_que_va_en_la_raiz)) / (2 * a)
    except ValueError:
        # Si no se pueden hacer las operaciones, esto quiere decir que no hay
        # raíces reales, entonces en tal caso empiezo a calcular la raiz
        # compleja.
        x1 = (-b + math.sqrt(-lo_que_va_en_la_raiz)) / (2 * a)
        x2 = (-b - math.sqrt(-lo_que_va_en_la_raiz)) / (2 * a)
        # Seteo la variable de los complejos con una i para saber que
        # tengo que agregarle la i al final ya que el resultado es
        # complejo.
        imaginario = "i"
    # Paso a int los resultados si se puede
    if x1 % 1 == 0:
        x1 = int(x1)
    if x2 % 1 == 0:
        x2 = int(x2)
    if imaginario == "i":  # Si tengo que agregar la i de imaginario la agrego.
        x1 = str(x1) + imaginario
        x2 = str(x2) + imaginario
    if x1 != x2:  # Me fijo si hay un resultado o dos para dar
        # Si hay dos devuelvo 2
        return x1, x2
    else:
        return x1  # Si hay uno devuelvo 1


def interseccion_entre_rectas(pendiente1, ordenada_origen1, 
                            pendiente2, ordenada_origen2):
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
    for numeros in [pendiente1, ordenada_origen1, pendiente2, ordenada_origen2]:
        if not(isinstance(numeros, int) or isinstance(numeros, float)):
            # Si hay alguno que no es de tipo numérico, entonces devuelvo
            # un error.
            return("Error. Ha ingresado tipos de datos no admitidos.")
    # Me fijo si los valores de las pendientes son iguales para ver si se
    # puede obtener la intersección o no.
    if pendiente1 == pendiente2:
        # Me fijo si las ordenadas de origen son iguales para saber si es la
        # misma función.
        if ordenada_origen1 == ordenada_origen2:
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
    interseccion = -(ordenada_origen2 - ordenada_origen1) / (pendiente2 - pendiente1)
    if interseccion % 1 == 0:  # Intento ver si puedo pasar el resultado a int.
        interseccion = int(interseccion)  # Si se puede lo paso.
    
    return interseccion  # Devuelvo el valor.


# print(obtenerVertice(1,0,4))

print (raiz(10, 10, 10))
