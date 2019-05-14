# -*- coding: utf-8 -*-
import math

# Hago una variable pi para poder usarla en todas las funciones
# sin necesidad de declararla duplicadas veces.
PI = math.pi


# Las siguientes funciones son para comprobación de datos, que
# se repite en todos los ejercicios.
def es_numerico(cosa):
    """
    Función que recibe cualquier tipo de dato y devuelve True si es
    de tipo numérico y False si es de cualquier otro tipo de dato.
    """
    if isinstance(cosa, (int, float)):
        return True
    return False


def es_positivo(numero):
    """
    Función que recibe un dato de tipo numérico y devuelve True si
    es positivo y False si es negativo, en el caso que el dato sea
    0, devuelve True.

    Si ingresa un tipo de dato no numérico devuelve None.
    """
    if not es_numerico(numero):
        return None
    if numero >= 0:
        return True
    return False


def perimetro_rectangulo(base, altura):
    """Función que sirve para calcular el perímetro de un rectángulo
    dadas su base y su altura.

    En los parámetros se debe ingresar dos valores de tipo numéricos positivos
    uno que hace referencia a la base y otro que hace referencia a la
    altura de un rectángulo

    La función no imprime nada, sinó que devuelve el perimetro.
    Devuelve un valor de tipo numérico.

    En caso de haber un error de tipo de variable, o que no se haya
    ingresado valor, lo informará devolviendo."""
    # Me fijo si son numéricos
    if not es_numerico(base) or not es_numerico(altura):
        return None
    # Me fijo si la base o la altura es 0
    if (base == 0 or altura == 0):
        return None
    # Me fijo si son negativos
    if not es_positivo(base) or not es_positivo(altura):
        return None
    return base * 2 + altura * 2


def area_rectangulo(base, altura):
    """Función que sirve para calcular el área de un rectángulo dadas
    su base y su altura.

    En los parámetros se debe ingresar dos valores de tipo numéricos
    positivos, uno que hace referencia a la base y el otro que hace
    referencia a la altura.

    La función no imprime nada, sino que devuelve el área del
    rectángulo dado, devuelve un tipo de dato numérico, de tipo int
    o float dependiendo el caso.

    En caso de haber un error de tipo de variable, o que no se haya
    ingresado, lo informará devolviendo None
    """
    # Me fijo si la base o la altura es 0
    if base == 0 or altura == 0:
        return None
    # Me fijo si son numéricos
    if not es_numerico(base) or not es_numerico(altura):
        return None
    # Me fijo si son negativos
    if not es_positivo(base) or not es_positivo(altura):
        return None
    area = base * altura
    return area


def area_rectangulo_coord(x1x,
                          x1y,
                          x2x,
                          x2y,
                          x3x,
                          x3y,
                          x4x,
                          x4y):
    """
    Función que sirve para obtener el área de un rectángulo dadas
    sus coordenadas en un sistema de ejes cartesianos(es decir pide
    x1,x2,x3,x4 del rectángulo).

    La función recibe los siguientes parámetros, cada uno hace
    referencia a el valor de x o de y en el punto en el plano:
    x1x,x1y = Valores del punto 1, es decir el de abajo a la
              izquierda
    x2x,x2y = Valores del punto 2, es decir el de arriba a la
              izquierda
    x3x,x3y = Valores del punto 3, es decir el de arriba a la derecha
    x4x,x4y = Valores del punto 1, es decir el de abajo a la derecha
    Todos los valores deben ser de tipo numérico.

    La función no imprime nada sino que devuelve el valor pedido, que
    es de tipo numérico.

    En caso de haber un error de tipo de variable, o que no se haya
    ingresado, lo informará devolviendo None.
    """
    def modulo_de(x):
        """Función que sirve para obtener el módulo o el valor real
        de un número.

        La función solo recibe un parámetro y debe ser un valor numérico,
        y debe ser el número que se quiere obtener el módulo.

        La función no imprime nada, sinó que devuelve un valor numérico
        que es igual al módulo del número ingresado.

        Si ingresa un valor de tipo no numérico, lo informará devolviendo
        None.
        """
        # Me fijo si es numérico
        if not es_numerico(x):
            return None
        # Está todo ok
        if x < 0:
            x = -x
        return x
    # Me fijo si me dió un valor negativo.
    valores = (x1x, x1y, x2x, x2y, x3x, x3y, x4x, x4y)
    for punto in valores:
        if not es_numerico(punto):
            return None
    # Esto no se si hacia falta pero lo hice para detectar si hay
    # algun error y no es un rectangulo
    if not x1x == x2x or not x1y == x4y or not x2y == x3y or not x3x == x4x:
        return None
    # Hago los cáculos necesarios para obtener la base y la altura teniendo
    # las x1, x2, x3, x4
    base = modulo_de(x1y - x2y)
    altura = modulo_de(x1x - x4x)
    return base * altura


def area_y_perimetro_circulo(radio):
    """Función que sirve para calcular el área y el perímetro
    de un círculo dado su radio.

    La función recibe solo un parámetro y es el radio del
    círculo en cuestión, debe ser un dato de tipo numérico positivo.

    Si se ingresa un valor no numérico o negativo se devolvera None"""
    # Me fijo si es numérico
    if not es_numerico(radio):
        return None
    # Me fijo si es negativo
    if not es_positivo(radio):
        return None
    # Ta todo ok uso las ecuaciones de los círculos.
    area = PI * (radio ** 2)
    perimetro = 2 * PI * radio
    return area, perimetro


def volumen_esfera(radio):
    """
    Función que sirve para obtener el volumen de una esfera dado su radio.

    La función recibe un solo parámetro y es el radio de la esfera en cuestión.
    Debe ser un dato de tipo numérico positivo.

    La función no imprime nada, sino que devuelve un dato de tipo numérico que
    hace referencia al volumen de la esfera.

    Si se ingresa un valor no numérico o negativo, se devolvera None.
    """
    # Me fijo si es numérico
    if not es_numerico(radio):
        return None
    # Me fijo si es negativo
    if not es_positivo(radio):
        return None
    # Ecuacion del volumen de las esferas = 4 / 3 * pi * r ** 3
    return 4 / 3 * PI * radio ** 3
