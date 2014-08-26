'''
Created on 25.08.2014

@author: philipp.wilken
'''
def bildauslesen(iv_path): #Todo: richtigen Pfad uebergeben
    print "Bild pruefen"
    import Image
    import time
    import os
    
    global gv_redcard
    gv_redcard = 0
    
    start = time.clock()
    value = 0
  
    im = Image.open(iv_path)
    pix = im.load()
    zielfarbe = [135,31,30]
    
    
    # Auf Basis des Referenz-RGB-Wert werden Intervalle berechnet.
    zielfarberotmax = zielfarbe[0]+100
    zielfarberotmin = zielfarbe[0]-20
    zielfarbegrunmax = zielfarbe[1]+30
    zielfarbegrunmin = zielfarbe[1]-5
    zielfarbeblaumax = zielfarbe[2]+25
    zielfarbeblaumin = zielfarbe[2]-18
    
    #Damit die berechneten Werte nicht ausserhalb der Gueltigkeit der RGB-Werte liegen, prueft folgende If-Bedingung die Gueltigkeit der Werte
    if zielfarberotmax >255:
        zielfarberotmax = 255
    if zielfarberotmin <0:
        zielfarberotmin = 0
    if zielfarbegrunmax >255:
        zielfarbegrunmax = 255
    if zielfarbegrunmin <0:
        zielfarbegrunmin = 0
    if zielfarbeblaumax > 255:
        zielfarbeblaumax = 255
    if zielfarbeblaumax <0:
        zielfarbeblaumin = 0
    
    
    
    
    z11 =0
    z12=0
    a =0
    currpos_length = 0
    length = im.size[0] #Breite bzw. Laenge des Bilds
    wide = im.size[1]  # Hoehe des Bilds
    
    
    while currpos_length <= length-1:
        currpos_wide=0
        while currpos_wide <= wide-1:
            #print pix[currpos_length,j]
           
            farbe = pix[currpos_length,currpos_wide]
            rot = farbe[0]
            grun= farbe[1]
            blau = farbe[2]
            #farbeermittelt =[rot, grun, blau]
    
            if zielfarberotmin < rot < zielfarberotmax and zielfarbegrunmin < grun < zielfarbegrunmax and zielfarbeblaumin < blau < zielfarbeblaumax:
                print "Treffer"
                z1=currpos_length
                z2=currpos_wide
                z11 =0
                z12=0
                
                while z1 <= currpos_length+60: # Prueft ob in den naechsten 60 Pixeln 30 Treffer sind
                    farbe = pix[z1,z2]
                    rot = farbe[0]
                    grun= farbe[1]
                    blau = farbe[2]
                    #farbeermittelt =[rot, grun, blau]
                    if zielfarberotmin < rot < zielfarberotmax and zielfarbegrunmin < grun < zielfarbegrunmax and zielfarbeblaumin < blau < zielfarbeblaumax:
                       
                        z11 = z11+1
                        if z11 == 30:
                            break
    
                    z1=z1+1
                while z2 < currpos_wide+60:  #Prueft ob in den naechsten 80 Pixeln vertikel 40 Treffer sind.
                    farbe = pix[z1,z2]
                    rot = farbe[0]
                    grun= farbe[1]
                    blau = farbe[2]
                    #farbeermittelt =[rot, grun, blau]
                    if zielfarberotmin < rot < zielfarberotmax and zielfarbegrunmin < grun < zielfarbegrunmax and zielfarbeblaumin < blau < zielfarbeblaumax:
        
                        z12 =z12+1
                        if z12 == 30 and z11 == 30:
                            #print "raus1"
                            break
                   
                 
                    z2 =z2+1
                if z12 == 30 and z11 == 30:
                    #print "raus 2"
                    break
              
    # os.system("Signalton.py 1")
            currpos_wide=currpos_wide+10
        if z12 ==30 and z11 ==30:
            gv_redcard = 1
            print "Wir gehen raus!"
    
            break
        currpos_length=currpos_length+10
    #print im.size
    #print length
    #print a
    #print z12, z11
    #ende = time.clock()
    
    return gv_redcard
    #print "Die Funktion lief %1.2f Sekunden" % (ende - start) 




#________________________TODO: Grenzwerteberechnen: Die berechneten Grenzen koennten ausserhalb des Bildes liegen und einen Laufzeitfehler erzeugen

#def grenzwertberechnen(iv_currpos,iv_wide,iv_length,wideorlength):
    #global grenzwert
    #if wideorlength == 1:
        #distanz=60
    #if wideorlength == 2:
        #distanz = 80
    
    
   # endposition = iv_currpos+distanz
    
   # if wideorlength ==1:
        #if endposition > iv_length:
            #grenzwert = iv_length-iv_currpos
    #if wideorlength ==2:
        #if endposition > iv_wide:
            #grenzwert = iv_wide-iv_currpos
    #return grenzwert