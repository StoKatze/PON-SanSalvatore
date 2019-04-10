# Script utilizzato solo per mostrare uno schermo nero quando le proiezioni non sono attive

#!/usr/bin/python
import pygame
import time
import sys

picture = pygame.image.load("test.jpg") # Carica l'immagine
picture = pygame.transform.scale(picture,(1280,720))
panel = pygame.display.set_mode((1,1), pygame.FULLSCREEN) # Imposta la dimensione dell'immagine e la modalita' a schermo intero
pygame.mouse.set_visible(False) # Nasconde il cursore
panel.blit(picture,(0,0)) # Imposta il primo punto dell'immagine
pygame.display.flip() # Aggiorna la finestra 
time.sleep(10000) # Timeout esagerato
sys.exit() # Interrompe il programmma
