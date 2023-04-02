#Asincrona Semana 10
'''Se solicita crear un programa que permita al usuario procesar los montos de las compras de un cliente
(Se desconoce la cantidad de compras que realizará), se contará el ingreso de datos de las compras.
Si se ingresa un monto negativo, no se debe procesar la operación, si el monto supera los $500,
se debe aplicar un 5% de descuento, pero si supera los $1000 se debe aplicar un 10% de descuento.'''

print("--------------------------------------------------")
print("== Bienvenido Ing. a nuestro programa ==")
print("--------------------------------------------------\n")


print("Inicio del programa.\n")
print("Ingrese los datos que se le pidan para determinar si el monto que debe pagar puede recibir un descuento.\n")

#definir variables
x = 1
sumaMonto = 0
montoNegativo = False

# pedirle al usuario que indique la cantidad de compras que realizó
NumCompras = int(input("Cuantas compras necesita realizar -> "))

# estructura While para que escriba la cantidad de Monto que pagó en cada compra
while x <= NumCompras:
    Monto = float(input("Ingrese la cantidad de monto por compra realizada -> $"))

    if Monto < 0:
        print("\n========================================================================")
        print("\nEl monto ingresado es negativo. No se procesará la operacion.")
        print("\n========================================================================")
        montoNegativo = True
        break

    sumaMonto = sumaMonto + Monto
    x = x+1

#Estructura IF para verificar si se debe aplicar un descuento añadiendo el valor boleano para que si el usuario escribe un número negativo no se realice el proceso


if not montoNegativo:
    if sumaMonto >= 500 and sumaMonto < 1000:
        sumaMonto *= 0.95
        print("\n============================================================================================================================")
        print("\nAl tener un monto más de $500 se le ha aplicado un descuento del 5%. Ahora deberá pagar: $",sumaMonto)
        print("\n============================================================================================================================")
        
    elif sumaMonto >= 1000:
        sumaMonto *= 0.9
        print("\n============================================================================================================================")
        print("\nAl tener un monto más de $1000 se le ha aplicado un descuento del 10%. Ahora deberá pagar: $",sumaMonto)
        print("\n============================================================================================================================")
        
    else:
        print("\n=======================================================================================================================================")
        print("\nLastimosamente su monto no supera los $500, por lo que no se le puede aplicar descuento. El monto total que debe pagar es: $",sumaMonto)
        print("\n=======================================================================================================================================")


# Indicar el fin del programa si no se ingresó un monto negativo que impida el desarrollo del proceso
if not montoNegativo:
    print("\nFIN del programa! Gracias por usarlo.\n")
