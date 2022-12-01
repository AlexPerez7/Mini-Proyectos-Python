#Funcion que convierte un numero binario a decimal

def decimal(binario):
    decimal = 0
    potencia = len(binario) - 1
    for digito in binario:
        decimal = decimal + int(digito) * 2 ** potencia
        potencia = potencia - 1
    return decimal

numero = input("Introduce un número binario: ")
print("El número decimal es: " + str(decimal(numero)))