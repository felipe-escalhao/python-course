import os
import random


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def play():
    ended = False
    player = choose_first()
    player_marks = choose_mark(player)

    print(f'Player 1: {player_marks["Player 1"]}')
    print(f'Player 2: {player_marks["Player 2"]}\n')

    board = ['Null', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    while not ended:
        choose_position(player, player_marks[player], board)

        if check_status(board):
            print(f"\nThe winner is {player}!")
            ended = True
        elif not board.__contains__(' '):
            print(f"\nIt is a tie!")
            ended = True
        else:
            if player == 'Player 1':
                player = 'Player 2'
            else:
                player = 'Player 1'

    if play_again():
        clear_screen()
        play()
    else:
        print('Thanks for playing!')


def choose_mark(player):
    mark = ''

    while mark.upper() != 'X' and mark.upper() != 'O':
        mark = input('Choose X or O ')

    if mark.upper() == 'X':
        mark1, mark2 = ('X', 'O')
    else:
        mark1, mark2 = ('O', 'X')

    players = {
        'Player 1': mark1 if player == 'Player 1' else mark2,
        'Player 2': mark1 if player == 'Player 2' else mark2
    }

    return players


def display_board(board):
    model = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    clear_screen()
    print('MODEL:\n')
    print(f'{model[1]} | {model[2]} | {model[3]}')
    print(f'{model[4]} | {model[5]} | {model[6]}')
    print(f'{model[7]} | {model[8]} | {model[9]}')
    print('--------------------------------------')
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print(f'{board[7]} | {board[8]} | {board[9]}')


def choose_position(player, mark, board):
    position = 0
    while position not in range(1, 10):
        position = input(f'\nChoose a position (1 to 9) to place your mark {player}\n')

        position = int(position) if position.isnumeric() else 0

        if position in range(1, 10) and board[position] != 'X' and board[position] != 'O':
            board.pop(position)
            board.insert(position, mark)
            display_board(board)
        else:
            display_board(board)
            print('\nPlease, choose an empty and valid position!')
            position = 0


def check_status(board):
    display_board(board)
    win_conditions = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7)
    ]

    for condition in win_conditions:
        win_list = []
        for position in condition:
            win_list.append(board[position])

        if len(set(win_list)) == 1 and win_list[0] != ' ':
            return True

    return False


def play_again():
    response = ''

    while response.lower() != 'yes' and response.lower() != 'no':
        response = input('Do you wanna play again? ')

    return response.lower() == 'yes'


def choose_first():

    flip = random.randint(0, 1)

    if flip == 0:
        player = 'Player 1'
    else:
        player = 'Player 2'

    print(f"\nLet's play! {player} will start!")
    return player


play()
