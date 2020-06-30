from python_course.blackjack.class_files.abstract.Player import Player


class Customer(Player):

    def hit(self, cards):
        for card in cards:
            self.hand.add(card)
            if card.rank == 'Ace' and not self.ace_value:
                while True:
                    try:
                        ace_value = int(input('Aces can be 1 or 11. Which one do you choose?'))

                        if ace_value == 1 or ace_value == 11:
                            self.hand.ace_value(ace_value)
                            self.ace_value = True
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print('Please, type either 1 or 11')
                        continue

    def show_cards(self):
        cards = ''
        for card in self.hand.cards:
            cards = cards + f' {card},'

        return f'The player has the following cards:\n{cards[1:-1]}'

    def bet(self, amount=0):
        return self.chips.bet(amount)

    def win(self):
        self.chips.win()

    def add_chips(self, amount):
        self.chips.add_chips(amount)
