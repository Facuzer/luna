def matriz_identidad(n):
    """Función que se utiliza para imprimir una matriz identidad del volumen
    especificado.

    El parámetro n indica el volumen de la matriz y debe ser un número de tipo
    int positivo entre 1 y 50, de caso contrario devuelve None.
    Las cotas especificadas anteriormente son debido a que si
    el número ingresado fuese mayor, no entraría en la pantalla de la terminal.

    La función no devuelve ningún valor, sino que imprime en pantalla la
    matriz."""
    # Me fijo si el valor dado es de tipo int, caso contrario informo que se
    # cometió un error
    if not isinstance(n, int):
        return None
    # Me fijo si me dió un valor negativo, si es asi lo informo.
    if not n > 0:
        return None
    # Me fijo si me dió un valor fuera de las cotas.
    if n > 50:
        return None
    # Creo lista para guardar la matriz
    lista_matriz = []
    # Creo dos variables para saber: si ya puse el 1 y qué lugar debe ocupar
    # el 1 en la próxima iteración del bloque for.
    # Seteo en 0 la variable para que cuando empiezen las iteraciones, el
    # primer 1 este en la primera posición
    ultimo_uno = 0
    # La siguiente variable es para saber si en toda la iteración del segundo
    # bloque ya puse un uno o no.
    listo = False
    # Le puse un _ porque no uso la variable del bucle en ningún momento, sino
    # que solo uso el bloque para las iteraciones
    for _ in range(0, n):
        for j in range(0, n):
            # Comparo si la iteración del bloque corresponde a la misma en la
            # que tengo que poner el 1, y si ya lo puse antes o no.
            if ultimo_uno == j and not listo:
                # Si se cumplen las condiciones que imprima un 1 en vez de un 0
                # con el final " " así no se pasa a la próxima línea.
                if __name__ == "__main__":
                    print("1", end="  ")
                else:
                    lista_matriz.append(1)
                # Seteo el listo en True para saber que ya puse el 1.
                listo = True
                # Sumo a la variable 1 para saber, en el próximo ciclo, en qué
                # posición poner el uno.
                ultimo_uno += 1
            else:
                # Si no hay que poner un uno, pongo un cero con un final " "
                # para que no salte de linea
                if __name__ == "__main__":
                    print("0", end="  ")
                else:
                    lista_matriz.append(0)
        # Seteo la variable listo en False para que en el próximo ciclo se
        # pueda comparar para saber si necesito poner el 1 o no.
        listo = False
        # Imprimo un salto de línea para que la matriz aparezca bien.
        if __name__ == "__main__":
            print("\n")
        else:
            lista_matriz.append("_")
    return lista_matriz

matriz_identidad(5)
