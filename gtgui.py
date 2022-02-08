from gtsound import *
from gtnotation import *
from tkinter import *

#variables for tuning type and speed
type = "st"
speed = 1000
note = 82

#selected vs unselected color
selected = "#5da968"
unselected = "#c94848"

def tuneClick():
    playTuning(type, note, speed)

root = Tk()

standardLabel = Label(root, text="Standard")
standardLabel.grid(row=0,column=0)

dropLabel = Label(root, text="Drop")
dropLabel.grid(row=0,column=1)

tuneButton = Button(root, text="Tune", command=tuneClick)
tuneButton.grid(row=1, column=1)


root.mainloop()