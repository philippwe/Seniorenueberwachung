'''
Created on 25.07.2014

@author: philipp.wilken
'''
import os
import datetime
import time
#time.struct_time() = datetime.datetime.today()
monat = time.localtime()[1]
jahr = time.localtime()[0]
print monat+jahr
#os.remove(path)