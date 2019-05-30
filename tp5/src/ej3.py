def contar_todas_las_vocales(palabra):
    """
    Función que cuenta todas las vocales en una cadena de texto, sin importar
    la mayúscula o minúscula. Y devuelve una tupla con la cantidad de veces
    que aparece cada vocal.

    El parámetro que recibe es de tipo string, caso contrario devuelve
    TypeError.

    La función devuelve una tupla de 5 valores, cada una hace referencia a
    cuantas vocales hay, en orden.
    Ej: (1, 2, 3, 4, 5)
         |  |  |  |  |
         v  v  v  v  v
         a  e  i  o  u

    En el ejemplo habría 1 a, 2 e's, 3 i's, 4 i's y 5 u's
    """
    # Validación de datos.
    if not isinstance(palabra, str):
        return TypeError
    # Ta todo ok.
    cuantas_a = 0
    cuantas_e = 0
    cuantas_i = 0
    cuantas_o = 0
    cuantas_u = 0
    for letra in palabra:
        if letra == "a" or letra == "A":
            cuantas_a += 1
        elif letra == "e" or letra == "E":
            cuantas_e += 1
        elif letra == "i" or letra == "I":
            cuantas_i += 1
        elif letra == "o" or letra == "O":
            cuantas_o += 1
        elif letra == "u" or letra == "U":
            cuantas_u += 1
    return (cuantas_a, cuantas_e, cuantas_i, cuantas_o, cuantas_u)

if __name__ == "__main__":
    palabra_pedida = input("Ingrese una cadena de texto: ")
    tupla = contar_todas_las_vocales(palabra_pedida)
    print("Tu palabra tiene {} a(s), {} e(s), {} i(s), {} o(s) y {} u(s)."
          .format(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4]))
