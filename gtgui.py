from gtsound import *
from gtnotation import *
import tkinter as tk

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

window = tk.Tk()
window.title("Simple Guitar Tuner")
window.configure(bg='#898989')
window.iconbitmap('./assets/icon.ico')

standardLabel = tk.Label(window, text="Standard")
standardLabel.grid(row=0,column=0)
for i in getPossibleTunings("st"):
    tk.Radiobutton(window, text=[i], variable=tuning, value=[i]).grid(row=getPossibleTunings("st").index(i)+1, column=0)

dropLabel = tk.Label(window, text="Drop")
dropLabel.grid(row=0,column=1)
for i in getPossibleTunings("dr"):
    tk.Radiobutton(window, text=[i], variable=tuning, value=[i]).grid(row=getPossibleTunings("dr").index(i)+1, column=1)

tuneButton = tk.Button(window, text="Tune", command=tuneClick)
tuneButton.grid(row=0, column=3)


window.mainloop()