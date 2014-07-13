import Image
import os
value = 0
im = Image.open("Tulips.jpg")
pix = im.load()
zielfrabe = [150,199,255]
length = im.size[0]
wide = im.size[1]
i = 1
j=1
while i <= 1024:
    while j <= 768:
        print pix[i,j]

        farbe = pix[i,j]
        rot = farbe[0]
        grun= farbe[1]
        blau = farbe[2]
        farbeermittelt =[rot, grun, blau]
        if zielfrabe == farbeermittelt:
            print "Treffer"
            os.system("Signalton.py 1")
        j=j+1
    i=i+1
print im.size
print length

