from python_course.blackjack.class_files.abstract.Player import Player


class Customer(Player):

    def hit(self, cards):
        for card in cards:
            self.hand.add(card)
            if card.rank == 'Ace' and not self.ace_value:
                while True:
                    try:
                        ace_value = int(input('Aces can be 1 or 11. Which one do you choose? Answer: '))

                        if ace_value == 1 or ace_value == 11:
                            card.ace_value(ace_value)
                            self.ace_value = True
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print('Please, type either 1 or 11')
                        continue

    def show_cards(self, show_all=False):
        cards = ''
        points = 0
        for card in self.hand.cards:
            cards = cards + f' {card},'
            points = points + card.rank_value

        print(f'The player has the following cards:\n{cards[1:-1]} (Points: {points})')

    def do_bet(self):
        return self.chips.bet(self.bet)

    def win(self):
        self.chips.win()

    def add_chips(self, amount):
        self.chips.add_chips(amount)

    def busted(self):
        return self.hand.check_hand_value() > 21

    def clear(self):
        self.bet = -1
        self.hand.clear()
