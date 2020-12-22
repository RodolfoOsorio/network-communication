
import socket

# Protocolos
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Que puertos
socket_client.connect( ("127.0.0.1", 9999) )
#socket_client.connect( ("localhost", 9999) )

# Mensaje

while True:
	mensaje = input("> ").encode() # codifica a 8 bits
	socket_client.send(mensaje)
	if mensaje == b"quit":
		break

# Cierre
print("Bye")
socket_client.close()
