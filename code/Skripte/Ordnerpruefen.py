import time
import sys
import os

curr_anzahl = 0
anzahl = 0
counter = 0

try:
    while True:
        
        print "Test"
        #Pfad des Ordners angeben, in dem die Fotos von Motion abgespeichert werden
        objects = os.listdir('C:\Users\philipp.wilken\Documents\GitHub\Seniorenueberwachung\code\Skripte')
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
        if counter == 30:
            counter = 0
            os.system("Signalton.py 1")
        
        time.sleep(1)
except KeyboardInterrupt:
    print ("Programm beendet")
    
except:
    print ("Fehler:" +sys.exc_info()[0])
    raise