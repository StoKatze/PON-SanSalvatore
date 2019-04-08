import socket
import time

HOST = '127.0.0.1'    # Indirizzo del server
PORT = 50007          # La stessa porta usata dal server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT)) # Connessione al server
stringa = 'fine'
s.send(stringa.encode('utf-8')) # Manda la stringa codificata in utf-8
data = s.recv(1024)
s.close()