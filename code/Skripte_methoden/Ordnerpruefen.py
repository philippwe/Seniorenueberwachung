def getNewest(pfad):

    import os
    import glob
    try:
        newest = max(glob.iglob(pfad+"/*.*"), key = os.path.getctime)
    except ValueError:
        return 0
    
    return newest
   
def ueberwachen(pfad):
	
	import time
	import sys
	import os
	import Email	 #Email.py
	import delete    #delete.py
	import control   #control.py
	import Signalton #Signalton.py
	
	curr_anzahl = 0
	anzahl = 0
	counter = 0
	deleteImages = 1
	pause = 0
	
	#Ueberwachungsdauer auslesen
	s = []
	fobj = open ("/var/www/Konfiguration.txt" , "r") 
	for line in fobj: 
		s.append(line)    
	fobj.close()
	
	countmax = int(s[1].strip())  #entfernt leerzeichen
	print countmax
    
	#Ordner auf Veraenderungen ueberpruefen -> bei Bewegung wird ein neues Bild hinzugefuegt
	#todo: eigene methode "bewegung pruefen"
	try:
		while True:
			#Pfad des Ordners angeben, in dem die Fotos von Motion abgespeichert werden
			#= os.listdir('C:\Users\philipp.wilken\Documents\GitHub\Seniorenueberwachung\code\Skripte')
	
			objects = os.listdir(pfad)
	
			curr_anzahl = len(objects)
			
			if anzahl == 0:
				anzahl = curr_anzahl

			if curr_anzahl > anzahl:
				counter = 0
				anzahl = curr_anzahl
			else:
				counter = counter +1
				print counter #todo noch entfernen
				
			if counter == countmax:  #10:  #30
				counter = 0
				Signalton.output("keineBewegung")
				
				time.sleep(30)
				s = 0
				if s <= 30:
					s = s+1	
					time.sleep(1) 
					#todo bewegung pruefen
				else:
					Email.sendMail()
					pause = 1
				
			#time.sleep(1)
			
			if (time.localtime()[4]%10)==5:
				if deleteImages == 1:
					deleteImages = 0
					delete.cleanup(10)
					anzahl = len(objects)
			else:
				deleteImages = 1   #damit nicht eine minute lang bei jedem schleifendurchlauf geloescht wird
			
			
			newest = getNewest(pfad)

			if (newest != 0):
				break
				#if roteKarte()==1:  
				#	pause = 1
				#   Signalton.output('pause')

			if (pause == 1):       #bei ausgeloestem alarm oder unterbrechung durch rote karte soll der zaehler nicht weiterlaufen. hier wird er deshalb unterbrochen
			#sleepTime = control.userInput()
			#time.sleep(sleepTime)
				while True:
					action = input("Diese Aussage ist falsch! Stimmt das oder nicht? (y/n) ")
					#var = pixelmethode()
					if input == "y":
						Signalton.output("ueberwachungAktiviert")
						break
						# hier koennte nochmals eine Mail an alle rausgeschickt werden. Beispielsweise bei einem Fehlalarm	

	except KeyboardInterrupt:
		print ("Programm beendet")
		
	except:
		print ("Fehler:" +str(sys.exc_info()[0]))
		raise
		
