import psycopg2
import numpy as np


def conexion(oper, n1, n2, res): #función para conectar con postgres
    datos = (oper,n1,n2,res) #datos recibidos almacenados en la variable
    try:
        con = psycopg2.connect(user="postgres", password="123456", host="localhost",  port="5432" ,database="calculadora")
        print ("database open")
        print ("Guardando...")
    except:
        print("No se accedió a la base de datos")

    try:
        cur=con.cursor()
        cur.execute("INSERT INTO CALCULADORA(operando,n1,n2,resultado) VALUES(%a,%a,%a,%a)", datos)
        con.commit()
        print ("record created succesfuly")
        print ("guardado")
        con.close()
    except:
        print("Fallo guardando archivos")


def borrar():
    con = psycopg2.connect(user="postgres", password="contraseña", host="localhost",  port="5432" ,database="calculadora")
    cur=con.cursor()
    cur.execute("DELETE FROM CALCULADORA")
    con.commit()
    con.close()

def divzero():
    try:
        z = x/y
    except ZeroDivisionError:

        print("n2 tiene que ser distinto de cero, valor indeterminado")

while True:
    print ('\nCalculadora')
    print ('opciones:')
    print ('1. Suma')
    print ('2. Resta')
    print ('3. Multiplicación')
    print ('4. División')
    print ('5. Exponente')
    print ('6. Raíz')
    print ('7. Borrar')
    print ('8. Salir\n')

    try:

        a = input("Seleccione una opción: ")
        a = int(a)

        if a == 1:
            print ('\nSeleccione suma\n')
            while True:
                try:
                    x = input("Ingrese n1: ")
                    y = input("Ingrese n2: ")
                    x = float(x)
                    y = float(y)
                    z = float(x+y)
                except:
                    print("Error: ambos deben ser numeros\n")
                else:
                    conexion('suma', x,y,z)
                    print ('el resultado de la operación es: ',z)
                    break
        elif a == 2:
            print ("\nSelecciono resta\n")
            while True:
                try:
                    x = input("Ingrese n1: ")
                    y = input("Ingrese n2: ")
                    x = float(x)
                    y = float(y)
                    z = float(x-y)
                except:
                    print ('Error: Ambos deben ser números\n')
                else:
                    conexion('Resta', x, y, z)
                    print('El resultado de la operación es: ', z)
                    break

        elif a == 3:
            print ("\nSelecciono multiplicacion\n")
            while True:
                try:
                    x = input("Ingrese n1: ")
                    y = input("Ingrese n2: ")
                    x = float(x)
                    y = float(y)
                    z = float(x*y)
                except:
                    print ('Error: Ambos deben ser números\n')
                else:
                    conexion('Multiplicación', x, y, z)
                    print('El resultado de la operación es: ', z)
                    break

        elif a == 4:
            print ("\nSelecciono division\n")
            while True:
                try:
                    x = input("Ingrese n1: ")
                    y = input("Ingrese n2: ")
                    x = float(x)
                    y = float(y)
                    z = float(x/y)
                except:
                    print ('Error: Ambos deben ser números\n')
                else:
                    conexion('Division', x, y, z)
                    print('El resultado de la operación es: ', z)
                    break
    except:
        print('Seleccione una opción valida')
