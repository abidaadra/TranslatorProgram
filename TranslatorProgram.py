#importing from google translate data
from googletrans import Translator

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


translator = Translator()


class MyGrid(GridLayout):
    def __init__(self, **arg):

        super(MyGrid, self).__init__(**arg)

        self.cols = 1

        self.inside_grid = GridLayout(cols=2)

        self.input = TextInput(multiline=False, hint_text="Write Text Here",font_size=30)
        self.inside_grid.add_widget(self.input)

        self.button = Button(text="Translate", font_size=40)
        self.button.bind(on_press=self.translate)
        self.inside_grid.add_widget(self.button)

        self.add_widget(self.inside_grid)

        self.output = Button(text='', font_size=40)
        self.add_widget(self.output)


    def translate(self, instance):
        input_text = self.input.text
		
		#you can change the destination language here example dest='de' de is german
        translation = translator.translate(input_text, dest='en').text
        self.output.text = translation


class MyApp(App):
    def build(self):
        return MyGrid()


MyApp().run()
