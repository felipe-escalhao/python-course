from python_course.blackjack.class_files.Hand import Hand
from python_course.blackjack.class_files.Chip import Chips


class Player:
    def __init__(self, chips=0, deck=None):
        self.chips = Chips(chips)
        self.hand = Hand()
        self.deck = deck
        self.ace_value = False
        self.bet = -1

    def hit(self, cards):
        raise NotImplementedError("Subclass must implement this abstract method")

    def show_cards(self, show_all):
        raise NotImplementedError("Subclass must implement this abstract method")

    def busted(self):
        raise NotImplementedError("Subclass must implement this abstract method")