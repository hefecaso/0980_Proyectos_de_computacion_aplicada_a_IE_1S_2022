import psycopq2, psycopq2.extras

class Calculadora(object):

    def __init__(self):
        self.ope = 0
        self.n1 = 0
        self.n2 = 0
        self.answer = 0

    def inicio(self):
        print("\nBienvenido a la calculadora con base de datos")
        print("Suma (s), Resta (r), Multiplicación (m), Division (d), Para borrar base de datos (b)")
        while (1):
            self.ope = raw_input("Seleccióne la operación a realizar: ")
            if(self.ope == 's' or self.ope == 'r' or self.ope == 'm' or self.ope == 'd' or self.ope == 'b'):
                break

        if self.ope != 'b':
            while(1):
                self.n1 = raw_input("\nIngrese n1 -->")
                try:
                    float(self.n1)
                    break
                except ValueError:
                    print("\nIngrese un valor numérico.")

            while(1):
                self.n2 = raw_input("\nIngrese n2 -->")
                try:
                    float(self.n2)
                    if(float(self.n2) == 0.0 and self.ope == 'd'):
                        print("\nEl resultado es indefinido")
                    else:
                        break
                except ValueError:
                    print("\nIngrese un valor numérico")

            self.Operacion()
        else:
            self.Borrado()

    def operacion(self):
        if self.ope == 's':
            self.answer = float(self.n1) + float(self.n2)
        elif self.ope == 'r':
            self.answer = float(self.n1) - float(self.n2)
        elif self.ope == 'm':
            self.answer = float(self.n1) * float(self.n2)
        elif self.ope == 'd':
            self.answer = float(self.n1) / float(self.n2)

        print(self.answer)

        self.Base()

    def Base(self):

        conn = psycopq2.connect(database = 'calculadora', user = 'postgres', password = '123456', host = 'localhost')
        cur = conn.cursor()
        cur.execute("INSERT INTO calcu (operador, n1, n2, answer) VALUES ('"+str(self.operado)(+str(self.n1)"','""))
