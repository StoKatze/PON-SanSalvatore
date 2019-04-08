# Programma server
import socket
import time

while True:
	HOST = '127.0.0.1'        # Indirizzo host
	PORT = 50007              # Porta
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(1)
	conn, addr = s.accept()
	print('Connected by', str(addr)) #Stampa sorgente connessione
	while True:
		data = conn.recv(1024) # Riceve dati
		rcvd = data.decode()
		if rcvd == 'inizio':
			time.sleep(30) # Attesa di 30 secondi prima di iniziare la riproduzione
			print('Avvio')
			lunghezzaVideoSecondi = 30 # Durata del video in secondi (approssimata per eccesso)
			player = subprocess.Popen(['omxplayer', '-b' , 'test.mp4']) # Apre il player
			time.sleep(lunghezzaVideoSecondi) # Mette in attesa il programma fin quando non termina la riproduzione
			player.kill() # Chiude il player
			break
		if rcvd == 'fine':
			print('Termino')
			player.kill()
			break
		elif not data: break
	conn.send(data.encode('utf-8'))
	conn.close()
