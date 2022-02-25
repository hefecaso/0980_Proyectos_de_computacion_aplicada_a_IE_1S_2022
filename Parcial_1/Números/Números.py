import psycopg2

connection =  psycopg2.connect(
    host="localhost",
    user="postgres",
    password="123456",
    database="unidades",
    port="5432"
)


print("\nMostrar la unidad, la decena y centena.\n")

while True:
    try:
        num = int(input("\nIngrese un numero comprendido entre 1 y 999: "))

        print("\n================================")
        print("\nMenú de opciones: ")
        print("\n1. Mostrar las centenas, decenas, unidades")
        print("2. Ver el historial")

        op = input("\nIngrese su opción: ")
        print("================================\n")

    except:
        print ("ERROR")
        op = '?'

    if op == '1':
        cen = (num-(num%100))/100
        res = num%100
        dec = (res-(res%10))/10
        uni = res%10
        print("Centena: ",int(cen))
        print("Decena: ",int(dec))
        print("Unidad:",int(uni))
        connection.autocommit = True
        def insertardatos(centena,decena,unidad):
            cursor = connection.cursor()
            query = f""" INSERT INTO unidades (centena,decena,unidad) values('{centena}','{decena}','{unidad}')"""
            cursor.execute(query)
            cursor.close()
        insertardatos(cen,dec,uni)

        break
    elif op == '2':

        cursor = connection.cursor()
        SQL = 'select * from unidades;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        break
    else:
        print("""has ingresado una opción incorrecta""")
