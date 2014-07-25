'''
Created on 25.07.2014

@author: philipp.wilken
'''
from threading import Timer
import os

def email():
    os.system("Email.py 1")

t = Timer(5.00, email)
t.start()
t.