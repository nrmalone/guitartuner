from gtmath import *
import winsound

def playTuning(type, note, speed):
    if type == "st":
        strings = standardCalc(note)
        for string in strings:
            winsound.Beep(string, speed)
    
    if type == "dr":
        strings = dropCalc(note)
        for string in strings:
            winsound.Beep(string, speed)