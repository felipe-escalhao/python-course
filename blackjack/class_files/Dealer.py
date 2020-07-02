from python_course.blackjack.class_files.abstract.Player import Player


class Dealer(Player):
    def hit(self, cards):
        for card in cards:
            self.hand.add(card)

    def show_cards(self, show_all=False):
        cards = ''
        points = 0
        for card in self.hand.cards:
            if card == self.hand.cards[0]:
                cards = f' X-HIDDEN-X,'
                if show_all:
                    cards = f' {card},'
                    points = points + card.rank_value

            else:
                cards = cards + f' {card},'
                points = points + card.rank_value

        print(f'The dealer has the following cards:\n{cards[1:-1]} (Points: {points})')

    def deal(self, num_cards=1):
        return self.deck.draw(num_cards)

    def busted(self):
        return self.hand.check_hand_value() > 21
