# #listas 

import os

lista1 =[10,5,3]
lista2 =[1.5,2.66,1.70,89.2]
lista3 =["Lunes","Martes","Miércoles"]
lista4=["Juan",45,1.92]

print(type(lista1))
print(len(lista1))
print(lista1[0])

x = 0
suma=0
while x<len(lista1):
    suma=suma+lista1[x]
    x+=1

print("La suma es: {} ".format(suma))

print(lista1)
print(lista1[0])
lista1.append(100)
print(lista1)
print(lista1[3])

lista5=[]

for x in range(5):
    valor=int(input("Ingrese un valor: "))
    lista5.append(valor)

print(lista5)

#eliminar elementos de lista
print(lista1)
lista1.pop()
print(lista1)


'''
crear un programa pedir una cantidad de n numeros y almacenarlos en un arreglo la 
salida debera ser la siguiente:
Lsita completa: XXXXXXXX
Numero de Pares de la lista: aaaaa
Numero de impares de la lista: rrrrrr
'''
def pedirCantidad():
    cantidad = int(input("Ingrese la cantidad de numeros a clasificar: "))

    numeros = []
    numerosPares = []
    numerosImpares = []
    x = 0

    for x in range(cantidad):
        valor = int(input("Ingrese un valor: "))
        numeros.append(valor)
        if valor % 2 == 0:
            numerosPares.append(valor)
        else:
            numerosImpares.append(valor)
        x += 1
        
    print("Lista completa: {}".format(numeros))
    print("Número de Pares de la lista: {}".format(numerosPares))
    print("Número de impares de la lista: {}".format(numerosImpares))

def run():
    os.system("cls")
    pedirCantidad()
    
if __name__ == "__main__":
    run()
    


print("Sorting lista1")
lista1.sort()
print(lista1)
lista1.reverse()
print(lista1)

lista1.remove(10)
print(lista1)

lista1.clear()
print(lista1)




    
    

    
    