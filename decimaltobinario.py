#Pasar de decimal a binario

#Función que convierte un número decimal a binario

def binario(decimal):
    binario = ""
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

numero = int(input("Introduce un número decimal: "))
print("El número binario es: " + binario(numero))