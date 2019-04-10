import socket
import time
import sys

HOST = '192.169.203.168' # Indirizzo del server
PORT = 50007 # La stessa porta usata dal server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Crea l'oggetto socket
s.connect((HOST, PORT)) # Connessione al server
stringa = 'inizio' # Messaggio da inviare
s.send(stringa.encode('utf-8')) # Manda la stringa codificata in utf-8
data = s.recv(1024) # Riceve il messaggio di chiusura connessione
s.close() # Chiude la connessione
sys.exit() # Chiude lo script
