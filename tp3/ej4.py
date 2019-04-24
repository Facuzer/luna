import math


# Creo una función para sacar la distancia al centro de un punto, ya que
# se usa dos veces estas líneas de código.
def distanciaCentro(listaPuntos):
    """Función que se utiliza para obtener la distancia al centro de un punto.

    El parámetro p debe ser una lista de dos elementos int o float.

    La función devuelve un número que hace referencia a la distancia al centro
    del punto dado.

    Si se ingresa un tipo de dato distinto que int o float en la lista, o no
    se ingresa una lista, sale de la función sin hacer nada.

    A continuación un ejemplo:
    distanciaCentro([1,2])
    en el ejemplo, haría referencia a un punto con x=1 y y=2"""
    # Me fijo si no me dió una lista
    if not(isinstance(listaPuntos, list)):
        # Si no me dió una lista, salgo de la función sin hacer nada, ya que
        # así lo especifiqué en la documentación.
        return
    # Me fijo si ingresó algún tipo de dato no soportado
    for numero in listaPuntos:
        if not(isinstance(numero, int) or isinstance(numero, float)):
            # Si es así, salgo de la función ya que asi lo especifiqué en la
            # documentación.
            return
    # Creo variables para almacenar el valor de los puntos, los llamo catetos,
    # ya que voy a aplicar el teorema de pitágoras.
    cateto1 = abs(listaPuntos[0])
    cateto2 = abs(listaPuntos[1])
    # Almaceno en d(distancia) el valor final para hacer luego un return.
    # Lo que estoy haciendo en la siguiente línea de código es aplicar el
    # teorema de Pitágoras al triángulo que se forma entre el punto dado y el
    # eje de coordenadas.
    distancia = math.sqrt(cateto1**2 + cateto2**2)
    return distancia


# Creo puntos para guardar lo pedido.
punto1 = [int(input("Ingrese el valor en X del punto 1: ")),
          int(input("Ingrese el valor en Y del punto 1: "))]
punto2 = [int(input("Ingrese el valor en X del punto 2: ")),
          int(input("Ingrese el valor en Y del punto 2: "))]
punto3 = [int(input("Ingrese el valor en X del punto 3: ")),
          int(input("Ingrese el valor en Y del punto 3: "))]
# Hago variables para guardar las distancias al centro de cada punto.
distanciaPunto1 = distanciaCentro(punto1)
distanciaPunto2 = distanciaCentro(punto2)
distanciaPunto3 = distanciaCentro(punto3)
# Comparo cada distancia para saber cuál es la más grande.
# Y luego los imprimo en pantalla.
if distanciaPunto1 > distanciaPunto2 and distanciaPunto1 > distanciaPunto3:
    print(
        "El punto 1({},{}) es el que esta mas lejos del centro ".format(
            punto1[0],
            punto1[1]))
elif distanciaPunto2 > distanciaPunto1 and distanciaPunto2 > distanciaPunto3:
    print(
        "El punto 2({},{}) es el que esta mas lejos del centro ".format(
            punto2[0],
            punto2[1]))
else:
    print(
        "El punto 3({},{}) es el que esta mas lejos del centro ".format(
            punto3[0],
            punto3[1]))
