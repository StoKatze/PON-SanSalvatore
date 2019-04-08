#!/usr/bin/python
import time
import pygame

i = 0
while i < 5:
	name = str(i) + ".jpg" #Nome dei file sara' 0.jpg - 1.jpg e cosi via
	picture = pygame.image.load(name) #Caricamento immagine
	picture = pygame.transform.scale(picture, (1280,720))
	panel = pygame.display.set_mode((1280,720), pygame.FULLSCREEN)
	pygame.mouse.set_visible(False) #Nasconde il cursore
	panel.blit(picture, (0,0))
	pygame.display.flip()
	time.sleep(5) #Intervallo prima di cambiare immagine
	i += 1
	if(i == 5): #Ricomincia il ciclo una volta arrivato a 5
		i = 0