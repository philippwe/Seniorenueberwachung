import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

COMMASPACE = ","

print "Email-Skript starten"
adressat = ["pwilken@web.de", "philipp.wilken@accenture.com"]
inhalt = "Hallo, das Ueberwachungssystem hat einen Alarm ausgeloest. Bitte kontaktieren Sie sofort die ueberwachte Person!"

msg = MIMEMultipart()
msg["Subject"] = "Alarm"
msg["From"]= "ueberwachungraspberry@gmail.com"
msg["To"]= COMMASPACE.join(adressat) 
emailinhalt = MIMEText(inhalt, "plain")
msg.attach(emailinhalt)

print "Port setzen"
server = smtplib.SMTP("smtp.gmail.com", 587)

print "Verschluesselung"
server.starttls()

print "anmelden"
server.login("ueberwachungraspberry", "xxxPasswort siehe Dokuxxx") #Darauf achten das das Passwort beim Commit raus ist!!!

print "Email verschicken"
server.sendmail("ueberwachungraspberry@gmail.com", adressat, msg.as_string())

print "Serververbindung schliessen"
server.quit()
