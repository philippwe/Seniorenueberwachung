def getRecipient():
	pass #todo

def getName():
	pass #todo

def sendMail():

	import smtplib
	from email.mime.image import MIMEImage
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
		
	i=0
	s = []
	COMMASPACE = ","
	
	fobj = open ("/var/www/Konfiguration.txt" , 'r') 
	for line in fobj: 
		s.append(line)
		print s[i
	]
		i= i+1    
	fobj.close()
		
	print "Email-Skript starten"
	adressat = s[2:i]
	# ["pwilken@web.de", "philipp.wilken@accenture.com"]
	inhalt = "Hallo, das Ueberwachungssystem von "+ s[0]+" hat einen Alarm ausgeloest. Bitte kontaktieren Sie "+ s[0] +" sofort!"
	
	msg = MIMEMultipart()
	msg["Subject"] = "Alarm bei " + s[0]
	msg["From"]= "ueberwachungraspberry@gmail.com"
	msg["To"]= COMMASPACE.join(adressat) 
	emailinhalt = MIMEText(inhalt, "plain")
	msg.attach(emailinhalt)
	
	print "Port setzen"
	server = smtplib.SMTP("smtp.gmail.com", 587)
	
	print "Verschluesselung"
	server.starttls()
	
	print "anmelden"
	server.login("ueberwachungraspberry", "RaspPJN14") #Darauf achten das das Passwort beim Commit raus ist!!!
	
	print "Email verschicken"
	server.sendmail("ueberwachungraspberry@gmail.com", adressat, msg.as_string())
	
	print "Serververbindung schliessen"
	server.quit()
