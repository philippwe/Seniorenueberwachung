def cleanup(iv_period):   
#fuer Werte zwischen 0 und 60
    import glob
    import os
    import time

    year = time.localtime()[0]
    month = time.localtime()[1]
    day = time.localtime()[2]
    hour = time.localtime()[3]
    minute = time.localtime()[4]

    if minute>=iv_period:
        minute = minute-iv_period
    else:
        minute = minute+(60-iv_period)
        if hour>=1:
            hour = hour-1
        else:
            hour = 23
            if day>=1:
                day = day-1
            else:
                if (month-1)==0:
                    #31tage
                        day = 31
                elif (month-1)==1:
                    #31tage
                        day = 31
                elif (month-1)==2:
                        if (year % 4)==0:
                            day = 29
                        else:
                            day = 28
                        #schaltjahre!!!
                elif (month-1)==3:
                        day = 31
                elif (month-1)==4:
                        day = 30
                elif (month-1)==5:
                        day = 31
                elif (month-1)==6:
                        day = 30
                elif (month-1)==7:
                        day = 31
                elif (month-1)==8:
                        day = 31
                elif (month-1)==9:
                        day = 30
                elif (month-1)==10:
                        day = 31
                elif (month-1)==11:  
                        day = 30  
                if month>=1:
                    month = month-1
                else: 
                    month = 12
                    year = year-1
    
    year = str(year)
    month = str(month)
    if len(month)==1:
        month = "0"+month
    day = str(day)
    if len(day)==1:
        day = "0"+day    
    hour = str(hour)    
    if len(hour)==1:
        hour = "0"+hour
    minute = str(minute)
    if len(minute)==1:
        hour = "0"+minute
    
    pfad = "/srv/motion/*"+year+month+day+hour+minute+"*"
    
    print pfad #TODO entfernen
    
    for fl in glob.glob(pfad):
        os.remove(fl)
        
def cleanAll(pfad):
    import glob
    import os
    for fl in glob.glob(pfad+"*.jpg"):
    #Do what you want with the file
        os.remove(fl)
