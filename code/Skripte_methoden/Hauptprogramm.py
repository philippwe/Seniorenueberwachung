########### globale Variablen 


#Auf diese koennen die Methoden zugreifen

gv_stopCheckCard = 0
gv_stopCheckChange = 0
gv_stopCheckChangeConfirm = 0
gv_stopPeriodicCleanup = 0
gv_stopPeriodicCleanupConfirm = 0

gv_checkChangeReturn = 0
gv_checkCardReturn = 0  #0 = nichts, 1=rot, 2=gelb

gv_newImage = 0

def getCheckTime():  #liest den Zeitraum aus, in welcher sich die ueberwachte Person bewegen muss
	
	s = []
	fobj = open ("/var/www/Konfiguration.txt" , "r") 
	for line in fobj: 
		s.append(line)    
	fobj.close()
	
	countmax =  int(s[1].strip())  #entfernt leerzeichen
	#countmax = countmax * 60
	return countmax

def getNewest(iv_path):

	import os
	import glob
	try:
		newest = max(glob.iglob(iv_path+"/*.*"), key = os.path.getctime)
		
	except ValueError:
		return 0
	except AttributeError:
		return 0
	
	return newest

def checkChange(iv_counter, iv_pfad, id):  #ueberprueft ob dateien dazu gekommen sind und loescht regelmaessig alte bilder
	
	import os
	import time

	curr_anzahl = 0
	anzahl = 0
	counter = 0
	
	global gv_stopCheckChangeConfirm
	global gv_checkChangeReturn
	global gv_stopCheckChange
	global gv_newImage
	
	gv_stopCheckChange = 0
	gv_stopCheckChangeConfirm = 0
	gv_checkChangeReturn = 0
	
	#Ordner auf Veraenderungen ueberpruefen -> bei Bewegung wird ein neues Bild hinzugefuegt
	while (gv_checkChangeReturn == 0) and (gv_stopCheckChange == 0):
				
		time.sleep(1)
		objects = os.listdir(iv_pfad)
		curr_anzahl = len(objects)
			
		if anzahl == 0:
			anzahl = curr_anzahl
		#fuer den fall, dass bilder geloescht wurden
		if curr_anzahl < anzahl:
			anzahl = curr_anzahl
			
		if curr_anzahl > anzahl:
			counter = 0
			anzahl = curr_anzahl
			gv_newImage = 1
		else:
			counter = counter +1
			print id+": "+str(counter) #todo noch entfernen
			
		if counter == iv_counter:  #10:  #30	
			gv_checkChangeReturn = 1 #lange zeit keine bewegung -> benachrichtigung

	print "--------------- returning from checkChange"
	
	gv_stopCheckChangeConfirm = 1
	return
	
def periodicCleanup(iv_deletePeriod):

	import delete
	import time

	global gv_stopPeriodicCleanup
	global gv_stopPeriodicCleanupConfirm
	gv_stopPeriodicCleanupConfirm = 0
	gv_stopPeriodicCleanup = 0
	
	while (gv_stopPeriodicCleanup == 0):
		
		if (time.localtime()[4]%10)==5:
			delete.cleanup(iv_deletePeriod)
			time.sleep(60)
			
	gv_stopPeriodicCleanupConfirm = 1
	return

def checkCard(iv_path): #return: 0 = nichts; 1 = rot; 2 = gelb;
	import Pixel
	
	global gv_newImage
	global gv_checkCardReturn
	
	while (gv_stopCheckCard == 0):
		try:			
			if (gv_newImage == 1):
			
				#print "Pruefe Bild, leite Pixel.py ein"	
				path = getNewest(iv_path) #wird der pixelmethode uebergeben
			
				if (path !=  0):
					returnCard = Pixel.bildauslesen(path)
					if returnCard == 1:
						gv_checkCardReturn = 1
						#elseif (pixelmethode == "gelb":)
						#gv_checkCardReturn = 2	
						break
					else:  
						gv_checkCardReturn = 0
					
				gv_newImage = 0
		
		except IOError:
			returnCard = 0			
		except IndexError:
			returnCard = 0
		

	return #es sollte ja nicht nachdem ein bild geprueft wird gleich aus der methode rausgegangen werden. so wird der thread erst beendet, wenn von aussen ein stopCheckCard kommt

