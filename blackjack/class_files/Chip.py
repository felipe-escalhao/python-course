class Chips:
    def __init__(self, chips):
        self.chips = chips
        self.amount = 0

    def __str__(self):
        return f'The player has {self.chips} chips left'

    def bet(self, amount):
        self.amount = amount
        if amount < self.chips:
            return True
        else:
            self.chips = self.chips - self.amount
            return False

    def win(self):
        self.chips = self.chips + (self.amount * 2)
