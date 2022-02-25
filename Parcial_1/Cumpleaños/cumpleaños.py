import datetime
import psycopg2

connection =  psycopg2.connect(
    host="localhost",
    user="postgres",
    password="123456",
    database="cumpleaños",
    port="5432"
)


dia = int(input("\nIngrese el día en que nació: "))
mes = int(input("Ingrese el mes en que nació: "))
año = int(input("Ingrese el año en que nació: "))

dia_act = int(input("\nIngrese el día actual: "))
mes_act = int(input("Ingrese el mes actual: "))
año_act = int(input("Ingrese el año actual: "))


anos_persona = año_act - año

if mes_act < mes :
    print("\n===================================")
    print("Fecha de nacimiento de la persona:")
    print(f"Día: {dia} Mes: {mes} Año: {año}")

    print(f'\nEsta persona tiene {anos_persona} y no ha cumplido años.')

else:
    print("\n===================================")
    print("Fecha de nacimiento de la persona:")
    print(f"Día: {dia} Mes: {mes} Año: {año}")

    print(f'\nEsta persona tiene {anos_persona} y ya ha cumplido años.')


connection.autocommit = True

def insertardatos(edad):
    cursor = connection.cursor()
    query = f""" INSERT INTO anos(edad) values('{edad}')"""
    cursor.execute(query)
    cursor. close()

insertardatos(anos_persona)
