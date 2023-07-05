import os
import random

symbols = ['X', 'O']

class Player(object):
    all_players = []

    def __init__(self, name):
        self.name = name
        self.all_players.append(self)

    def remove(self):
        self.all_players.remove(self)

    def change_name(self, name):
        self.name = name


def find_player(name):
    for player in Player.all_players:
        if player.name == name:
            break
    else:
        return None
    return player

def add_player(name):
    if find_player(name) is None:
        new_player = Player(name)
        print('Successfully add new player')
    else:
        print('Player with this name exist.\nFail to add new player')

def remove_player(name):
    if find_player(name) is None:
        print('Player with this name does not exist.')
    else:
        player = find_player(name)
        player.remove()
        print('Successfully remove player')

def show_players():
    for i, player in enumerate(Player.all_players):
        print(player.name)

def modify_player(old_name, new_name):
    if find_player(old_name) is None:
        print('Player with this name does not exist.')
    elif (find_player(new_name) is not None):
        print('Player with this new name exist.')
    else:
        player = find_player(old_name)
        player.change_name(new_name)
        print('Successfully player name changed')

def handle_players():
    while True:
        print('You are at manage players menu')
        command = input("Please enter a valid command: ")
        os.system('clear')
        match command:
            case 'add new player' | '1':
                add_player(input('Please enter player name: '))
            case 'show players' | '2':
                show_players()
            case 'change player name' | '3':
                old_name = input('Please enter player name: ')
                new_name = input('Please enter new name: ')
                modify_player(old_name, new_name)
            case 'remove player' | '4':
                remove_player(input('Please enter player name: '))
            case 'help':
                print('1: add new player')
                print('2: show players')
                print('3: change player name')
                print('4: remove player')
                print('0: quit')
            case 'quit' | '0':
                break
            case _:
                print("Invalid command.")

def start_new_game(player1, player2):
    turn = random.choice([1 , 2])

    def initial_game():
        player_symbol = [None, None]
        if turn == 1:
            while True:
                choice = input('Player 1 choose his symbol: ')
                if choice in ['X', 'O']:
                    player_symbol[0] = choice
                    break
                else:
                    print('Please choose a valid symbol. (X or O)')
            player_symbol[1] = 'O' if player_symbol[0] == 'X' else 'X'

        else:
            while True:
                choice = input('Player 2 choose his symbol: ')
                if choice in ['X', 'O']:
                    player_symbol[1] = choice
                    break
                else:
                    print('Please choose a valid symbol. (X or O)')
            player_symbol[0] = 'O' if player_symbol[1] == 'X' else 'X'

        return player_symbol

    player_symbol = initial_game()
    game_board = [['-', '-', '-'] for i in range(3)]
    os.system('clear')

    while True:
        if turn == 1:
            print('Turn for player 1')
        else:
            print('Turn for player 2')

        for i in range(3):
            for j in range(3):
                print(game_board[i][j], end=' ')
            print()

        try:
            row, col = list(map(int, input('Please enter the position you want to play: ').split()))
        except Exception:
            os.system('clear')
            print('Error! Please enter the position you want to play in a true format. (for example your input could be 1 3)')
        else:
            os.system('clear')
            if 0 < row < 4 and 0 < col < 4:
                if (game_board[row - 1][col - 1] == '-'):
                    game_board[row - 1][col - 1] = player_symbol[turn - 1]
                    turn = 1 if turn == 2 else 2

                    def check_for_win():

                        for i in range(3):
                            for j in range(2):
                                if game_board[i][j] != game_board[i][j + 1] or game_board[i][j] == '-':
                                    break
                            else:
                                return True

                        for j in range(3):
                            for i in range(2):
                                if game_board[i][j] != game_board[i + 1][j] or game_board[i][j] == '-':
                                    break
                            else:
                                return True

                        if (game_board[0][0] == game_board[1][1]
                                and game_board[1][1] == game_board[2][2]
                                and game_board[0][0] != '-'):
                            return True

                        if (game_board[2][0] == game_board[1][1]
                                and game_board[1][1] == game_board[0][2]
                                and game_board[1][1] != '-'):
                            return True

                        return False

                    if check_for_win():
                        print(f'Player {turn} wins the game!')
                        break

                    def check_for_draw():
                        for i in range(3):
                            for j in range(3):
                                if game_board[i][j] == '-':
                                    return False
                        return True

                    if check_for_draw():
                        print('Draw!')
                        break
                else:
                    print('Error! You can not play at this positon')
            else:
                print('Error! You must choose your number in [1,3]')

def main_menu():
    while True:
        print('You are at main menu')
        command = input("Please enter a valid command: ")
        os.system('clear')
        match command:
            case 'manage players' | '1':
                handle_players()

            case 'start new game' | '2':
                player1 = input("Please enter first player's name: ")
                if find_player(player1) is None:
                    print('Player with this name does not exist')
                else:
                    player2 = input("Please enter second player's name: ")
                    if find_player(player2) is None:
                        print('Player with this name does not exist')
                    else:
                        start_new_game(player1, player2)

            case 'show history' | '3':
                pass
            case 'help':
                print('1: manage players')
                print('2: start new game')
                print('3: show history')
                print('0: quit')
            case 'quit' | '0':
                break
            case _:
                print("Invalid command.")

main_menu()