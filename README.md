# Guitar Tuner
## Purpose
This project is a simple guitar tuning app built in **Python** that I hope to continually expand upon. In its current state, the goal is for the user to select from several standard or drop tunings and hear it played back to them.
## Structure
This project definitely doesn't follow best practices for OOP, but at least it transcends single dictionary-esque file territory and should be reasonably organized. Each file has its own functionality described below as well as potential for future improvement.<br/>
[gtmath.py](https://github.com/nrmalone/guitartuner/blob/master/gtmath.py) calculates the necessary frequencies to emulate each guitar string in the user's selected tuning. In order to appease the current audio playback solution, calculations accept only integer input and output, causing gradually significant rounding errors for lower frequencies.<br/>
[gtnotation.py](https://github.com/nrmalone/guitartuner/blob/master/gtnotation.py) contains getter functions to retrieve available tunings and notation of each tuning. The application's GUI dynamically displays tunings from this file.<br/>
[gtsound.py](https://github.com/nrmalone/guitartuner/blob/master/gtsound.py) handles all audio playback within the app. Currently, the *winsound* Beep function plays back approximated frequencies of each string since it only accepts integer input, but better audio solutions will be a top priority as long as this project is developed.<br/>
[gtgui.py](https://github.com/nrmalone/guitartuner/blob/master/gtgui.py) creates the program's interface and dictates user input. Early iterations using *tkinter* will appear primitive until a more sophisticated UI is laid out, possibly with turtle.
## Dependencies
To the best of my knowledge, all Python distributions comes with the *winsound* and *tkinter* libraries, so no dependencies are required at the time of writing. Likely dependencies in the future will include *turtle* for a better UI, *sounddevice* to facilitate audio I/O, and other similar libraries that will improve UX. Links to any dependencies will appear here once they are integrated into the project.
