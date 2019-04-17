# Programma server
import socket
import time
import subprocess
import sys

# Modalità debug:
# Se si avvia lo script specificando come argomento "d" si abiliterà la modalità di debug, ovvero la console rimarrà visibile e non sarà mostrato lo schermo nero.
# Altrimenti, avviando lo script con qualsiasi altro argomento (necessario almeno uno) lo script funzionerà normalmente (schermata nera per nascondere il Desktop).
if (sys.argv[1] == "d"):
	print ("Debug mode attivata")
else:
	immagine = subprocess.Popen(['python3', 'immagine.py'])

HOST = '192.169.203.168' # Indirizzo host
PORT = 50007 # Porta
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Crea l'oggetto socket
s.bind((HOST, PORT)) # Assegna indirizzo e porta al socket
while True:
	s.listen(1) # Rimane in attesa della connessione del client
	conn, addr = s.accept() # Accetta la connessione
	print('Connected by', str(addr)) # Stampa sorgente connessione
	while True:
		data = conn.recv(1024) # Riceve dati
		rcvd = data.decode() # Decodifica i dati appena ricevuti
		if rcvd == 'inizio': # Se viene ricevuta la stringa di inizio
			print('Avvio') # Debug
			player = subprocess.check_output(['omxplayer', '-b' , 'frate.mp4']) # Apre il player
			break # Una volta terminato esce dal ciclo
		if rcvd == 'fine': # Se riceve la stringa di terminazione
			print('Termino') # Debug
			break # Esce dal ciclo
		elif not data: break # Se non diceve dati termina e torna in ascolto
	#conn.send(data.encode('utf-8')) # Invia segnale chiusura connessione
	conn.close() # Chiude la connessione e torna in attesa

