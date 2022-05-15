from gtmath import *
import winsound
#from subprocess import call

def playTuning(tuning, duration, volume):
    #call(["amixer", "-D", "pulse", "sset", "Master", str(volume)+"%"])
    if "Standard" in tuning:
        strings = standardCalc(tuning[:2].strip())
        for string in strings:
            winsound.Beep(string, duration)
    
    if "Drop" in tuning:
        strings = dropCalc(tuning[-2:].strip())
        for string in strings:
            winsound.Beep(string, duration)
