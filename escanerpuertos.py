import sys
import socket

objetivo = socket.gethostbyname(input("Introduce la dirección IP o el nombre del host: "))

print("Escaneando el objetivo " + objetivo)

try:
    for puerto in range(1, 150):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultado = s.connect_ex((objetivo, puerto))
        if resultado == 0:
            print("Puerto {} abierto".format(puerto))
        s.close()
except KeyboardInterrupt:
    print("Saliendo...")
    sys.exit()