from abc import ABC, abstractmethod


class BaseStdout(ABC):
    @abstractmethod
    def print(self):
        pass


class ConsoleStdout(BaseStdout):
    def __init__(self, models: dict):
        self.models = models

    def print(self):
        for key, value in self.models.items():
            print(key)
            print("\n".join(value), end='\n\n')
