

def comparacion():#Definiendo para hacer una comparación de valores
    prueba = False
    while(not prueba):
        try:
            A = int(input("\nIngrese el primer valor\n"))
            B = int(input("Ingrese el segundo valor\n"))
            C = int(input("Ingrese el tercer valor\n"))
        except ValueError:
            print("Debes escribir un número")

        if(A == B and A == C and C == B ):
            print("Todos los numeros son iguales")
            texto = open("comparación.txt","w")
            print("Todos los números son iguales",file = texto)
        elif(A == B):
            print("El valor diferente es: ", C)
            texto = open("comparación.txt","w")
            print(f"El valor diverente es {C}",file = texto)
        elif(A == C):
            print("El valor diferente es: ", B)
            texto = open("comparación.txt","w")
            print(f"El valor diverente es: {B}",file = texto)
        elif(B == C):
            print("El valor diferente es: ", A)
            texto = open("comparación.txt","w")
            print(f"El valor diferente es: {A}",file = texto)
        elif(A > B and A > C):
            Z = A+B+C
            print("El primer valor es mayor, por lo tanto la suma de los tres es: ", Z)
            texto = open("comparación.txt","w")
            print(f"El primer valor es mayor, por lo tanto la suma de los tres es: {Z}   ",file = texto)
        elif(B > A and B > C):
            Z = A*B*C
            print("El segundo valor es el mayor, por lo tanto la multiplicación de los tres es: ", Z)
            texto = open("comparación.txt","w")
            print(f"El segundo valor es el mayor, por lo tanto la multiplicación de los tres es: {Z}",file = texto)
        elif(C > A and C > B):
            Z = A,B,C
            print("El tercer valor es el mayor, por lo tanto ", Z)
            texto = open("comparación.txt","w")
            print(f"El tercer valor es el mayor, por lo tanto {Z}", file = texto)
        break

def divisor():#Definiendo para saber los divisores de un número
    try:
        numero = int(input("ingrese un valor: "))#se solicita que ingrese un valor
        resultado = [i for i in range(1, numero+1) if numero % i == 0]
        return resultado
    except ValueError:
        print("¡Debes escribir un número!")
    texto = open ("Divisores.txt","w")
    print(f"Los divisores son: {divisor()}",file=texto)

def contador():#Definiendo aumento de 2 en 2
    try:
        no1 = int(input("Ingrese su valor inicial: "))
        no2 = int(input("Ingrese su valor final: "))
        for x in range(no1, no2+2, 2):
            print(x)
            texto = open("Aumento.txt","a")
            print(f"{x}", file = texto)
    except ValueError:
        print("¡Debes escribir un número!\n")

def descendente():#Definiendo contador descendente de 1
    try:
        num1 = int(input("Ingrese un valor: "))
        num2 = int(input("Ingrese el segundo valor:"))
        for x in range(num1, num2-1,-1):
            print(x)
            texto = open("Decremento.txt","a")
            print(f"{x}", file=texto)
    except ValueError:
        print("¡Debes escribir un número!")

def Menu1():#Solicitando valores para menú principal
    correcto = False
    num = 0
    while(not correcto):
        try:
            correcto = True
            num = int(input("Ingrese una opción: "))
        except ValueError:
            print("Seleccione una opción valida")
    return num

salir = False
while not salir:#Selección de opción del menu principal
    print("1. Comparación de números \n2. Divisores de un número")
    print("3. Aumento de número de 2 en 2 \n4. Descendente" )
    print("5. para salir")
    opcion = Menu1()
    if opcion == 1:
        comparacion()
    elif opcion == 2:
        print("Los divisores son:",divisor())
    elif opcion == 3:
        contador()
    elif opcion == 4:
        descendente()
    elif opcion == 5:
        salir = True
    else:
        print("\nIngrese una opción valida")
print("\nGracias por usar el programa")
