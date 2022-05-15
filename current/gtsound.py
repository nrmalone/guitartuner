from gtmath import *
import winsound

def playTuning(tuning, speed):
    if "Standard" in tuning:
        strings = standardCalc(tuning[:2].strip())
        for string in strings:
            winsound.Beep(string, speed)
    
    if "Drop" in tuning:
        strings = dropCalc(tuning[-2:].strip())
        for string in strings:
            winsound.Beep(string, speed)