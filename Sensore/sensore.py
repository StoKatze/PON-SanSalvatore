#!/usr/bin/python
import RPi.GPIO as GPIO
import time

while True:
	try:
	      GPIO.setmode(GPIO.BOARD)

	      PIN_TRIGGER = 7
	      PIN_ECHO = 11
	      PIN_LED = 13
	      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
	      GPIO.setup(PIN_ECHO, GPIO.IN)
	      GPIO.setup(PIN_LED, GPIO.OUT)
	      GPIO.output(PIN_LED, GPIO.LOW)
	      GPIO.output(PIN_TRIGGER, GPIO.LOW)

	      print "Waiting for sensor to settle"

	      time.sleep(0.01)

	      print "Calculating distance"

	      GPIO.output(PIN_TRIGGER, GPIO.HIGH)

	      time.sleep(0.00001)

	      GPIO.output(PIN_TRIGGER, GPIO.LOW)

	      while GPIO.input(PIN_ECHO)==0:
	            pulse_start_time = time.time()
	      while GPIO.input(PIN_ECHO)==1:
	            pulse_end_time = time.time()

	      pulse_duration = pulse_end_time - pulse_start_time
	      distance = round(pulse_duration * 17150, 2)
	      print "Distance:",distance,"cm"
	      time.sleep(0.1)

	      if(distance < 100): #Trigger distanza
		GPIO.output(PIN_LED, GPIO.HIGH)
	finally:
		GPIO.cleanup()
