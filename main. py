# ============================================================
# SUPERIOR SOLOMON SCIENTIFIC CALCULATOR
# ============================================================
# Copyright © 2026 SiyomaCodingPrograms
# ============================================================

import math

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorLayout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.display = TextInput(
            text="",
            readonly=True,
            halign="right",
            font_size=32,
            size_hint_y=0.22
        )

        self.add_widget(self.display)

        buttons = [
            ["C", "⌫", "(", ")"],
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["√", "x²", "xʸ", "!"],
            ["sin", "cos", "tan", "π"],
        ]

        grid = GridLayout(
            cols=4,
            spacing=5,
            padding=5
        )

        for row in buttons:
            for text in row:
                button = Button(
                    text=text,
                    font_size=22
                )
                button.bind(on_press=self.button_pressed)
                grid.add_widget(button)

        self.add_widget(grid)

    def button_pressed(self, instance):
        value = instance.text

        if value == "C":
            self.display.text = ""

        elif value == "⌫":
            self.display.text = self.display.text[:-1]

        elif value == "=":
            self.calculate()

        elif value == "√":
            self.display.text += "sqrt("

        elif value == "x²":
            self.display.text += "**2"

        elif value == "xʸ":
            self.display.text += "**"

        elif value == "!":
            self.display.text += "!"

        elif value == "×":
            self.display.text += "*"

        elif value == "÷":
            self.display.text += "/"

        elif value == "π":
            self.display.text += "pi"

        elif value == "sin":
            self.display.text += "sin("

        elif value == "cos":
            self.display.text += "cos("

        elif value == "tan":
            self.display.text += "tan("

        else:
            self.display.text += value

    def calculate(self):
        expression = self.display.text

        try:
            while "!" in expression:
                import re

                match = re.search(r"(\d+)!$", expression)

                if not match:
                    raise ValueError("Invalid factorial")

                number = int(match.group(1))

                expression = (
                    expression[:match.start()]
                    + str(math.factorial(number))
                )

            allowed = {
                "sqrt": math.sqrt,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "pi": math.pi,
            }

            result = eval(
                expression,
                {"__builtins__": {}},
                allowed
            )

            if isinstance(result, float) and result.is_integer():
                result = int(result)

            self.display.text = str(result)

        except Exception:
            self.display.text = "Error"


class SuperiorSolomonCalculator(App):

    def build(self):
        self.title = "Superior Solomon Scientific Calculator"
        return CalculatorLayout()


if __name__ == "__main__":
    SuperiorSolomonCalculator().run()
