from os import system
import os


os.system ("clear")

print("##############################")
print("#    Programas chapter 6     #")
print("##############################")

def menu():
    print("\n")
    print("1. adaptive_thresholding")
    print("2. otsu_and_riddler")
    print("3. simple_thresholding")
    print("4. salir")

while True:

    menu()
    opcion = input("\nSeleccione una opción: ")

    if opcion == '1':
        os.system ("clear")
        system("python3 adaptive_thresholding.py --image coins.png")

    elif opcion == '2':
        os.system ("clear")
        system("python3 otsu_and_riddler.py --image coins.png")

    elif opcion == '3':
        os.system ("clear")
        system("python3 simple_thresholding.py --image coins.png")

    else:
        break
