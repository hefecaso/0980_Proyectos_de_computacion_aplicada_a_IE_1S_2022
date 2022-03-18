from os import system
import os


os.system ("clear")

print("##############################")
print("#    Programas chapter 6     #")
print("##############################")

def menu():
    print("\n")
    print("1. arithmetic")
    print("2. bitwise")
    print("3. colorspaces")
    print("4. crop")
    print("5. flipping")
    print("6. imutils")
    print("7. masking")
    print("8. resize")
    print("9. rotate")
    print("10. splitting_and_merging")
    print("11. translation")
    print("12. salir")

while True:

    menu()
    opcion = input("\nSeleccione una opción: ")

    if opcion == '1':
        os.system ("clear")
        system("python3 arithmetic.py --image trex.png")

    elif opcion == '2':
        os.system ("clear")
        system("python3 bitwise.py")

    elif opcion == '3':
        os.system ("clear")
        system("python3 colorspaces.py --image beach.png")
########
    elif opcion == '4':
        os.system ("clear")
        system("python3 crop.py --image trex.png")

    elif opcion == '5':
        os.system ("clear")
        system("python3 flipping.py --image trex.png")

    elif opcion == '6':
        os.system ("clear")
        system("python3 imutils.py")
######
    elif opcion == '7':
        os.system ("clear")
        system("python3 masking.py --image beach.png")
######
    elif opcion == '8':
        os.system ("clear")
        system("python3 resize.py --image trex.png")

    elif opcion == '9':
        os.system ("clear")
        system("python3 rotate.py --image trex.png")

    elif opcion == '10':
        os.system ("clear")
        system("python3 splitting_and_merging.py --image wave.png")

    elif opcion == '11':
        os.system ("clear")
        system("python3 translation.py --image trex.png")

    else:
        break
