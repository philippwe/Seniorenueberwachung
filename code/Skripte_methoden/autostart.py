import os
import delete
import Signalton
import Ordnerpruefen

#0.) motion starten
os.system('sudo /etc/init.d/motion stop')
os.system('sudo /etc/init.d/motion start')

Signalton.output('motionAktiviert')

#1.) /srv/motion leeren
delete.cleanAll("/srv/motion/*.jpg")

#2.) Ordnerpruefen ausfuehren
Ordnerpruefen.ueberwachen()