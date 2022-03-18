import psycopq2

def conexion(oper, no1, no2, res):
    datos = (oper, no1, no2, res)
    try:
        conn = psycopq2.connect(database="DatosCalcu", user="postgres", password="123456", host="localhost")
        print("Database open")
        print("Guardando...")
    except:
        prin("No se accedió a la base de datos")

    try:
        cur = conn.cursor()
        cur.execute("Insert into DATOSCALCU(operando, n1, n2, resultado) VALUES(%a, %a, %a, %a)", datos)
        conn.commit()
        print("Record created succesfully")
        print("Guardado")
        conn.close()
    except:
        print("Fallo guardando archivos")

def borrar():
    conn = psycopq2.connect(database="DatosCalcu", user="postgres", password="123456", host="localhost")
    cur=conn.cursor()
    cur.execute("DELETE FROM DATOSCALCU")
    conn.commit()
    conn.close()

def diverso():
    try:
        z = x/y
    except ZeroDivisionError:
        print("n2 tiene que ser distinto de cer.Valor indeterminado.")

while True:
    print("\nCalculadora")
    print("Opciones: \n")
    print("1. Suma")
    print("")
    print("")
    print("")
    print("")
    print("")
