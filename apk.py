from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random

class RandomNumberGeneratorApp(App):
    def build(self):
        self.title = 'Generatore di Numeri Casuali'

        # Crea un layout verticale
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Crea un'etichetta per mostrare il numero
        self.label = Label(text='Premi il pulsante per generare un numero', font_size='20sp')
        layout.add_widget(self.label)

        # Crea un pulsante per generare il numero
        button = Button(text='Genera Numero', font_size='20sp', size_hint=(1, 0.5))
        button.bind(on_press=self.generate_random_number)
        layout.add_widget(button)

        return layout

    def generate_random_number(self, instance):
        # Genera un numero casuale da 1 a 10
        random_number = random.randint(1, 10)
        self.label.text = f'Numero generato: {random_number}'

if __name__ == '__main__':
    RandomNumberGeneratorApp().run()
