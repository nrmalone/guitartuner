import tkinter as tk
import gttunings
import gtsound

window = tk.Tk()
window.title("Simple Guitar Tuner")
window.geometry("640x480")
window.resizable(False, False)
window.configure(bg='#898989')
window.iconbitmap('./assets/icon.ico')

def tuneClick():
    gtsound.playTuning(tuningSelection.get(), speed=1000) #TODO: Implement speed slider

tuningSelectionLabel = tk.Label(window, text="Select Tuning:")
tuningSelectionLabel.grid(row=0,column=0)

tuningRow = 1
tuningSelection = tk.StringVar(window, "E Standard")
for (text, value) in gttunings.possibleTunings.items():
    tk.Radiobutton(window, text = text, variable = tuningSelection,
                value = value, indicator = 0,
                background = "#afafaf").grid(row=tuningRow, column=0)
    tuningRow += 1

button = tk.Button(window, text = "Tune", command = tuneClick).grid(row=0,column=2)

window.mainloop()