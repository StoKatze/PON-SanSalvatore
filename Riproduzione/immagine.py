#!/usr/bin/python
import pygame
import time

picture = pygame.image.load("test.jpg") #Carica l'immagine
picture = pygame.transform.scale(picture,(1280,720))
panel = pygame.display.set_mode((1280,720), pygame.FULLSCREEN)
pygame.mouse.set_visible(False) #Nasconde il cursore
panel.blit(picture,(0,0))
pygame.display.flip()
time.sleep(10000) #Timeout esagerato

