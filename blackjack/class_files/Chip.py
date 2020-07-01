class Chips:
    def __init__(self, chips):
        self.chips = chips
        self.amount = 0

    def __str__(self):
        return f'The player has {self.chips} chips left'

    def bet(self, amount):
        self.amount = amount
        if amount <= self.chips:
            self.chips = self.chips - self.amount
            return False
        else:
            return True

    def win(self):
        self.chips = self.chips + (self.amount * 2)

    def add_chips(self, amount):
        self.chips = self.chips + amount
