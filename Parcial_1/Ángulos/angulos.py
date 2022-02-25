import psycopg2

connection =  psycopg2.connect(
    host="localhost",
    user="postgres",
    password="123456",
    database="angulos",
    port="5432"
)

while True:
    try:
        a1 = int(input("\nIngrese el valor del primer angulo: "))
        a2 = int(input("Ingrese el valor del segundo angulo "))

        print("\n================================")
        print("\nMenú de opciones: ")
        print("\n1. Encontrar el tercer ángulo")
        print("2. Ver el historial")

        op = input("\nIngrese su opción: ")
        print("================================\n")
    except:
        print ("ERROR")
        op = '?'

    if op == '1':
        a3= 180-a1-a2
        connection.autocommit = True
        def insertardatos(angulo1,angulo2,angulo3):
            cursor = connection.cursor()
            query = f""" INSERT INTO angulos (angulo1,angulo2, angulo3) values('{angulo1}','{angulo2}','{angulo3}')"""
            cursor.execute(query)
            cursor.close()
        insertardatos(a1,a2,a3)
        print("El angulo 3 es: ",a3)
        break
    elif op == '2':

        cursor = connection.cursor()
        SQL = 'select * from angulos;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        break
    else:
        print("""has ingresado una opción incorrecta""")
