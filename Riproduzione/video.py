# Script per la riproduzione del video a schermo intero
# N.B. Il video non viene mostrato tramite VNC, ma solo sulla porta HDMI
# !!! N.B. Per l'audio occorre impostare una modalita' CEA e non DMT !!! Vedi: raspi-config > Advanced > Resolution

import subprocess
import time
import sys

player = subprocess.check_output(['omxplayer', '-b' , 'test.mp4']) # Apre il player
sys.exit() # Termina lo script