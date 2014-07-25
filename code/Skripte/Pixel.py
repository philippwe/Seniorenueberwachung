import Image
import time
import os
start = time.clock()
value = 0
im = Image.open("philipp.jpg")
pix = im.load()
zielfarbe = [135,31,30]



zielfarberotmax = zielfarbe[0]+20
zielfarberotmin = zielfarbe[0]-20
zielfarbegrunmax = zielfarbe[1]+20
zielfarbegrunmin = zielfarbe[1]-20
zielfarbeblaumax = zielfarbe[2]+20
zielfarbeblaumin = zielfarbe[2]-20

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
#print zielfarberotmax, zielfarberotmin, zielfarbegrunmax, zielfarbegrunmin, zielfarbeblaumax, zielfarbeblaumin



z11 =0
z12=0
a =0
length = im.size[0]
wide = im.size[1]
currpos_length = 0

while currpos_length <= length-1:
    j=0
    while j <= wide-1:
        #print pix[currpos_length,j]
       
        farbe = pix[currpos_length,j]
        rot = farbe[0]
        grun= farbe[1]
        blau = farbe[2]
        farbeermittelt =[rot, grun, blau]

        if zielfarberotmin < rot < zielfarberotmax and zielfarbegrunmin < grun < zielfarbegrunmax and zielfarbeblaumin < blau < zielfarbeblaumax:
            #print "Treffer"
            z1=currpos_length
            z2=j
            z11 =0
            z12=0
            while z1 <= currpos_length+60:
                farbe = pix[z1,z2]
                rot = farbe[0]
                grun= farbe[1]
                blau = farbe[2]
                farbeermittelt =[rot, grun, blau]
                if zielfarberotmin < rot < zielfarberotmax and zielfarbegrunmin < grun < zielfarbegrunmax and zielfarbeblaumin < blau < zielfarbeblaumax:
                   
                    z11 = z11+1
                    if z11 == 30:
                        break

                z1=z1+1
            while z2 < j+80:
                farbe = pix[z1,z2]
                rot = farbe[0]
                grun= farbe[1]
                blau = farbe[2]
                farbeermittelt =[rot, grun, blau]
                if zielfarberotmin < rot < zielfarberotmax and zielfarbegrunmin < grun < zielfarbegrunmax and zielfarbeblaumin < blau < zielfarbeblaumax:
    
                    z12 =z12+1
                    if z12 == 40:
                        break
               
             
                z2 =z2+1
            if z12 == 40 and z11 == 30:
                break
            a= a+1
# os.system("Signalton.py 1")
        j=j+10
    if z12 ==40 and z11 ==30:
       # print "Wir gehen raus!"
        #os.system("Signalton.py 1")
        break
    currpos_length=currpos_length+10
#print im.size
#print length
#print a
#print z12, z11
ende = time.clock()
print "Die Funktion lief %1.2f Sekunden" % (ende - start) 
