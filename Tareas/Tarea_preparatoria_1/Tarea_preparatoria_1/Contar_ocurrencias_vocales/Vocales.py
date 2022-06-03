# Python 3.8

#pedir una palabra y contar cuantas veces aparece cada vocal

Cadena = input("\nIngrese una palabra en minúsculas: ")

a = "a"
contadorA = Cadena.count(a)

e = "e"
contadorE = Cadena.count(e)

i = "i"
contadorI = Cadena.count(i)

o = "o"
contadorO = Cadena.count(o)

u = "u"
contadorU = Cadena.count(u)


print("\nA se repite: " + str(contadorA) + " veces")
print("E se repite: " + str(contadorE) + " veces")
print("I se repite: " + str(contadorI) + " veces")
print("O se repite: " + str(contadorO) + " veces")
print("U se repite: " + str(contadorU) + " veces")


f = open("Data.txt", "w")

print(f"Ingrese una palabra en minúsculas: {Cadena}", file=f)
print("\nA se repite: " + str(contadorA) + " veces", file=f)
print("E se repite: " + str(contadorE) + " veces", file=f)
print("I se repite: " + str(contadorI) + " veces", file=f)
print("O se repite: " + str(contadorO) + " veces", file=f)
print("U se repite: " + str(contadorU) + " veces", file=f)
