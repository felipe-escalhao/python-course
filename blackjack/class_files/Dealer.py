from python_course.blackjack.class_files.abstract.Player import Player


class Dealer(Player):
    def hit(self, deck):
        self.hand.add(deck.draw())

    def show_cards(self):
        cards = ''
        for card in self.hand.cards:
            if card == self.hand.cards[0]:
                cards = cards + f' X-HIDDEN-X,'
            else:
                cards = cards + f' {card},'

        return f'The dealer has the following cards:\n{cards[1:-1]}'

    def deal(self, deck, player, num_cards):
        card_draw = deck.draw(num_cards)
        player.hand.add(card_draw)
