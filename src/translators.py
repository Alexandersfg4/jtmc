from src.readers import BaseReader


class Translator:
    def __init__(self, reader: BaseReader):
        self.reader = reader

    def translate_data(self):
        return self.reader.get_data()
