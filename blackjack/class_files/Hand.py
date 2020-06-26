_values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Hand:
    def __init__(self):
        self.cards = []
        self.hand_value = 0

    def add(self, card_draw):
        for card in card_draw:
            self.cards.append(card)

    def check_hand_value(self):
        self.hand_value = 0
        for card in self.cards:
            self.hand_value = self.hand_value + _values.get(card.card)

        return self.hand_value
