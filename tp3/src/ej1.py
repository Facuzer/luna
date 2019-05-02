def repetirPalabra(palabra):
    """Función que se utiliza para repetir una palabra 1000 veces sin saltos
    de línea y con un espacio entre cada repetición.

    Recibe un solo parámetro, que es la palabra a repetir mil veces.

    La función no devuelve ningún valor sinó que lo imprime en pantalla."""
    print((palabra + " ") * 1000)

# Pidiendo al usuario que ingrese la palabra a repetir.
palabraPedida = input("Ingrese la palabra a repetir: ")
# Usando la función para repetir la palabra, con el parámetro que le pedí
# anteriormente al usuario.
repetirPalabra(palabraPedida)
