from os import system
import os


os.system ("clear")

print("##############################")
print("#    Programas chapter 7     #")
print("##############################")

def menu():
    print("\n")
    print("1. color_histograms")
    print("2. equalize")
    print("3. grayscale_histogram")
    print("4. histogram_with_mask")
    print("5. salir")

while True:

    menu()
    opcion = input("\nSeleccione una opción: ")

    if opcion == '1':
        os.system ("clear")
        system("python3 color_histograms.py --image beach.png")
#
    elif opcion == '2':
        os.system ("clear")
        system("python3 equalize.py --image beach.png")

    elif opcion == '3':
        os.system ("clear")
        system("python3 grayscale_histogram.py --image beach.png")

    elif opcion == '4':
        os.system ("clear")
        system("python3 histogram_with_mask.py --image beach.png")

    else:
        break
