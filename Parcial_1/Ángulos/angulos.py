def CalcularG3(A,B,C):

# calcular el angulo en radianes
G3 = acos(B*B+C*C-A*A)
# convertir a grados
G3 = G3*180/pi


print("El tercer angulo es: {}".format(G3))
