import numpy as np

def sumar (a,b):
    x = a + b
    print(("Resultado"), (x))
def restar(a,b):
    x = a - b
    print(("Resultado"), (x))
def multiplicar(a,b):
    x = a * b 
    print(("Resultado"), (x))
def dividir(a,b):
    x = a / b
    print(("Resultado"), (x))
def potencia(a,b):
    x = (np.power(a,b))
    print(("Resultado"), (x))

def raiz(a,b):
    x = (np.power(a,(1/b)))
    print(("Resultado"), (x))




#empieza el bucle
while True:
    try: #obtener datos de entrada
        a = int(input("Ingresar el primer número: \n"))
        b = int(input("Ingresar el segundo número: \n"))
        print (("Qué operación desea realizar"), (a), ("y"), (b), ("?\n")) #pregunta por la operación
        op = str(input(""" #Ofrece las opciones
        1- Sumar
        2- Restar
        3- Multiplicar
        4- Dividir
        5- Potencia
        6- Raíz \n"""))
    except: #En caso de error:
        print ("ERROR")
        op = '?'

    ####################
    #Despliegue de menú#
    ####################
    if op == '1': #si elige opcion 1 (sumar)
        sumar(a, b)
        break
    elif op == '2': #si elige opcion 2 (Restar)
        restar(a, b)
        break
    elif op == '3': #si elige opción 3 (multiplicar)
        multiplicar(a, b)
        break
    elif op == '4': #si elige opción 4 (dividir)
        dividir(a, b)
        break
    elif op == '5': #si elige opción 5 (potencia)
        potencia(a, b)
        break
    elif op == '6': #si elige opción 6 (raiz)
        raiz(a, b)
        break
    else:
        print("""Has ingresado un número de opción incorrecto""")

 
