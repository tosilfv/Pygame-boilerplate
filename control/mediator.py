# Mediator
class Mediator():

    def __init__(self) -> None:
        self.message = "Mediator was created."
        self.print_message()

    def notify(self, message):
        self.message = message
        self.print_message()

    def print_message(self):
        print(self.message)
