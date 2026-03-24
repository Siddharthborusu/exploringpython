# Functions operate on data

# functional programming vs Object/instance oriented programming
#functional - A programming paradigm where computation is done using pure functions that transform data without changing state.
#object oriented -A programming paradigm where programs are built using objects that combine data and behavior (methods).
class TextProcessor:
    def __init__(self, text):
        self.text=text

    def clean_text(self):
        self.text = self.text.strip().lower()
        return self
    
    def remove_punctuation(self):
        self.text= self.text.replace(".", "").replace(",", "")
        return self

# Chain functions together
processor = TextProcessor("Hello,,, WorLD")
result = processor.clean_text().remove_punctuation().text

