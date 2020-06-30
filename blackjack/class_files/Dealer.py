from python_course.blackjack.class_files.abstract.Player import Player


class Dealer(Player):
    def hit(self, cards):
        for card in cards:
            self.hand.add(card)

    def show_cards(self):
        cards = ''
        for card in self.hand.cards:
            if card == self.hand.cards[0]:
                cards = cards + f' X-HIDDEN-X,'
            else:
                cards = cards + f' {card},'

        return f'The dealer has the following cards:\n{cards[1:-1]}'

    def deal(self, num_cards=1):
        return self.deck.draw(num_cards)
