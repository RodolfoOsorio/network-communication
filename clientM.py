import socket
import json
import numpy

# Protocolos
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Que puertos
socket_client.connect( ("127.0.0.1", 9999) )
# socket_client.connect( ("localhost", 9999) )

# Mensaje
matrix= numpy.array( [ [10,11,12,13, 14,15,16,17]]);
matrix= numpy.append(matrix, [ [20,21,22,23, 24,25,26,27]],0)
matrix= numpy.append(matrix, [ [30,31,32,33, 34,35,36,37]],0)
matrix= numpy.append(matrix, [ [40,41,42,43, 44,45,46,47]],0)
matrix= numpy.append(matrix, [ [50,51,52,53, 54,55,56,57]],0)
matrix= numpy.append(matrix, [ [60,61,62,63, 64,65,66,67]],0)
matrix= numpy.append(matrix, [ [70,71,72,73, 74,75,76,77]],0)
matrix= numpy.append(matrix, [ [80,81,82,83, 84,85,86,87]],0)

print("Preparing message:\n", matrix) #Imprime mensaje

# Codifica mensaje
print("Coding...")
lista = matrix.tolist() # Transforma a lista
listastr = json.dumps(lista) # Transforma a str
blistastr = listastr.encode() # Codifica a 8 bits

# Envia mensaje
print("Sending...")
socket_client.send(blistastr)

# Cierre
print("Message sent!")
socket_client.close()
