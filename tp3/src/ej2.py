def calcular_fichas_domino():
    """Función que se utiliza para imprimir en pantalla todas las fichas del
    dominó.

    No requiere ningún parametro.

    No devuelve ningún valor, sino que imprime en pantalla."""
    # Hago una variable para guardar el valor de los dominós para poder
    # testearlo después.
    fichas_domino = []
    # Hago dos bucles para poder imprimir los dominós más fácil
    for i in range(0, 7):
        for j in range(0, 7):
            # Imprimo en pantalla el dominó correspondiente según el bucle en
            # el que se encuentra el programa.
            if __name__ == "__main__":
                imprimir_ficha_domino(i, j)
            else:
                # Lo guardo en la variable
                fichas_domino.append((i, j))
            # Si el valor de la variable del primer bucle(i) es igual a la del
            # segundo bucle(j), sale del segundo bucle. Esto sirve para que no
            # se repitan fichas del dominó.
            if j == i:
                break
    if not __name__ == "__main__":
        return fichas_domino


def imprimir_ficha_domino(numero_1, numero_2):
    print(" ---------------- ")
    print("|   {}   |   {}   |".format(numero_1, numero_2))
    print(" ---------------- ")


calcular_fichas_domino()


