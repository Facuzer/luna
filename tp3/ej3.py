def nTriagulares(n):
    """Función que se utiliza para imprimir en pantalla cierta cantidad de números
    triangulares especificados.

    El parámetro n hace referencia a la cantidad de números triangulares
    solicitados, debe ser de tipo int y mayor o igual que 0. Si se ingresa
    algun tipo de dato distinto que int o menor que 0, sale de la funcion
    sin hacer nada.

    La función no devuelve valores, sino que imprime en pantalla lo
    solicitado."""
    # Me fijo si me dió un valor de tipo distinto a int, si es asi salgo del
    # programa.
    if not(isinstance(n, int)):
        return
    # Me fijo si me dió un valor negativo, y si es así salgo de la función.
    if not(n >= 0):
        return
    # Variable que creo para almacenar el valor de i en el anterior paso del
    # bucle.
    anterior = 0
    for i in range(1, n + 1):
        # Imprimo en pantalla el valor de i, es decir el paso del bucle en el
        # que está el programa y luego el valor del anterior número sumado a i
        # (Es decir el valor del número triangular)
        print("{} - {}".format(i, anterior + i))
        # Le sumo a la variable el valor de i para poder luego imprimir en
        # pantalla en los próximos bucles.
        anterior += i


# Creo una variable para saber si me dió bien el valor es decir si es
# de tipo int
bien = False
# Hago un bucle para pedirle al usuario que me diga cuantos números
# triangulares quiere, y si me da caracteres, le vuelvo a pedir.
while not(bien):
    # Seteo en bien para empezar el paso del bucle asi.
    bien = True
    # Le pido un numero
    numeroDado = input("¿Cuántos números triangulares querés? ")
    # Compruebo si puedo pasarlo a int
    try:
        numeroDado = int(numeroDado)
    except:
        # Si hay error pongo la variable en false para que me siga haciendo
        # el bucle, ya que ingresó caracteres.
        print("Error, ingresó caracteres.")
        bien = False

# Llamo a la función, con el valor antes pedido, que ya estoy seguro que es
# de tipo int.
nTriagulares(numeroDado)
