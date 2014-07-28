def userInput():
	
	print "1"
	action = input("Was soll gemacht werden? ")
	#0-nichts   -> keine rote Karte
	#1-pause	-> rote Karte: 
	#					evtl. default Wert von 2h
	#					/ pause bis karte erneut gezeigt wird
	
	if action==0:
		return 0
	else:
		dauer = input("Fuer wie lange soll pausiert werden (Sekunden)? ")
		return dauer

def timer(n):
	print "timer"
	import time 

	time.sleep(n)
	return "0"

