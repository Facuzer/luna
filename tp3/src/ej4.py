import math


# Creo una función para sacar la distancia al centro de un punto, ya que
# se usa dos veces estas líneas de código.
def distancia_centro(lista_puntos):
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
    if not isinstance(lista_puntos, list):
        # Si no me dió una lista, salgo de la función sin hacer nada, ya que
        # así lo especifiqué en la documentación.
        return
    # Me fijo si ingresó algún tipo de dato no soportado
    for numero in lista_puntos:
        if not(isinstance(numero, int) or isinstance(numero, float)):
            # Si es así, salgo de la función ya que asi lo especifiqué en la
            # documentación.
            return
    # Creo variables para almacenar el valor de los puntos, los llamo catetos,
    # ya que voy a aplicar el teorema de pitágoras.
    cateto_1 = abs(lista_puntos[0])
    cateto_2 = abs(lista_puntos[1])
    # Almaceno en distancia el valor final para hacer luego un return.
    # Lo que estoy haciendo en la siguiente línea de código es aplicar el
    # teorema de Pitágoras al triángulo que se forma entre el punto dado y el
    # eje de coordenadas.
    distancia = math.sqrt(cateto_1**2 + cateto_2**2)
    return distancia


def mayor_numero_de_tres(numero1, numero2, numero3):
    """Función que se utiliza para saber cual es el número más grande entre
    tres números.
    
    La función recibe 3 valores, los tres deben ser de tipo int o float.
    En caso contrario se devolverá None.

    La función no imprime nada sino que devuelve un string indicando cuál fue
    el mayor número ingresado, haciendo referencia al orden. En caso de que
    los numeros mas grandes sean iguales, se devolvera un string 
    indicandolo(1 = 2, 2 = 1, 1 = 2 = 3, etc)
    
    Ej:
    usa la funcion como mayor_numero_de_tres(10, 20, 30) la función
    devolverá "3"
    """
    numeros = (numero1, numero2, numero3)
    for numero in numeros:
        if not isinstance(numero, (int, float)):
            return None
    if numero1 == numero2 and numero1 == numero3:
        return "1 = 2 = 3"
    elif numero1 > numero2 and numero1 > numero3:
        return "1"
    elif numero2 > numero1 and numero2 > numero3:
        return "2"
    elif numero3 > numero1 and numero3 > numero2:
        return "3"
    elif numero1 == numero2:
        return "1 = 2"
    elif numero1 == numero3:
        return "1 = 3"
    elif numero2 ==  numero3:
        return "2 = 3"
    else:
        return "ahre"



# Esto es pedido de datos
if __name__ == "__main__":
    # Creo puntos y guardo en ellos el valor que voy a pedir 
    # lo puse en un while por si me da valores no numéricos.
    sigo = True
    while sigo:
        try:
            sigo = False
            punto1 = [int(input("Ingrese el valor en X del punto 1: ")),
                    int(input("Ingrese el valor en Y del punto 1: "))]
            punto2 = [int(input("Ingrese el valor en X del punto 2: ")),
                    int(input("Ingrese el valor en Y del punto 2: "))]
            punto3 = [int(input("Ingrese el valor en X del punto 3: ")),
                    int(input("Ingrese el valor en Y del punto 3: "))]
        except ValueError: # Si hay un error, lo avisa y intenta de nuevo
            print("Ingreso valores no admitidos, intente de nuevo.")
            sigo = True

    # Uso mi función para las distancias
    distanciaPunto1 = distancia_centro(punto1)
    distanciaPunto2 = distancia_centro(punto2)
    distanciaPunto3 = distancia_centro(punto3)
    a = mayor_numero_de_tres(distanciaPunto1,distanciaPunto2,distanciaPunto3)
    if a == "1 = 2 = 3":
        print("Todos los puntos son iguales.")
    else:
        print("El/los mayores puntos es/son: " + a)




