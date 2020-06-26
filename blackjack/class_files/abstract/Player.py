from python_course.blackjack.class_files.Hand import Hand
from python_course.blackjack.class_files.Chip import Chips


class Player:
    def __init__(self, chips=0):
        self.chips = Chips(chips)
        self.hand = Hand()

    def hit(self, deck):
        raise NotImplementedError("Subclass must implement this abstract method")

    def show_cards(self):
        raise NotImplementedError("Subclass must implement this abstract method")