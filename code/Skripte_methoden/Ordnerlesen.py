#def getNewest(p):

import os
import glob

#path = "C:\Users\d056973\Downloads"

newest = max(glob.iglob("*.*"), key = os.path.getctime)

print newest