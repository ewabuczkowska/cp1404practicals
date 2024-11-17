from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Kivy app demo box layouts."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Print greeting."""
        # print('greet')
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clear the box."""
        self.root.ids.output_label.text = ''
        self.root.ids.input_name.text = 'Enter your name'


BoxLayoutDemo().run()
