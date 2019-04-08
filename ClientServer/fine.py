import socket
import time

HOST = '192.169.203.81'    # Indirizzo del server
PORT = 50007          # La stessa porta usata dal server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Crea l'oggetto Socket
s.connect((HOST, PORT)) # Connessione al server
stringa = 'fine' # Messaggio da inviare
s.send(stringa.encode('utf-8')) # Manda la stringa codificata in utf-8
data = s.recv(1024) # Riceve il messaggio di chiusura connessione
s.close() # Chiude la connessione
