# Python 3.8

#Solicita 3 datos y define que tipo de triángulo es

print("\nPrograma que solicita 3 datos e identifica el tipo de triángulo que es. \n")


a = input("Ingrese el primer lado de un triángulo: ")
b = input("Ingrese el segundo lado de un triángulo: ")
c = input("Ingrese el tercer lado de un triángulo: ")

f = open("entrada.txt", "w")
print(f"Ingrese el primer lado de un triángulo: {a}", file=f)
print(f"Ingrese el segundo lado de un triángulo: {b}", file=f)
print(f"Ingrese el tercer lado de un triángulo: {c}", file=f)

if a == b and b == c :
    print("\nEl triángulo es un triángulo equilátero")
    fo = open("salida.txt", "w")
    print("\nEl triángulo es un triángulo equilátero", file=fo)

elif a == b:
    print("\nEl triángulo es un triángulo isósceles")
    fo = open("salida.txt", "w")
    print("El triángulo es un triángulo isósceles", file=fo)

else:
    print("\nEl triángulo es un triángulo escaleno")
    fo = open("salida.txt", "w")
    print("El triángulo es un triángulo escaleno", file=fo)
