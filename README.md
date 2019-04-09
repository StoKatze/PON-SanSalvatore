# Valorizziamo e diffondiamo il patrimonio culturale con la tecnologia
### La tecnologia per la valorizzazione del patrimonio storico-artistico a rischio di abbandono
### Progetto PON - FSE

## Descrizione
La parte tecnica del progetto riguarda la programmazione di alcuni Raspberry Pi per la proiezione di filmati, audio ed immagini in alcuni locali dell'abbazia di San Salvatore Maggiore (RI).

Gli script sono realizzati in Python.

# Distribuzione dei dispositivi nel locale
Nella stanza dell'installazione sono presenti i seguenti dispositivi:
* 2x Raspberry Pi 3 Model B
* 2x Proiettori 
* 1x Switch di rete

Ad ogni Raspberry Pi è collegato un proiettore tramite HDMI. Risoluzione impostata sui raspberry: 1280x720 CEA Mode.

# Funzionamento
Sul primo Raspberry (1) verrà eseguito lo script [sensore.py](Sensore/sensore.py) che rileverà eventuali movimenti. E' stato preferito un sensore ad ultrasuoni in quanto un sensore IR potrebbe non funzionare correttamente in quanto la stanza potrebbe non essere illuminata a sufficienza. Sul secondo Raspberry (2) viene avviato lo script [server.py](ClientServer/server.py) che rimane in attesa di messaggi da parte di 1.
Al rilevamento di un movimento la fase di ascolto del sensore viene interrotta e vengono lanciati due script:
* [inizio.py](ClientServer/inizio.py) che comunica a 2 di avviare la riproduzione di un file video
* [video.py](Riproduzione/video.py) che avvia la riproduzione di un secondo file video

Entrambi i file video saranno di uguale lunghezza. In particolare il video riprodotto da 1 è formato da una clip ripetuta tante volte fino a raggiugnere la lunghezza del file desiderata. Il video riprodotto da 2, invece, comprende 30 secondi iniziali di vuoto (schermo nero) per permettere ai visitatori di entrare nella stanza. 
Al termine di entrambi i video lo script [sensore.py](Sensore/sensore.py) riprenderà a rilevare movimenti.

Lo script [fine.py](ClientServer/fine.py) non viene mai utilizzato. Serve per terminare il processo del server.

## Componenti
* Raspberry Pi 3 Model B
* Proiettori vari
* Sensore di prossimità HC-SR04 ([Schema elettrico solo sensore](https://cdn.pimylifeup.com/wp-content/uploads/2018/03/Distance-Sensor-Fritz.png)) oppure ([Schema elettrico con LED](https://raw.githubusercontent.com/StoKatze/PON-SanSalvatore/master/img/schemaled.png)) ([Collegamenti su breadbord](https://raw.githubusercontent.com/StoKatze/PON-SanSalvatore/master/img/schemaelettricoled.jpg))
* LED e altri componenti elettrici (resistenze, cavi)

## Sul raspberry sono installati
* Python/Python 3
* Libreria Pygame
* Libreria RPi.GPIO

### N.B. Il progetto va preso come "proof of concept", da non utilizzare in ambienti di produzione.


