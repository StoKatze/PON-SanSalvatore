# Programma server
import socket
import time
import subprocess
import sys

while True:
	HOST = '192.169.203.81' # Indirizzo host
	PORT = 50007 # Porta
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Crea l'oggetto socket
	s.bind((HOST, PORT)) # Assegna indirizzo e porta al socket
	s.listen(1) # Rimane in attesa della connessione del client
	conn, addr = s.accept() # Accetta la connessione
	print('Connected by', str(addr)) # Stampa sorgente connessione
	while True:
		data = conn.recv(1024) # Riceve dati
		rcvd = data.decode() # Decodifica i dati appena ricevuti
		if rcvd == 'inizio': # Se viene ricevuta la stringa di inizio
			print('Avvio') # Debug
			player = subprocess.check_output(['omxplayer', '-b' , 'test.mp4']) # Apre il player
			break # Una volta terminato esce dal ciclo
		if rcvd == 'fine': # Se riceve la stringa di terminazione
			print('Termino') # Debug
			sys.exit() # Termina lo script del server
		elif not data: break # Se non diceve dati termina e torna in ascolto
	conn.send(data.encode('utf-8')) # Invia segnale chiusura connessione
	conn.close() # Chiude la connessione e torna in attesa

