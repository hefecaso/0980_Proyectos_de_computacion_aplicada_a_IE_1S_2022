import random
import psycopg2

connection =  psycopg2.connect(
    host="localhost",
    user="postgres",
    password="123456",
    database="ocho",
    port="5432"
)

while True:
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    print("Dado1: ",dado1)
    print("Dado2: ", dado2)

    try:
        if dado1 + dado2 == 8 :
            print("\nUsted ha ganado! :3")
            connection.autocommit = True
            def insertardatos(dados,resultado):
                cursor = connection.cursor()
                query = f""" INSERT INTO ocho(dados,resultado) values('{dados}','{resultado}')"""
                cursor.execute(query)
                cursor.close()
            insertardatos(dado1+dado2,"ganó")
            break

        elif dado1 + dado2 == 7:
            print("\nUsted ha perdido :(")
            connection.autocommit = True
            def insertardatos(dados,resultado):
                cursor = connection.cursor()
                query = f""" INSERT INTO ocho(dados,resultado) values('{dados}','{resultado}')"""
                cursor.execute(query)
                cursor.close()
            insertardatos(dado1+dado2,"perdió")
            break
        else:
            print("Sigue lanzando")
    except:
        break
