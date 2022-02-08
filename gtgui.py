from gtsound import *
from gtnotation import *
from tkinter import *

#variables for tuning type and speed
type = "st"
speed = 1000
note = 82
tuning = "E Standard"

#selected vs unselected color
selected = "#5da968"
unselected = "#c94848"

def tuneClick():
    playTuning(type, note, speed)

root = Tk()
root.title("Simple Guitar Tuner")
root.iconbitmap('./assets/icon.ico')

standardLabel = Label(root, text="Standard")
standardLabel.grid(row=0,column=0)
for i in getPossibleTunings("st"):
    Radiobutton(root, text=[i], variable=tuning, value=[i]).grid(row=getPossibleTunings("st").index(i)+1, column=0)

dropLabel = Label(root, text="Drop")
dropLabel.grid(row=0,column=1)
for i in getPossibleTunings("dr"):
    Radiobutton(root, text=[i], variable=tuning, value=[i]).grid(row=getPossibleTunings("dr").index(i)+1, column=1)

tuneButton = Button(root, text="Tune", command=tuneClick)
tuneButton.grid(row=0, column=3)


root.mainloop()