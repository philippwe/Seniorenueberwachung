import smtplib

import time

absender = "pwilken@web.de"
adressat ="philipp.wilken@accenture.com"
betreff = "test"
inhalt = "Hallo , ich bin Pi"
zeit = time.ctime(time.time())

server = smtplib.SMTP("smtp.web.de", 587)
server.set_debuglevel(1)

server.starttls()
server = smtplib.SMTP("smtp.web.de")
server.login("pwilken", ".")

server.sendmail("pwilken@web.de", "pwilken@web.de", "test from Pi")


server.quit()