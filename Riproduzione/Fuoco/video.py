# Script per la riproduzione del video a schermo intero
# N.B. Il video non viene mostrato tramite VNC, ma solo sulla porta HDMI
# !!! N.B. Per l'audio occorre impostare una modalita' CEA e non DMT !!! Vedi: raspi-config > Advanced > Resolution

import subprocess
import time
import sys

#lunghezzaVideoSecondi = 30 # Durata del video in secondi (approssimata per eccesso)
player = subprocess.check_output(['omxplayer', '-b' , 'fuoco.mp4']) # Apre il player
#time.sleep(lunghezzaVideoSecondi) # Mette in attesa il programma fin quando non termina la riproduzione
sys.exit() # Termina lo script
