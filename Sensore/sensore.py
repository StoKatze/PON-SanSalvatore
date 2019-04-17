#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import subprocess
import sys

if (sys.argv[1] == "d"):
	print "Debug mode attivata"
else:
	immagine = subprocess.Popen(['python3', 'immagine.py'])

while True:
	try:
	      GPIO.setmode(GPIO.BOARD) # Imposta la modalita' GPIO in BOARD. Cosi si possono usare direttamente i numeri dei pin

	      PIN_TRIGGER = 7 # Assegna il controllo trigger al pin 7 (emissione ultrasuoni)
	      PIN_ECHO = 11 # Assegna il controllo echo al pin 11 (ricezione onde sonore)
	      PIN_LED = 13 # Assegna il pin 13 al LED per il debug
	      GPIO.setup(PIN_TRIGGER, GPIO.OUT) # Imposta il trigger come output
	      GPIO.setup(PIN_ECHO, GPIO.IN) # Imposta l'echo come input
	      GPIO.setup(PIN_LED, GPIO.OUT) # Imposta il led come output
	      GPIO.output(PIN_LED, GPIO.LOW) # Spegne il led
	      GPIO.output(PIN_TRIGGER, GPIO.LOW) # Disattiva l'emissione degli ultrasuoni

	      print "Waiting for sensor to settle" # Debug

	      time.sleep(0.01) # Attende che il sensore si sistemi

	      print "Calculating distance" # Debug

	      GPIO.output(PIN_TRIGGER, GPIO.HIGH) # Emette gli ultrasuoni per un tempo brevissimo

	      time.sleep(0.00001) # Leggere sopra

	      GPIO.output(PIN_TRIGGER, GPIO.LOW) # Interrompe l'emissione di ultrasuoni

	      while GPIO.input(PIN_ECHO)==0: # Ottiene il tempo in cui sono stati emessi gli ultrasuoni
	            pulse_start_time = time.time()
	      while GPIO.input(PIN_ECHO)==1: # Ottiene il tempo in cui sono stati ricevuti gli ultrasuoni
	            pulse_end_time = time.time()

	      pulse_duration = pulse_end_time - pulse_start_time # Calcola la durata dell'impulso
	      distance = round(pulse_duration * 17150, 2) # Calcola la distanza
	      print "Distance:",distance,"cm" # Debug
	      time.sleep(0.1) # Breve attesa per la lettura

	      if(distance < 290): #Trigger distanza
		GPIO.output(PIN_LED, GPIO.HIGH) # Accensione LED
		server = subprocess.Popen(['python', 'inizio.py']) # Invio segnale di avvio al secondo raspberry
		processo = subprocess.check_output(['python3', 'video.py']) # Inizio riproduzione video fuoco
		GPIO.output(PIN_LED, GPIO.LOW) # Spegne il LED
	finally:
		GPIO.cleanup() # Libera i pin GPIO


immagine.exit()
