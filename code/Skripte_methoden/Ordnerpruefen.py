def ueberwachen():
	
	import time
	import sys
	import os
	import Email
	import delete
	
	curr_anzahl = 0
	anzahl = 0
	counter = 0
	deleteImages = 1
	#Ueberwachungsdauer auslesen
	
	s = []
	fobj = open ("/var/www/Konfiguration.txt" , 'r') 
	for line in fobj: 
		s.append(line)    
	fobj.close()
	
	countmax = int(s[1].strip())  #entfernt leerzeichen
	
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
				#Signalton.output()
				Email.sendMail()
				
			time.sleep(1)
			
			if (time.localtime()[4]%10)==5:
				if deleteImages == 1:
					deleteImages = 0
					delete.cleanup(10)
					anzahl = len(objects)
			else:
				deleteImages = 1
			
	except KeyboardInterrupt:
		print ("Programm beendet")
		
	except:
		print ("Fehler:" +str(sys.exc_info()[0]))
		raise