def ueberwachen(iv_path):  #main
	
	import time
	import sys
	import thread
	import Email	 #Email.py
	import Signalton #Signalton.py
	
	
	#Ueberwachungsdauer auslesen
	countmax = getCheckTime()
	
	global gv_stopCheckChange
	global gv_checkChangeReturn	
	global gv_stopCheckChangeConfirm
	global gv_checkCardReturn
	alarmMailSent = 0	
	
	try: 
		thread.start_new_thread(checkChange, (countmax, iv_path, "anfang"))
		thread.start_new_thread(checkCard, (iv_path,))
		thread.start_new_thread(periodicCleanup, (10,))
		
		while True:

			if (gv_checkChangeReturn == 1) and (alarmMailSent == 0): #alarm
				#hier ist der thread fuer checkChange schon durchgelaufen und beendet
				print "--------------- keine bewegung"
				Signalton.output("keineBewegung") #Aufforderung sich zu bewegen
				
				while (gv_stopCheckChangeConfirm == 0):
					pass   #damit der thread auch wirklich beendet ist
								
				thread.start_new_thread(checkChange, (25, iv_path, "keine bewegung")) #1 thread
				#time.sleep(30)
				c = 0
				while (c<=30):
				#	print "t0: "+str(c)
					time.sleep(1)
					if (gv_checkCardReturn == 1):
						break #mail verschicken
					if (gv_checkChangeReturn == 1):
						break #mail verschicken
					else:
						c+=1
					
				if (gv_checkChangeReturn == 1) or (gv_checkCardReturn ==1): #wenn in der Zeit keine Bewegung erfolgt ist
					
					gv_stopCheckChange = 1  #1 thread gestoppt -> 0 threads
					while (gv_stopCheckChangeConfirm == 0):
						pass
										
					Email.sendMail()
					alarmMailSent = 1
					#Signalton.output("mailVersendet")
					
					gv_checkChangeReturn = 0  #hier wird nicht mehr auf bewegung ueberprueft, da bereits ein alarm abgeschickt wurde
				else:
					gv_stopCheckChange = 1
					#print "gv_stopCheckChange = 1"
					while (gv_stopCheckChangeConfirm == 0):
						pass
					
					thread.start_new_thread(checkChange, (countmax, iv_path, "abbruch/anfang"))
			
			#if (gv_checkCardReturn == 2) and (alarmMailSent == 1):  #wenn eine gelbe karte vorgehalten wird, wird der alarm unterbrochen
				#thread.start_new_thread(checkChange, countmax, iv_path)
				#Email.sendMail("Fehlalarm") #todo parameter einfuegen
				#alarmMailSent = 0
					
			#if (gv_checkCardReturn == 1) and (pause = 0): #gelbe Karte bedeutet pausieren
				#if (pause = 0):
					#gv_checkCardReturn = 0
					#gv_stopCheckChange = 1
					#pause = 1
				#else:
					#thread.start_new_thread(checkChange, countmax, iv_path)
					#gv_checkCardReturn = 0
					#pause = 0
			
			if (gv_checkCardReturn == 1) and (alarmMailSent == 0): #rote karte
				print "-------- Rotgefunden"
				#Signalton.output("kontrolle") #muss noch erstellt werden
				if (gv_checkCardReturn == 1):
					Email.sendMail()
					alarmMailSent = 1
				gv_checkCardReturn = 0
				#gv_stopCheckChange = 1
				break #kann spaeter entfernt werden. 				

	except KeyboardInterrupt:
		print ("Programm beendet")
		#Signalton.output("programmBeendet") TODO
		
	except:
		print ("Fehler:" +str(sys.exc_info()[0]))
		#Signalton.output("Fehler") TODO
		raise
		
