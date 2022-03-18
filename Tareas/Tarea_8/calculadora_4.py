import psycopg2
import os

#############################
#   Enlazando postgresql    #
#############################

try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "123456",
        dbname = "calculadora"
    )

    print("\n###############################")
    print("#    Base de datos onectado   #")
    print("###############################")

except psycopg2.Error as e:
    print("\nOcurrió un error en la conexión")
    print("\nVerifique los parámetros")

############
#   Menú   #
############

def calc():

    print ("\nMenú calculadora")
    print ("1.Sumar")
    print ("2.Restar")
    print ("3.Multiplicar")
    print ("4.Dividir")
    print ("5.Potencia")
    print ("6.Raíz")
    print ("7.Historial")
    print ("8.Salir")

    opcion = input("\nSelección el tipo de operación: ")
    os.system ("clear")
    print("")
    cursor = conexion.cursor()

#####################
#   Operaciónes     #
#####################


    if opcion == "1":
        opcion = "Suma"
        print("##############")
        print("#    Sumar   #")
        print("##############\n")
        try:
            x = float(input("Primer número: "))
            y = float(input("Segundo número: "))
        except ValueError as ERROR:
            print("\nNo letras\n")
            print(ERROR)
            print("\nIngresando números")
            return
        z = x+y
        cursor.execute("insert into calculadora(Operando, n1, n2, resultado) values(%s, %s, %s, %s);",(opcion, x, y, z))
        conexion.commit()
        print("\n========================")
        print("Resultado: ",z)
        print("========================")

    if opcion == "2":
        opcion = "Resta"
        print("##############")
        print("#    Resta   #")
        print("##############\n")
        try:
            x = float(input("Minuendo: "))
            y = float(input("Sustraendo: "))
        except ValueError as ERROR:
            print("\nNo letras\n")
            print(ERROR)
            print("\nIngresa numeros")
            return
        z = x - y
        cursor.execute("insert into calculadora(Operando, n1, n2, resultado) values(%s, %s, %s, %s);",(opcion, x, y, z))
        conexion.commit()
        print("\n========================")
        print("Resultado: ",z)
        print("========================")

    elif opcion == "3":
        print("#######################")
        print("#    Multiplicación   #")
        print("#######################\n")
        opcion = "Multiplicación"
        try:
            x = float(input("Primer factor: "))
            y = float(input("Segundo factor: "))
        except ValueError as ERROR:
            print("\nNo letras \n")
            print(ERROR)
            print("\nIngresa números")
            return
        z = x * y
        cursor.execute("insert into calculadora(Operando, n1, n2, resultado) values(%s, %s, %s, %s);",(opcion, x, y, z))
        conexion.commit()
        print("\n========================")
        print("Resultado: ",z)
        print("========================")

    elif opcion == "4":
        opcion = "Dividir"
        print("################")
        print("#    Dividir   #")
        print("################\n")
        try:
            x = float(input("Divisor: "))
            y = float(input("Dividendo: "))
        except ValueError as ERROR:
            print("\nNo letras\n")
            print(ERROR)
            print("\nIngresa números")
            return
        try:
            z = x / y
            cursor.execute("insert into calculadora(Operando, n1, n2, resultado) values(%s, %s, %s, %s);",(opcion, x, y, z))
            conexion.commit()
            print("\n========================")
            print("Resultado: ",z)
            print("========================")
        except ZeroDivisionError as ERROR:
            print("\nNo se puede dividir entre cero\n")
            print(ERROR)
            print("\nIntentalo de nuevo")
            return
    elif opcion == "5":
        opcion = "Potencias"
        print("#################")
        print("#    Potencia   #")
        print("#################\n")
        try:
            x = float(input("Base: "))
            y = float(input("Exponente: "))
        except ValueError as ERROR:
            print("\nNo letras\n")
            print(ERROR)
            print("\nIngresa números")
            return
        z = pow (x,y)
        cursor.execute("insert into calculadora(Operando, n1, n2, resultado) values(%s, %s, %s, %s);",(opcion, x, y, z))
        conexion.commit()
        print("\n========================")
        print("Resultado: ",z)
        print("========================")

    elif opcion == "6":
        opcion = "Raíz"
        print("#############")
        print("#    Raíz   #")
        print("#############\n")
        try:
            x = float(input("Numero: "))
            y = float(input("Raíz: "))
            w = float (1/y)
        except ValueError as ERROR:
            print("\nNo letras \n")
            print(ERROR)
            print("\nIngresa números")
            return
        z = pow (x,w)
        cursor.execute("insert into calculadora(Operando, n1, n2, resultado) values(%s, %s, %s, %s);",(opcion, x, y, z))
        conexion.commit()
        print("\n========================")
        print("Resultado: ",z)
        print("========================")

#########################
#   Historial y Salir   #
#########################

    elif opcion == "7":
        print("=========================================================")
        print("              Historial de operaciónes                   ")
        print("=========================================================")
        cursor = conexion.cursor()
        SQL = 'select*from calculadora;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        print("=========================================================")

    elif opcion == "8":
        print("Cerrar")
        quit()

    else:
        resp = "Operación no valida"



while True:
    calc()

#Es muy importante tener siempre esto afuera de todo
cursor.close()
conexion.close()
