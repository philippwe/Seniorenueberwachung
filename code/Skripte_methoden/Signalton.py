#import os
#import winsound
#winsound.Beep(2500,1000)

#os.system('mpg321 test.mp3 &')

def output(scenario):
    
    import os
    
    if scenario == "keineBewegung":
        os.system("mplayer soundausgabe/bewegen.wma")
    elif scenario == "motionAktiviert":
        os.system("mplayer soundausgabe/motionon.wma")
    elif scenario == "motionDeaktiviert":
        os.system("mplayer soundausgabe/motionoff.wma")
    elif scenario == "ueberwachungAktiviert":
        os.system("mplayer soundausgabe/ueberwachung.wma")
    elif scenario == "pause":
        os.system("mplayer soundausgabe/pause.wma")
        