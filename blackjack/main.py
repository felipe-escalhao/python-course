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
    bet = -1

    while bet < 0:
        try:
            bet = int(input('How many chips do you want to bet?'))
            if player.bet(bet):
                print("You don't have enough chips to do this bet. Choose a lower amount.")
                bet = -1
        except ValueError:
            print('Please, choose a number greater than 0')
            continue

    if bet == 0:
        print('Thanks for playing!')
        return

    dealer.hit(dealer.deal(2))
    player.hit(dealer.deal(2))

    dealer.show_cards()
    player.show_cards()

    player_hit(dealer, player)

    if player.hand.check_hand_value() > 21:
        print(f'Player busted and lost {bet} chips')
        return


def player_hit(dealer, player):
    while True:
        hit_answer = (input('Do you want to hit? (yes/no)')).lower()
        if hit_answer == 'yes':
            card = dealer.deal()
            player.hit(card)
        elif hit_answer == 'no':
            break
        else:
            print("Please, choose between yes or no")


def buy_chips(player):
    while True:
        player_answer = input('Do you want to buy chips? (yes/no)').lower()

        if player_answer == 'yes':
            while True:
                try:
                    player_chips = int(input('How many chips do you want to buy?'))

                    if player_chips > 0:
                        player.add_chips(player_chips)
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


if __name__ == '__main__':
    main()
