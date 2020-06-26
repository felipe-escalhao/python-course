from python_course.blackjack.class_files.abstract.Player import Player


class Customer(Player):
    def hit(self, deck):
        self.hand.add(deck.draw())

    def show_cards(self):
        cards = ''
        for card in self.hand.cards:
            cards = cards + f' {card},'

        return f'The player has the following cards:\n{cards[1:-1]}'

    def bet(self, amount=0):
        self.chips.bet(amount)

    def win(self):
        self.chips.win()
