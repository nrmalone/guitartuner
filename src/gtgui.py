from ctypes import alignment
import tkinter as tk
import gttunings
import gtsound

window = tk.Tk()
window.title("Simple Guitar Tuner")
window.resizable(False, False)
window.configure(bg='#1d1d1d')
window.iconbitmap('./assets/icon.ico')

def tuneClick():
    gtsound.playTuning(tuningSelection.get(), duration=durationSlider.get(), volume=volumeSlider.get()) #TODO: Implement duration/speed & volume sliders

#header
welcomeLabel = tk.Label(window, text="Welcome to Simple Guitar Tuner!", font=("Arial", 16))
welcomeLabel.configure(bg='#1d1d1d', fg='#dbdbdb')
welcomeLabel.grid(row=0,column=0,columnspan=3)
instructionLabel = tk.Label(window,
                            text="Instructions:\n1. Select tuning, duration, & volume.\n2. Press Tune button to hear that tuning.\n*Wait for the tuner to finish before making another selection",
                            font=("Arial", 10))
instructionLabel.configure(bg='#1d1d1d', fg='#dbdbdb')
instructionLabel.grid(row=1,column=0,columnspan=3,ipady=5)

#left column: tuning selection
tuningSelectionLabel = tk.Label(window, text="Select Tuning:")
tuningSelectionLabel.configure(bg='#1d1d1d', fg='#dbdbdb')
tuningSelectionLabel.grid(row=3,column=0)
tuningSelection = tk.StringVar(window, "E Standard")
tuningRow = 4
for (text, value) in gttunings.possibleTunings.items():
    tk.Radiobutton(window, text = text, variable = tuningSelection,
                value = value, indicator = 0,
                background = "#a5a5a5", foreground='#000000').grid(row=tuningRow, column=0,sticky="ew")
    tuningRow += 1

#middle column: duration slider
durationSliderLabel = tk.Label(window, text="Duration (ms):")
durationSliderLabel.configure(bg='#1d1d1d', fg='#dbdbdb')
durationSliderLabel.grid(row=4,column=1,sticky="EW")
durationSlider = tk.Scale(window, from_=2500, to=250)
durationSlider.configure(sliderrelief='raised', highlightbackground='#1d1d1d', bg='#1d1d1d', fg='#dbdbdb', cursor='double_arrow', resolution=10)
durationSlider.set(1000)
durationSlider.grid(row=5,column=1,rowspan=tuningRow,sticky="NS")

#right column: tune button & volume slider
tuneButton = tk.Button(window, text = "Tune", font=("Arial", 14), command = tuneClick)
tuneButton.configure(bg='#a5a5a5', fg='#000000', cursor='exchange')
tuneButton.grid(row=2,column=2,rowspan=2)

volumeSliderLabel = tk.Label(window, text="Volume:")
volumeSliderLabel.configure(bg='#1d1d1d', fg='#dbdbdb')
volumeSliderLabel.grid(row=4,column=2,sticky="EW")
volumeSlider = tk.Scale(window, from_=100, to=0)
volumeSlider.configure(sliderrelief='raised', highlightbackground='#1d1d1d', bg='#1d1d1d', fg='#dbdbdb', cursor='double_arrow', resolution=1)
volumeSlider.set(100)
volumeSlider.grid(row=5,column=2,rowspan=tuningRow,sticky="NS")

window.mainloop()