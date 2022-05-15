import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp

class GuitarTuner(Widget):
    pass

class GuitarTunerApp(App):
    def build(self):
        return GuitarTuner()

if __name__ == '__main__':
    GuitarTunerApp().run()