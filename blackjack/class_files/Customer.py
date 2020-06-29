from python_course.blackjack.class_files.abstract.Player import Player


class Customer(Player):
    def hit(self, deck):
        while True:
            hit_answer = (input('Do you want to hit? (yes/no)')).lower()
            if hit_answer == 'yes':
                card = deck.draw()
                if card.rank == 'Ace':
                    self.hand.ace_value()
                self.hand.add(card)

            elif hit_answer == 'no':
                print("Dealer's turn")
                break
            else:
                print("Please, choose between yes or no")

    def show_cards(self):
        cards = ''
        for card in self.hand.cards:
            cards = cards + f' {card},'

        return f'The player has the following cards:\n{cards[1:-1]}'

    def bet(self, amount=0):
        return self.chips.bet(amount)

    def win(self):
        self.chips.win()
