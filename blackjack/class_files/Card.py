class Card:
    def __init__(self, rank, card):
        self.rank = rank
        self.card = card

    def __str__(self):
        return f'{self.card} of {self.rank}'
