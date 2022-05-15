import tkinter as tk
import gttunings
import gtsound

speed = 1000 #ms

window = tk.Tk()
window.geometry("640x480")
window.configure(bg='#898989')

def tuneClick():
    gtsound.playTuning(tuningSelection.get(), speed)

tuningSelection = tk.StringVar(window, "E Standard")


for (text, value) in gttunings.possibleTunings.items():
    tk.Radiobutton(window, text = text, variable = tuningSelection,
                value = value, indicator = 0,
                background = "#afafaf").pack()

button = tk.Button(window, text = "Tune", command = tuneClick).pack()

window.mainloop()