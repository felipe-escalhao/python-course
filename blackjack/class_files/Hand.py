class Hand:
    def __init__(self):
        self.cards = []
        self.hand_value = 0

    def add(self, card):
        self.cards.append(card)

    def check_hand_value(self):
        self.hand_value = 0
        for card in self.cards:
            self.hand_value = self.hand_value + card.rank_value

        return self.hand_value

    def clear(self):
        self.cards = []
