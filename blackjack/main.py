import os
from python_course.blackjack.class_files.Deck import Deck
from python_course.blackjack.class_files.Dealer import Dealer
from python_course.blackjack.class_files.Customer import Customer


def main():

    print('Welcome to blackjack!')
    player = None

    while True:
        player_answer = input('Do you want to play? (yes/no) Answer: ').lower()
        if player_answer == 'yes':
            player = Customer()
            buy_chips(player)
            break
        elif player_answer == 'no':
            print('Bye!')
            break
        else:
            print('Please, choose between yes or no')

    if player is not None:
        play(player)

        while True:
            keep_playing = input('Do you want to keep playing? (yes/no) Answer: ').lower()
            if keep_playing == 'yes':
                clear_screen()
                buy_chips(player)
                if player.chips.chips == 0:
                    print('You need to buy chips to keep playing!')
                else:
                    play(player)
            elif keep_playing == 'no':
                print('Bye!')
                break
            else:
                print('Please, choose between yes or no')


def play(player):

    dealer = Dealer(deck=Deck())

    while player.bet < 0:
        try:
            player.bet = int(input('How many chips do you want to bet? Answer: '))
            if player.do_bet():
                print("You don't have enough chips to do this bet. Choose a lower amount.")
                player.bet = -1
        except ValueError:
            print('Please, choose a number greater than 0')
            continue

    if player.bet == 0:
        print("You can't bet zero chips")
        return

    first_deal(dealer, player)
    if player.busted():
        print(f'Player busted and lost {player.bet} chips')
        player.clear()
        return

    player_hit(dealer, player)
    if player.busted():
        print(f'Player busted and lost {player.bet} chips')
        player.clear()
        return
    else:
        dealer_hit(dealer)
        check_winner(dealer, player)
        player.clear()


def player_hit(dealer, player):
    while True:
        hit_answer = (input('Do you want to hit? (yes/no) Answer: ')).lower()
        if hit_answer == 'yes':
            card = dealer.deal()
            player.hit(card)
            player.show_cards()
            if player.busted():
                break
        elif hit_answer == 'no':
            print(f'Player stands with {player.hand.check_hand_value()} points')
            break
        else:
            print("Please, choose between yes or no")


def dealer_hit(dealer):
    while dealer.hand.check_hand_value() <= 17:
        card = dealer.deal()
        dealer.hit(card)
        if dealer.busted():
            print(f'Dealer busted!')
            break

    dealer.show_cards(True)


def buy_chips(player):
    while True:
        player_answer = input(f'You have {player.chips.chips} chips. Do you want to buy chips? (yes/no) Answer: ').lower()

        if player_answer == 'yes':
            while True:
                try:
                    player_chips = int(input('How many chips do you want to buy? Answer: '))

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


def check_winner(dealer, player):
    if dealer.busted() or player.hand.check_hand_value() >= dealer.hand.check_hand_value():
        player.win()
        print('Congratulations, you won!')
    else:
        print('Sorry but you lost!')
        print(f"You have {player.hand.check_hand_value()} points and the dealer's got {dealer.hand.check_hand_value()} points")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    main()
