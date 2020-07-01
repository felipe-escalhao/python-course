from python_course.blackjack.class_files.Deck import Deck
from python_course.blackjack.class_files.Dealer import Dealer
from python_course.blackjack.class_files.Customer import Customer


def main():

    print('Welcome to blackjack!')
    player = None

    while True:
        player_answer = input('Do you want to play? (yes/no)').lower()
        if player_answer == 'yes':
            player = Customer()
            buy_chips(player)
            break
        elif player_answer == 'no':
            print('Please, choose between yes or no')
            break
        else:
            print('Please, choose between yes or no')

    if player is not None:
        play(player)

        while True:
            keep_playing = input('Do you want to keep playing? (yes/no)')
            if keep_playing == 'yes':
                buy_chips(player)
                if player.chips.chips == 0:
                    print('You need to buy chips to keep playing!')
                else:
                    play(player)
            elif player_answer == 'no':
                break
            else:
                print('Please, choose between yes or no')


def play(player):

    dealer = Dealer(deck=Deck())

    while player.bet < 0:
        try:
            player.bet = int(input('How many chips do you want to bet?'))
            if player.do_bet():
                print("You don't have enough chips to do this bet. Choose a lower amount.")
                player.bet = -1
        except ValueError:
            print('Please, choose a number greater than 0')
            continue

    first_deal(dealer, player)
    if busted(player):
        return

    player_hit(dealer, player)
    if busted(player):
        return

    print('OK')


def player_hit(dealer, player):
    while True:
        hit_answer = (input('Do you want to hit? (yes/no)')).lower()
        if hit_answer == 'yes':
            card = dealer.deal()
            player.hit(card)
            player.show_cards()
            if player.busted():
                break
        elif hit_answer == 'no':
            break
        else:
            print("Please, choose between yes or no")


def dealer_hit(dealer):
    while True:
        card = dealer.deal()
        dealer.hit(card)
        dealer.show_cards(True)
        # CONTINUA AQUI


def buy_chips(player):
    while True:
        player_answer = input('Do you want to buy chips? (yes/no)').lower()

        if player_answer == 'yes':
            while True:
                try:
                    player_chips = int(input('How many chips do you want to buy?'))

                    if player_chips > 0:
                        player.add_chips(player_chips)
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print('Please, choose a number greater than 0')
                    continue
            break
        elif player_answer == 'no':
            break
        else:
            print('Please, choose between yes or no')


def first_deal(dealer, player):
    dealer.hit(dealer.deal(2))
    player.hit(dealer.deal(2))

    dealer.show_cards()
    player.show_cards()


def busted(player):
    if player.busted():
        print(f'Player busted and lost {player.bet} chips')


if __name__ == '__main__':
    main()
