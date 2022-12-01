import socket

# Obtener el nombre del host o del PC
hostname = socket.gethostname()

# Obtener la IP del host o del PC
ip = socket.gethostbyname(hostname)

print("El nombre de la computadora es: " + hostname)
print("La dirección IP de la computadora es: " + ip)