#ejercicio 1

from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.label import Label
class MyApp (App):
    def build(self):
        return Label (text='Hola Mundo')
    
if __name__ == "__main__" :
    MyApp().run()