from os import system
import os


os.system ("clear")

print("##############################")
print("#    Programas chapter 6     #")
print("##############################")

def menu():
    print("\n")
    print("1. canny")
    print("2. sobel_and_laplacian")
    print("3. salir")

while True:

    menu()
    opcion = input("\nSeleccione una opción: ")

    if opcion == '1':
        os.system ("clear")
        system("python3 canny.py --image coins.png")

    elif opcion == '2':
        os.system ("clear")
        system("python3 sobel_and_laplacian.py --image coins.png")

    else:
        break
