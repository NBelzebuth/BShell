from rich.console import Console

console = Console()

class option:

    def __init__(self, text : str, is_input = False, is_selected = False):
        self.text = text
        self.is_input = is_input
        self.is_selected = is_selected

    def select(self):
        self.is_selected = not self.is_selected

    def is_selcted(self):
        return self.is_selected
        
    def print(self):
        if self.is_selected == False:
            return f"[red][bold][ ][/][/] {self.text}"
        if self.is_selected == True:
            return f"[red][bold][>][/][/] {self.text}"

color = option("color : 0f", True, True)

console.print(color.print(), True)

