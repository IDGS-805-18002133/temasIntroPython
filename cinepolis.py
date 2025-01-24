from io import open
import os

class ticket:
    def __init__(self):
        self.nombreDuenioTicket = ""
        self.cantPersonas = 0
        self.totalBoletos = 0
        self.totalAPagarTicket = 0.0
        self.porcentajeDescuentoTotal = 0.0
        self.metodoPago = ""
        
    def imprimirEnPantalla(self, index):
        print("\n==== Resumen de Compra #{} ====".format(index + 1))
        print("Nombre de Dueño: {}".format(self.nombreDuenioTicket))
        print("Cantidad de Personas: {}".format(self.cantPersonas))
        print("Total de Boletos: {}".format(self.totalBoletos))
        print("Método de Pago: {}".format(self.metodoPago))
        print("Total a pagar: ${:.2f}".format(self.totalAPagarTicket))

    def imprimirEnTxt(self, index):
        resumen = (
            "\n==== Resumen de Compra #{} ====\n"
            "Nombre de Dueño: {}\n"
            "Cantidad de Personas: {}\n"
            "Total de Boletos: {}\n"
            "Método de Pago: {}\n"
            "Total a pagar: ${:.2f}\n"
        ).format(index + 1, self.nombreDuenioTicket, self.cantPersonas, 
                 self.totalBoletos, self.metodoPago, self.totalAPagarTicket)
        return resumen

tickets = []

def calcularPago(boletos, metodoPago):
    porcentajeDescuentoTotal = 0.0
    
    #calcular descuentos
    if boletos >= 6:
        porcentajeDescuentoTotal += 0.15
    elif boletos >= 3:
        porcentajeDescuentoTotal += 0.10      

    totalAPagar = (boletos * 12.00) * (1 - porcentajeDescuentoTotal)

    # descuento para la tarjeta del cine(sunpongo) 
    if metodoPago == "CINECO":
        totalAPagar *= 0.9

    return totalAPagar

def run():
    os.system("cls")
    continuar = "s"
    
    while continuar != "n":
        # saber a nombre de quien queda el tiket
        nombreDuenioTicket = input("¿Quién compra?: ")
        cantPersonas = int(input("Ingrese la cantidad de personas: "))
        totalBoletos = int(input("¿Cuántos boletos quieres?: "))

        # no se pueden comprar mas de 7 boletos por persona
        while totalBoletos > 7 * cantPersonas:
            print("No puedes comprar más de 7 boletos por persona.")
            print("¿Deseas cambiar el total de boletos o personas?")
            print("a) Cambiar boletos")
            print("b) Cambiar personas")
            print("c) Salir (cancelar compra)")
            opcion = input("Selecciona una opción: ")

            if opcion == "a":
                totalBoletos = int(input("¿Cuántos boletos quieres?: "))
            elif opcion == "b":
                cantPersonas = int(input("Ingrese la cantidad de personas: "))
            elif opcion == "c":
                return 

        # metodo pago
        metodoPago = input("¿Qué método de pago deseas?\n"
                           "a) CINECO (10% de descuento adicional)\n"
                           "b) Efectivo (0% de descuento)\n"
                           "Selecciona una opción: ")

        if metodoPago == "a":
            metodoPago = "CINECO"
        elif metodoPago == "b":
            metodoPago = "Efectivo"
        else:
            print("esa opcion no estaba, voy poner efectivo por defecto XD")
            metodoPago = "Efectivo"

        totalAPagarTicket = calcularPago(totalBoletos, metodoPago)
        print("El total a pagar es de ${:.2f}".format(totalAPagarTicket))

        # crear ticket
        nuevoTicket = ticket()
        nuevoTicket.nombreDuenioTicket = nombreDuenioTicket
        nuevoTicket.cantPersonas = cantPersonas
        nuevoTicket.totalBoletos = totalBoletos
        nuevoTicket.totalAPagarTicket = totalAPagarTicket
        nuevoTicket.metodoPago = metodoPago 

        tickets.append(nuevoTicket)

        print("\nCompra total:")
        for i, t in enumerate(tickets):
            t.imprimirEnPantalla(i)

        continuar = input("\n¿Deseas agregar otra compra? (s/n): ")

    # resumen en archivo
    resumenCadena = ""
    with open("resumen.txt", "w") as resumen:
        for i, t in enumerate(tickets):
            resumenCadena += t.imprimirEnTxt(i)
        resumen.write(resumenCadena)

    print("Se ha generado el ticket con el total en el archivo 'resumen.txt'.")

if __name__ == "__main__":
    run()
