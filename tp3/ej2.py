def imprimirFichasDomino():
    """Función que se utiliza para imprimir en pantalla todas las fichas del
    dominó.

    No requiere ningún parametro.

    No devuelve ningún valor, sino que imprime en pantalla."""
    # Hago dos bucles para poder imprimir los dominós más fácil
    for i in range(0, 7):
        for j in range(0, 7):
            # Imprimo en pantalla el dominó correspondiente según el bucle en
            # el que se encuentra el programa.
            print(" ---------------- ")
            print("|   {}   |   {}   |".format(i, j))
            print(" ---------------- ")
            # Si el valor de la variable del primer bucle(i) es igual a la del
            # segundo bucle(j), sale del segundo bucle. Esto sirve para que no
            # se repitan fichas del dominó.
            if j == i:
                break
