from os import system
import os


os.system ("clear")

print("##############################")
print("#    Programas chapter 8     #")
print("##############################")

def menu():
    print("\n")
    print("1. blurring T-rex")
    print("2. blurring  Beach")
    print("3. salir")

while True:

    menu()
    opcion = input("\nSeleccione una opción: ")

    if opcion == '1':
        os.system ("clear")
        system("python3 blurring.py --image trex.png")
#
    elif opcion == '2':
        os.system ("clear")
        system("python3 blurring.py --image beach.png")


    else:
        break
