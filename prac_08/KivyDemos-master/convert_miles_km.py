"""
CP1404 - Practical 08 - 4. Miles to Kilometres Converter
"""
from kivy.app import App
from kivy.lang import Builder

__author__ = 'Ewa Buczkowska'

MILES_TO_KM = 1.60934


class MilesToKmApp(App):
    """ Kivy App for converting miles to kilometres. """

    def build(self):
        """ Build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self):
        """ Handle calculation and update the result label. """
        value = self.validate_input()
        result = value * MILES_TO_KM
        self.root.ids.result_label.text = str(result)

    def handle_increment(self, change):
        """
        Handle up/down button press and update the input value.
        """
        value = self.validate_input() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculation()

    def validate_input(self):
        """
        Convert text input to float, with error handling.
        """
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0


if __name__ == '__main__':
    MilesToKmApp().run()
