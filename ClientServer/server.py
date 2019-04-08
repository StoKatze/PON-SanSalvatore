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
			print('Avvio')
			break
		if rcvd == 'fine':
			print('Termino')
			break
		elif not data: break
	conn.send(data.encode('utf-8'))
	conn.close()



