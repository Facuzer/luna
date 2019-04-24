from numpy import pi
#Calcular perimetro de un rectangulo dada b y h
def EjercicioA(b,h):
    return (b*2+h*2)
#print (EjercicioA(3,4))

#Calcular area de un rectangulo dada b y h
def EjercicioB(b,h):
    return b*h    
#print (EjercicioB(3,4))

#Calcular area de un rectangulo dada x1 x2 x3 x4
def EjercicioC(x1x,x1y,x2x,x2y,x3x,x3y,x4x,x4y):
    #x1=abajo a la izquierda x2=arriba a la izquierda x3 = arriba a la derecha x4 = abajo a la derecha
    #La x al final de cada valor hace referencia a que es un valor de x y la y a que es un valor de y
    #Funcion para hacer el modulo de algo, hice una funcion pq se repetia dos veces
    #Con modulo me refiero a |x| en matematica
    def moduloDe(x):
        if x < 0:
            x = -x
        return x    
    #Esto no se si hacia falta pero lo hice para detectar si hay algun error y no es un rectangulo
    if (not(x1x == x2x) or not(x1y == x4y) or not(x2y==x3y) or not(x3x==x4x)):
        return("Error, eso no es un rectangulo")
    b = moduloDe(x1y-x2y)
    h = moduloDe(x1x-x4x)
    return b*h
#print(EjercicioC(1,2,1,4,5,4,5,2))

#d)Calcular area y perimetro de un circulo dado el radio
def EjercicioD(r):
    pi = 3.14159265359
    area = pi*(r**2)
    perimetro = 2*pi*r
    return area,perimetro
#print(EjercicioD(5))

#e)Calcular volumen de esfera dado su radio
def EjercicioE(r):
    #Ecuacion = 4/3*pi*r**3
    pi = 3.14159265359 
    return 4/3*pi*r**3
#print(EjercicioE(5))


