"""
Mediator pattern implementation for game object communication.

This module implements the Mediator design pattern, allowing game objects
to communicate with each other without direct references. Objects notify
the mediator of events, and the mediator can coordinate responses.
"""

# Mediator
class Mediator():
    """
    Central communication hub for game objects.
    
    The Mediator class implements the Mediator design pattern, providing
    a centralized way for game objects to communicate. Objects send
    notification messages to the mediator, which can then coordinate
    responses or log events. This reduces coupling between game objects.
    
    Attributes:
        message (str): Current notification message.
    """

    def __init__(self) -> None:
        self.message = "Mediator was created."
        self.print_message()

    def notify(self, message):
        """
        Receive a notification message from a game object.
        
        Stores the message and prints it to the console. This method
        is called by game objects to communicate events or state changes.
        
        Args:
            message (str): Notification message from a game object.
        """
        self.message = message
        self.print_message()

    def print_message(self):
        """
        Print the current message to the console.
        
        Outputs the stored message to stdout for debugging and logging.
        """
        print(self.message)
