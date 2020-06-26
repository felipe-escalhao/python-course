from python_course.blackjack.class_files.Deck import Deck
from python_course.blackjack.class_files.Dealer import Dealer
from python_course.blackjack.class_files.Customer import Customer
import math


def main():
    player_chips = -1

    while player_chips <= 0:
        try:
            player_chips = int(input('How many chips do you want to buy?'))
            deck = Deck()
            player = Customer(player_chips)
            deck.shuffle(True)
            play(deck, player)
        except ValueError:
            print('Please, choose a number greater than 0')
            continue


def play(deck, player):

    dealer = Dealer()
    bet = 0

    while bet <= 0:
        try:
            bet = int(input('How many chips do you want to bet?'))
            if player.bet(bet):
                print("You don't have enough chips to do this bet. Choose a lower amount.")
                bet = 0
        except ValueError:
            print('Please, choose a number greater than 0')
            continue

    dealer.deal(deck, dealer, 2)
    dealer.deal(deck, player, 2)

    dealer.show_cards()
    player.show_cards()


if __name__ == '__main__':
    main()
