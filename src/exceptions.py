

class ArgumentNotFoundError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(f"Argument {self.message} is absent")
