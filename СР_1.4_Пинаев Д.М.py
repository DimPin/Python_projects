from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

class MyApp(App):
    def __init__(self):
        super().__init__()
        self.label = Label(text='')
        self.input_data = TextInput(hint_text='Bведите название файла')
        self.input_data2 = TextInput(hint_text='Введите текст файла')
        self.button = Button(text='Open file')
        self.button2 = Button(text='Create file')
        self.button3 = Button(text='Write to file')
        self.button.bind(on_press=self.open)
        self.button2.bind(on_press=self.create)
        self.button3.bind(on_press=self.write)

def open(self, *args):
    name = self.input_data.text
    try:
        f = open(name, 'r')
        t = f.read()
        if t != "":
            self.label.text = str(t)
        else:
            self.label.text = str("Empty")
        f.close()
    except:
        self.label.text = str("no such file")