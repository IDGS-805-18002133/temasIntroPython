# programa que pide 2 numeros y calcular la distancia entre esos 2 puntos
# d= sqrt((x2-x1)^2 + (y2-y1)^2)
from cmath import sqrt

print("Ingrese el primer punto:")
x1=float(input("Ingrese el valor x1: "))
y1=float(input("Ingrese el valor y1: "))
print("Ingrese el segundo punto:")
x2=float(input("Ingrese el valor x2: "))
y2=float(input("Ingrese el valor y2: "))

distancia=sqrt((x2-x1)**2 + (y2-y1)**2)
print("La distancia entre los 2 puntos es: {}".format(distancia))

