#Libreria
from sqlite3 import Cursor
import psycopg2

try:
    conexion =  psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "123456",
        dbname = "Tarea1"
    )
    print("\n")
    print("Conexión Exitosa!!!")
    print("\n")
except psycopg2.Error as e:
    print("Ocurrio un erro en la conexion \n")
    print("Verifique los parametros \n")



def contar_vocales(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "aeiou":
			contador += 1
	return contador




class exec:
    def menu():
        print("\n")
        print("Menu")
        print("1.Conteo de Vocales")
        print("2.Historial")
        print("3.Salir")

    def palabra():
        cadena = str(input('Ingrese su palabra: '))
        cantidad = contar_vocales(cadena)
        print(f"En la palabra '{cadena}'' hay {cantidad} vocales")

        f =  open("Contador.txt", "w")
        print("\n", file=f)
        print(f"En la palabra '{cadena}'' hay {cantidad} vocales", file=f)
        print("\n", file=f)

        cursor.execute("insert into Tabla3(palabra, vocales) values(%s, %s);",(cadena, cantidad))
        conexion.commit()
        print("Resultado: ",cantidad)



while True:
    try:
        exec.menu()
        opcion = int(input("\nQue operacion desea "))
        cursor =  conexion.cursor()
        if opcion == 1:
            exec.palabra()
            print('')
        elif opcion == 2:
            cursor = conexion.cursor()
            SQL = 'select * from Tabla3;'
            cursor.execute(SQL)
            valores = cursor.fetchall()
            print(valores)

        elif opcion == 3:
            break
        else:
            print("\n")
            print("-----------------")
            print("Datos incorrectos")
            print("-----------------")
            print("\n")
    except:
            print("\n")
            print("-----------------")
            print("Datos incorrectos")
            print("-----------------")
            print("\n")
