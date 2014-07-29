def ueberwachen():
	
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
	fobj = open ("/var/www/Konfiguration.txt" , 'r') 
	for line in fobj: 
		s.append(line)    
	fobj.close()
	
	countmax = int(s[1].strip())  #entfernt leerzeichen
	
	#Ordner auf Veraenderungen ueberpruefen -> bei Bewegung wird ein neues Bild hinzugefuegt
	
	try:
		while True:
			#Pfad des Ordners angeben, in dem die Fotos von Motion abgespeichert werden
			#= os.listdir('C:\Users\philipp.wilken\Documents\GitHub\Seniorenueberwachung\code\Skripte')
			objects = os.listdir('/srv/motion/')
				
	# objects.sort()
	# for objectname in objects:
	#  print(objectname)   

			curr_anzahl = len(objects)
			
			if anzahl == 0:
				anzahl = curr_anzahl

			if curr_anzahl > anzahl:
				counter = 0
				anzahl = curr_anzahl
			else:
				counter = counter +1
				print counter
				
			if counter == countmax:  #10:  #30
				counter = 0
				Signalton.output("keineBewegung")
				time.sleep(30)
				Email.sendMail()
				pausse = 1
				
			time.sleep(1)
			
			if (time.localtime()[4]%10)==5:
				if deleteImages == 1:
					deleteImages = 0
					delete.cleanup(10)
					anzahl = len(objects)
			else:
				deleteImages = 1   #damit nicht eine minute lang bei jedem schleifendurchlauf geloescht wird
			
			#if roteKarte()==1:  
			#	pause = 1
			#   Signalton.output('pause')
			
			if (pause == 1):       #bei ausgelöstem alarm oder unterbrechung durch rote karte soll der zähler nicht weiterlaufen. hier wird er deshalb unterbrochen
			#sleepTime = control.userInput()
			#time.sleep(sleepTime)
				while True:
					action = input("Diese Aussage ist falsch! Stimmt das oder nicht? (y/n) ")
					#var = pixelmethode()
					if input == "y":
						Signalton.output('ueberwachungAktiviert')
						break
						# hier könnte nochmals eine Mail an alle rausgeschickt werden. Beispielsweise bei einem Fehlalarm			
			
	except KeyboardInterrupt:
		print ("Programm beendet")
		
	except:
		print ("Fehler:" +str(sys.exc_info()[0]))
		raise