def repetirPalabra(palabra):
    """Función que se utiliza para repetir una palabra 1000 veces sin saltos
    de línea y con un espacio entre cada repetición.

    Recibe un solo parámetro, que es la palabra a repetir mil veces.

    La función no devuelve ningún valor sinó que lo imprime en pantalla."""
    palabra_mil_veces = (palabra + " ") * 1000
    if __name__ == "__main__":
        print(palabra_mil_veces)
    else:
        return palabra_mil_veces


# Si estoy ejecutando el programa como principal entonces que pida
if  __name__ == "__main__":
    # Pidiendo al usuario que ingrese la palabra a repetir.
    palabraPedida = input("Ingrese la palabra a repetir: ")
    # Usando la función para repetir la palabra, con el parámetro que le pedí
    # anteriormente al usuario.
    repetirPalabra(palabraPedida)
