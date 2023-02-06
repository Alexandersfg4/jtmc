import sys
from abc import ABC, abstractmethod


class BaseReader(ABC):
    @abstractmethod
    def get_data(self):
        pass


class StdinReader(BaseReader):
    def get_data(self):
        return sys.stdin.read()


class FileReader(BaseReader):
    def __init__(self, filename):
        self.filename = filename

    def get_data(self):
        with open(self.filename) as file:
            output = file.read()
        return output
