import os
import random

symbols = ['X', 'O']
history = []


class Player(object):
    all_players = []

    def __init__(self, name):
        self.name = name
        self.all_players.append(self)

    def remove(self):
        self.all_players.remove(self)

    def change_name(self, name):
        self.name = name


class Board(object):
    global history

    def __init__(self, player1_name, player2_name):
        self.players = [player1_name, player2_name]
        self.game_board = [['-', '-', '-'] for _ in range(3)]
        self.turn = random.choice([1, 2])
        self.symbols = self.initial_game()

    def initial_game(self):
        players_symbols = [None, None]
        if self.turn == 1:
            while True:
                choice = input(f'Player {self.players[0]} choose his symbol: ')
                if choice in ['X', 'O']:
                    players_symbols[0] = choice
                    break
                else:
                    print('Please choose a valid symbol. (X or O)')
            players_symbols[1] = 'O' if players_symbols[0] == 'X' else 'X'

        else:
            while True:
                choice = input(f'Player {self.players[1]} choose his symbol: ')
                if choice in ['X', 'O']:
                    players_symbols[1] = choice
                    break
                else:
                    print('Please choose a valid symbol. (X or O)')
            players_symbols[0] = 'O' if players_symbols[1] == 'X' else 'X'

        os.system('clear')
        return players_symbols

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(self.game_board[i][j], end=' ')
            print()

    def print_turn(self):
        if self.turn == 1:
            print(f'Turn for {self.players[0]}')
        else:
            print(f'Turn for {self.players[1]}')

    def start_game(self):
        while True:

            self.print_turn()
            self.print_board()

            # noinspection PyBroadException
            try:
                row, col = list(map(int, input('Please enter the position you want to play: ').split()))
            except Exception:
                os.system('clear')
                print('Error! Please enter the position you want to play in a true format. '
                      '(for example your input could be 1 3)')
            else:
                os.system('clear')
                if 0 < row < 4 and 0 < col < 4:
                    if self.game_board[row - 1][col - 1] == '-':
                        self.game_board[row - 1][col - 1] = self.symbols[self.turn - 1]

                        if self.check_for_win():
                            print(f'Player {self.players[self.turn - 1]} wins the game!')
                            history.append({'player1': self.players[0], 'player2': self.players[1],
                                            'result': 'win', 'winner': self.players[self.turn - 1]})
                            return
                        if self.check_for_draw():
                            print('Draw!')
                            history.append({'player1': self.players[0], 'player2': self.players[1],
                                            'result': 'draw', 'winner': None})
                            return

                        self.turn = 1 if self.turn == 2 else 2
                    else:
                        print('Error! You can not play at this position')
                else:
                    print('Error! You must choose your number in [1,3]')

    def check_for_win(self):

        for i_ in range(3):
            for j_ in range(2):
                if self.game_board[i_][j_] != self.game_board[i_][j_ + 1] or self.game_board[i_][j_] == '-':
                    break
            else:
                return True

        for j_ in range(3):
            for i_ in range(2):
                if self.game_board[i_][j_] != self.game_board[i_ + 1][j_] or self.game_board[i_][j_] == '-':
                    break
            else:
                return True

        if (self.game_board[0][0] == self.game_board[1][1]
                and self.game_board[1][1] == self.game_board[2][2]
                and self.game_board[0][0] != '-'):
            return True

        if (self.game_board[2][0] == self.game_board[1][1]
                and self.game_board[1][1] == self.game_board[0][2]
                and self.game_board[1][1] != '-'):
            return True

        return False

    def check_for_draw(self):
        for i_ in range(3):
            for j_ in range(3):
                if self.game_board[i_][j_] == '-':
                    return False
        return True


def find_player(name):
    for player in Player.all_players:
        if player.name == name:
            break
    else:
        return None
    return player


def add_player(name):
    if find_player(name) is None:
        Player(name)
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
    elif find_player(new_name) is not None:
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
    board = Board(player1, player2)
    board.start_game()


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
                for i, game in enumerate(history):
                    if game['result'] == 'win':
                        print(f"{i+1} : Game between {game['player1']} and {game['player2']} played "
                              f"and {game['winner']} wins the game.")
                    else:
                        print(f"{i+1} : Game between {game['player1']} and {game['player2']} played and no one wins.")

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
