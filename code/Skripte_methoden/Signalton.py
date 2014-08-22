#import os

def output(scenario):
    
    import os
    
    if scenario == "keineBewegung":
        os.system("mplayer /srv/seniorscript/soundausgabe/bewegen.wma")
    elif scenario == "motionAktiviert":
        os.system("mplayer /srv/seniorscript/soundausgabe/motionon.wma")
    elif scenario == "motionDeaktiviert":
        os.system("mplayer /srv/seniorscript/soundausgabe/motionoff.wma")
    elif scenario == "ueberwachungAktiviert":
        os.system("mplayer /srv/seniorscript/soundausgabe/ueberwachung.wma")
    elif scenario == "pause":
        os.system("mplayer /srv/seniorscript/soundausgabe/pause.wma")
        